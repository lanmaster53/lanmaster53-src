title: Recon-ng Update (v3.3.3)
publish: True
categories: [projects, tools, Recon-ng]

---

Some users may have noticed an usually high number of bugs over the past couple of weeks. We've been making some sweeping changes to the guts of the framework during that time, and since the entire user population is the beta test community, you have been instrumental in helping spot and fix issues. For that I thank you. We've been trying to fix bugs as fast as they've been reported, so at this point, I believe most issues have been identified and resolved. However, please continue to report any strange behavior or bugs.

<!-- READMORE -->

Also taking place over the past several weeks was voting for the 2013 Toolsmith Tool of the Year and the ToolsWatch 2013 Top Security Tools competitions. Users voted the Recon-ng framework as the #1 2013 Toolsmith Tool of the Year and the #7 ToolsWatch Top Security Tools of 2013 (ahead of Metasploit, WOW!). This acknowledgment of the Recon-ng framework as a popular and useful addition to professional's toolsets across the industry validates the time that's been poured into its development. After all, the good of the industry and making an overall positive impact on security is the reason I do this.

In appreciation of your votes, and because I just generally enjoy working on Recon-ng, quite a few new features have been added to the framework. Below is a quick round-up of the new features.

### Browser Emulation via Mechanize

Many users may have noticed the obvious absence of harvesting modules for resources like Facebook and Pastebin. This has been due to the way that these web sites require true browser functionality to render the desired content. None of the builtin web request modules (urllib, urllib2, httplib) have the ability to do this natively. Therefore, the popular Mechanize browser emulator package has been added to the framework. Now, any resource that requires true browser-like functionality to access data can be leveraged by the framework.

### Persistent Module Options (Migration Required)

We've been receiving requests for quite some time to make module options persist across sessions like the global options always have. One of the sweeping changes that took place over the past several weeks was an overhaul of the options management system. Now, all options at all contexts are stored and loaded dynamically. Therefore, if there is a module that inherits a global option, but you want it set as something else, you won't have to reset it every time you return to that module. This also makes debugging much easier for developers who are working with specific test scenarios. All options are still stored according to workspace, so there is no danger of information leakage between engagements. In order for this new feature to work properly in existing workspaces, remove the old "config.dat" file in the workspace and allow it to be dynamically regenerated the next time the workspace is loaded. A huge thanks to [Ethan Robish](https://twitter.com/EthanRobish) for making this feature a reality.

### Output Spooling

Since the inception of the framework, I've wanted the ability to spool output to a local file for data retention, proof of performance, and general CYA reasons. However, we've tried multiple implementations in testing and never liked any of them enough to push to the master branch. We've also tried all of the builtin OS tools like "tee" and "script", but they break functionality, like tab completion, and muck with output formatting. A couple weeks ago, a brilliant contributor, [Quentin Kaiser](https://bitbucket.org/qkaiser), put me on to a technique that looked promising. A few nights later, a solution was pushed to the master branch that accomplishes spooling quite well. Spooling has been implemented as the "spool" command, and works very similarly to the "record" command by giving users the ability to start and stop spooling, or check the current spooling status. The destination file for the spooled data is set as a parameter of the "spool start" command, `spool start <filename>`.

### JSON Support for Requests

It wasn't until I recently attempted to send a POST request with a JSON payload that I realized the custom requests method built for Recon-ng didn't support anything but standard POST content subtypes. Therefore, support for JSON content subtypes was implemented by adding a "content" parameter to the "request" method that accepts a string identifying the content subtype. While only JSON is currently supported, this implementation allows for other content subtypes to be easily added at a later time. In addition to this, the custom requests method was separated from the framework and placed into a module called "dragons.py" (as in, "here they lie"). This was done so that I, or anyone else, can leverage its functionality in other projects, as it does such a good job of simplifying the many things that can be done with web requests and urllib2.

### Revamped HTML Report

The HTML reporting module was something thrown together early on in development and was never revisited to make it a more polished product. Well, it's finally been done. With the new HTML reporting module, you'll notice a much cleaner interface with expanding ribbons for each section of the report, making it is easy to drill down into the content. Like before, the report is a static HTML file. All of the dynamic features are implemented using JavaScript and CSS that is built into the template. Therefore, you can easily send the HTML file to the customer as an appendix to your overall report.

### Conclusion

If you're interested in contributing to the framework, please see the [issues page](https://bitbucket.org/LaNMaSteR53/recon-ng/issues?status=new&status=open) for module ideas and feature requests. All contributions are welcome from anyone with any level of Python experience, including no experience. I am in this to teach as much as I am to develop, and I thoroughly enjoy helping those new to Python. Thanks again, and enjoy the framework.

[Recon-ng Home Page](http://www.recon-ng.com)
