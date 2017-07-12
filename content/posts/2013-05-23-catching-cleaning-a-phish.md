title: Catching and Cleaning a Phish
publish: True
categories: [network security]

This afternoon my wife looked up from her laptop and said to me, "You're gonna be proud of me. I just got phished (see image below). However, after clicking the link and seeing that it was asking me for my username and password, I logged into my Twitter account manually to see if the email was legit. It wasn't, so I deleted the email." While she thought that I should have been proud, I had obviously failed at explaining the risks of phishing attacks and it was time to dust off some incident response skills.

<!-- READMORE -->

My wife helps run her fathers company, so she handles most of the business email that the company receives. As a result, she received the following email.

[![](/images/posts/tpwitter_phish.png)](/images/posts/tpwitter_phish.png)

Looks pretty legit, right? You can't see it here, but the "from" address seems legit, and the links go to exactly where they say they're going. The trick here is that the attacker is using a URL shortener to obfuscate the final destination of the link. This is a good technique, as Twitter users are accustomed to seeing shortened URLs.

My wife did the right thing by manually going to twitter to see if she actually did receive a Direct Message, but not until after she clicked the link. Many people think that clicking links and visiting pages is okay as long as they don't enter credentials into untrusted pages. This is not the case. By merely visiting a web page, attacks can be launched against all sorts of client side technologies i.e. Java, Flash, the browser itself, etc. How each of these attacks work is out of the scope of this article. The point is, if someone clicks a link or visits a page which is hosting malicious content, they could be in trouble. Here is what the phishing site my wife encountered looks like.

[![](/images/posts/tpwitter_site.png)](/images/posts/tpwitter_site.png)

What's wrong with this picture?

As the defender of the network, I was glad that my user did not surrender credentials, but as I mentioned above, the possibility still exists that the site is hosting malware and my user's system could be infected. Is it too late? Has the damage already been done? Let's find out by taking some response actions.

The first step is safely acquiring a copy of the email. According to my good friend [Jake Williams](https://twitter.com/MalwareJake), the best way to do this is to extract the email in plain text directly from the PST where the message is stored on the local machine, or from the mail server via POP/IMAP. If the email is stored on a 3rd party mail server, this can be done using the affected user's credentials. Otherwise, the mail server administrator should have the ability to extract a copy of the email from the mail store. I acquired a copy by having the user forward me the email. This is not the preferred method, as sometimes header information is lost when emails are forwarded.

The second step is to conduct an analysis of the email. Some questions that need to be answered are:

- Where did the email come from?
- Are there embedded links?
- Where do the links go?
- Which links were clicked?
- What other users clicked the links according to traffic logs?

Since I'm dealing with a one user environment, getting these answers was simple.

The next step is to analyze the target site's invocation process and contents for signs of malicious activity. Website analysis in a safe manner used to be painful. One would have to build a customized sandboxed environment complete with IDS, exploitable client side technologies, etc. However, thanks to the fine folks at [URLQuery.net](http://urlquery.net/), all of these things are now available to us pain free.

URLQuery.net is a malicious web page analysis tool. It runs the contents of the given page through the proverbial "wringer". URLQuery.net loads web pages through two different Intrusion Detection Systems with commercial rule sets (Suricata and Snort), executes the content intended for client side technologies such as JavaScript, Java and Adobe Reader, and provides a detailed report on the results, including traffic analysis. The results for the page in question can be seen below. The level of information given is incredible. Take a few moments to analyze the report.

[![](/images/posts/tpwitter_urlquery.png)](/images/posts/tpwitter_urlquery.png)

As you can see, there isn't much danger on this site other than the fact that someone from Russia is trying to harvest Twitter credentials. Granted, there could be 0-day exploits embedded, but as far as we can see as first responders, things seem clean for now. Disaster averted.
