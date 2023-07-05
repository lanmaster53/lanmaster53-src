title: Getting Shell in Modern Restricted User Environments
publish: True
categories: [network security]

---

Anyone that has been doing penetration tests for a reasonable amount of time has at some point encountered a restricted user environment. A restricted user environment is a locked down, and usually shared, environment which restricts users to very limited functionality. These configurations are commonly seen in public kiosks and shared terminal servers.

<!-- READMORE -->

The first instinct to achieve shell in one of these environments is to simply run "cmd.exe". In most cases, it's not that easy. Finding a means to run "cmd.exe" can be challenging. The typical routes such as the "Run" command, Windows Explorer, and "Programs" menu are usually disabled. But there are ways to do it. Below I cover one such technique I have been using for several years and have not seen documented elsewhere. It leverages Internet Explorer Developer Tools. Let me show you how it works.

Most restricted user environments exist solely to provide functionality that is accessed via a web browser. Therefore, Internet Explorer is authorized in just about every restricted Windows environment. While not guaranteed, it has been available in every such environment that I have encountered to date. Built into Internet Explorer is the feature that we are going to leverage, a feature named Developer Tools.

[![](/static/images/posts/restricted_dev_tools.png)](/static/images/posts/restricted_dev_tools.png)

The Internet Explorer Developer Tools provide similar functionality to that of Chrome and Firefox. However, there is some additional functionality that becomes quite beneficial in solving our current predicament. Once the Developer Tools panel is loaded via pressing the "F12" key or clicking on "Developers Tools" in the "Tools" menu, a click on the "File" menu of the Developer Tools panel reveals an option named "Customize Internet Explorer view source".

[![](/static/images/posts/restricted_customize.png)](/static/images/posts/restricted_customize.png)

This menu option allows the user to select which program on the local system is used to load the HTML source of a web page in Internet Explorer when the "View Source" menu item is selected on the "Page" menu. The first instinct of any penetration tester should be to browse to "cmd.exe", select it as the program, click "OK", then view the source of any web page. While this sounds like a decent plan, there are 2 issues that must be addressed before we can achieve shell this way.

The first issue is that in restricted user environments, direct access to the contents of the system drive is usually disallowed. The solution to this problem is very simple. By typing the drive letter of the system drive in the "File name" box and hitting the "Enter" key, we are greeted with the contents of the drive.

[![](/static/images/posts/restricted_filename.png)](/static/images/posts/restricted_filename.png)

At this point, we browse to the "C:\Windows\System32" folder, select "cmd.exe", and view the source of any web page. We are promptly greeted with the following result.

[![](/static/images/posts/restricted_disabled.png)](/static/images/posts/restricted_disabled.png)

This is the second issue. Administrators have become savvy to the use of the command prompt by those looking to conduct nefarious activities on their tightly controlled system, and have leveraged local security policy to disable it. Fortunately, solving this issue is almost as easy as the first, but with a little twist.

[![](/static/images/posts/restricted_ps.png)](/static/images/posts/restricted_ps.png)

PowerShell fans everywhere should be screaming at me through their computer screens right about now. The partial answer here is to try and execute PowerShell rather than "cmd.exe" as it is often forgotten by administrators and is not restricted by the security policy setting that explicitly disables the command prompt.

[![](/static/images/posts/restricted_policy.png)](/static/images/posts/restricted_policy.png)

So we use the "Customize Internet Explorer view source" approach from above to browse to "C:\Windows\System32\WindowsPowerShell\v1.0", select "powershell.exe", and again view the source of any web page. This time around, we are greeted with the following result.

[![](/static/images/posts/restricted_ps_error.png)](/static/images/posts/restricted_ps_error.png)

This image was difficult to capture because, unfortunately, PowerShell doesn't understand the use of a cached HTML file name as syntactically correct input, fails, and exits without providing access to the shell. Bummer. However, there is still another option. Look back 3 images and notice the "powershell\_ise.exe" file. The "powershell\_ise.exe" program is the PowerShell Integrated Scripting Environment (ISE). It just so happens that by using this as our program to view the source of web pages in Internet Explorer, we are greeted with the following result.

[![](/static/images/posts/restricted_ise.png)](/static/images/posts/restricted_ise.png)

A friendly PowerShell IDE! We see our HTML loaded into the script editor and an interactive PowerShell prompt at the bottom of the window. The output from our commands populate the middle pane. This should be sufficient to move forward, but if you would rather have a raw PowerShell prompt, simply click the PowerShell button at the top of the page and you have your wish.

[![](/static/images/posts/restricted_ise_shell.png)](/static/images/posts/restricted_ise_shell.png)

At this point, we have accomplished our goal of gaining shell access in the restricted user environment. We can now use PowerSploit to conduct all kinds of nastiness on the target machine and take measures to elevate privilege.

From the defensive perspective, how do we prevent this type of attack? I am no Active Directory expert, but I am intimately familiar with the concepts of white listing and black listing. There are security policy rules that allow for explicit filtering of accessible programs in restricted user environments.

[![](/static/images/posts/restricted_defense.png)](/static/images/posts/restricted_defense.png)

I recommend using one of these security policy rules, preferably the white list rule, to ensure that binary executables which can result in shell are inaccessible to the user.
