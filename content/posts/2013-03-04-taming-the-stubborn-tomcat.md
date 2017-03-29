title: Taming the Stubborn Tomcat
publish: True
categories: [network security]

Today I ran into a problem that most penetration testers will encounter at some point, and whose solution required a creative approach. Therefore, I'm writing this brief article as a reference for future encounters with stubborn Tomcat servers.

I found an up-to-date Tomcat 7 server with easily guessable credentials and was able to access the Tomcat management console. At this point, compromising the server is usually a done deal. Typically, I would deploy a meterpreter shell via the Remote WAR deployment panel and proceed to pillage and pivot through the server using the SYSTEM level access that Tomcat granted me. However, this Tomcat was running on a fully patched and protected Windows Server 2008 R2 system which made this a bit more challenging.

Once I gained access to a Tomcat management console, I took the standard approach and deployed a meterpreter WAR application to the Tomcat server, but something was preventing meterpreter from exfiltrating the network. Extensive analysis proved that the target network was filtering all egress traffic from the target web server and only allowing outbound traffic for stateful TCP connections. Ingress filtering was also in place, so neither bind nor reverse meterpreter shells were possible against this server.

Next, I attempted to deploy a server side JSP shell and access it via a browser. While a JSP shell is not nearly as powerful as meterpreter, it is a SYSTEM shell nonetheless. The deployment appeared to be successful according to Tomcat, however, all attempts to access the shell via a browser returned 404 errors. The JSP shell was not being created during the deployment process for unknown reasons. Most likely the work of Antivirus software.

I tweeted for suggestions and [James Jardine](https://twitter.com/JardineSoftware) pointed me to a great [article](http://blog.secureideas.com/2013/03/admin-consoles-default-creds-and-sweet.html) and an open source WAR application called [filebrowser.war](http://sourceforge.net/projects/cmdjboss/files/filebrowser.war/download). The technique described in the article worked perfectly. I don't want to replicate content, so please read the original article for details. Below is an attack summary of the actions I took to compromise the server and surrounding environment after the initial exploitation.

1. Use the Tomcat management console to deploy the filebrowser.war application
2. Use the filebrowser application to upload a JSP shell to the filebrowser application directory.
3. Browser directly to the JSP shell.
4. Use the JSP shell to:
    - Survey the system using various post exploitation commands.
    - list volume shadow copies.
    - create a volume shadow copy.
    - copy the SYSTEM and SAM files from the created shadow copy to the filebrowser application directory.
5. Use the filebrowser application to:
    - download the SYSTEM and SAM files from the server for offline hash extraction with bkhive and samdump2.
    - upload mimikatz.exe and sekurlsa.dll to the server.
6. Use the JSP shell to execute mimikatz and extract the clear text credentials from memory. This must be done in a single command as the mimikatz interactive shell will not work through a non-interactrive web shell.

    ```
    mimikatz.exe privilege::debug sekurlsa::logonPasswords exit
    ```

7. Pivot and pwn...
8. Use the Tomcat management console to "stop" and "undeploy" the filebrowser application, destroying all resources in the application's path.

Mission complete.
