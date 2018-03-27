title: Local File Inclusion to Remote Command Execution using SSH
publish: True
categories: [application security]

Log poisoning has been used for years to upgrade local file inclusion vulnerabilities to remote command execution. In most cases, web server logs are used to execute such an attack. Most admins have become wise to the technique and do a decent job of preventing this. However, an equal amount of attention is not always paid to authentication logs.

<!-- READMORE -->

I was recently attempting to exploit a LFI vulnerability on a pen test and was having no luck poisoning the web server logs. Previous scans of the target showed that an OpenSSH service was running. I took one last shot at the LFI vulnerability and below was the result. I was shocked to find that auth.log was world readable.

[![](/static/images/posts/lfi_rce_orig_auth.png)](/static/images/posts/lfi_rce_orig_auth.png)

By default, OpenSSH makes an entry (consisting of the user name and other data) to auth.log for every authentication attempt made to the ssh daemon. Knowing this, I did some quick testing and found that I could inject php code into auth.log from the user name field of an ssh client by attempting to authenticate. The command took some time to get working right as bash requires finesse for processing special characters, but after some troubleshooting, I came up with the following:

[![](/static/images/posts/lfi_rce_cmd.png)](/static/images/posts/lfi_rce_cmd.png)

One issue I encountered is that OpenSSH makes 3 entries containing the user name to auth.log for every authentication attempt. In the following example, only one authentication attempt was made, but, as you can see, it appears in the log 3 times.

[![](/static/images/posts/lfi_rce_log.png)](/static/images/posts/lfi_rce_log.png)

The injected command will run 3 times unless php execution is terminated after the 1st command. I did this above with the `exit;` command. The unfortunate side effect is that you have one chance to get this right. Otherwise, you have to wait until the log cycles before you can make another attempt. Here is what the final product looked like with the addition of a pre-format tag for aesthetics.

[![](/static/images/posts/lfi_rce_output.png)](/static/images/posts/lfi_rce_output.png)
