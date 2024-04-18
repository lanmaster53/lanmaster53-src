title: 'Blowing the Whistle on Legal Bullying'
publish: False
categories: [leadership, application security, Burp Suite, development, tools]

---

I have spent the better part of a week defending an absurd case of legal bullying with one of the biggest names in web application security. I was hoping for a peaceful and fruitful resolution, but as I experienced, and you will see, that was not a possible outcome. I realize the risk I am taking by publishing this article, but if it saves one person from experiencing what I experienced, or makes one company think about doing this to another person, then it will be worth it. This kind of behavior simply cannot stand, and it is up to the community to hold companies accountable.

<!-- READMORE -->

I recently developed a tool called Burp Probe, which is a web interface that leverages the REST API exposed by Burp Suite Professional to remotely interact with the Burp Suite Pro. Within 24 hours of releasing the tool, I received a request from PortSwigger to remove the code from Github because they claimed that it violated our license agreement. I immediately took down the project and requested clarification as to why. The below conversation ensued.

Make your own judgement on what is happening here, but it is pretty clear that what started as an emotional response to something that was misunderstood, led to prideful arrogance, refusal to discuss on reasonable terms, and legal bullying to suppress the distribution of perfectly legal software that will ultimately help the community, and oddly enough, the PortSwigger brand.

---

Hi Tim,

I hope you are well.

We recently noticed that you have developed and published an application called "Burp Probe", which is designed to integrate with Burp Suite Professional. We understand and appreciate the effort and creativity involved in creating extensions or integrations. However, this specific application constitutes a breach of our commercial [license agreement (EULA)](https://portswigger.net/burp/eula/pro).

Please can you remove the "Burp Probe" repository from GitHub and any other platforms where it may be hosted, by the close of business on Monday, 15th April. We also ask that you don't distribute this by any other means going forward.

Given our existing relationship, we were surprised to see development of an application like this proceeded without prior discussion. Should you be interested in developing any future applications or integrations involving Burp Suite Professional, we would be more than happy to discuss them with you beforehand to confirm they align with our license agreement.

Please let us know if there are any aspects you'd like to discuss or if you need any further clarification regarding this request.

Thank you for your immediate attention to this matter and for your understanding.

Kind Regards,

\[omitted\]<br>
PortSwigger

---

Hi James,

Thanks for reaching out. I appreciate the opportunity to clear up any miscommunication or misunderstanding that has taken place. I can assure you, and I tried to make it clear in Burp Probe's documentation, that I in no way intended to violate a terms of service or negatively impact PortSwigger. To the contrary, Burp Probe was meant to further demonstrate the usefulness of Burp Suite Pro while simultaneously pointing users toward the Burp Suite Enterprise product.

I have been a long time advocate of Burp Suite Pro, have trained companies and governments on how to use it, no doubt resulting in direct business to PortSwigger. I myself am a paying customer, and every company for which I have managed teams of consultants has been as well. My actions make it clear that I am an advocate for PortSwigger, not a threat.

Let me say up front that the purpose of everything to follow in this email is to gain a thorough understanding of what the issue is so that I can move forward in a way that serves everyone well. There is no ill will or desire to circumvent sound ethics on this end.

It seems to me that any potential EULA violation wouldn't apply to me in this case because Burp Probe is just a web application that operates independent of Burp Suite Pro. To demonstrate this, you can pull down Burp Probe's source code, run it, and use the interface without the Burp Suite Pro software, without a Burp Suite Pro license, and without knowing that Burp Suite Pro even exists. It wouldn't be very useful, but it would function as a web application just fine. I'm confused about how a EULA can apply to something that doesn't even require the licensed software. It seems to me that the EULA would only be relevant when a user of Burp Probe purchases their own Burp Suite Pro license and configures their instance of Burp Probe to communicate with the Burp Suite Pro REST API. At that point, if there is a EULA violation, then that would be between that licensee and PortSwigger.

Regarding EULA violation, I read through the entire EULA and was not able to find anything that would clearly prevent a user from using Burp Probe in the way it was designed. Please point me to the part of the EULA that is violated. The closest paragraphs I could find were 1.2.6 and 1.2.13. Regarding 1.2.6, Burp Suite Pro is not "combined with" or "incorporated in" Burp Probe. Again, Burp Probe runs completely independent of Burp Suite Pro. Regarding 1.2.13, Burp Probe is not an automated service offering. It's not automated, it's not a part of a service, and it isn't an offering. Burp Suite Pro's scanner is automated, but Burp Probe must explicitly invoke that action through the API that Burp Suite Pro exposes for this purpose.

That brings me to the technical perspective. I am confused why Burp Suite Pro exposes a REST API for launching scans if it is against the EULA to use it. That is all that Burp Probe attempts to do. This is no different than someone using their browser to interface with Burp Suite Pro REST API's Swagger interface to launch a scan. They are both literally web applications that launch a scan and retrieve results from a browser. Therefore, that would make using Burp Suite Pro's own Swagger interface a violation of the EULA. I find it hard to believe that PortSwigger is entrapping their own users in a EULA violation. However, to follow the thread, if using the REST API does violate the EULA, then why does the functionality even exist? To take this even further, Burp Suite Pro also exposes a command line interface. Any Bash, Python, etc. script that runs Burp Suite Pro using the CLI would also be in violation of the EULA. Yet, there are many support threads that assist with and encourage the use of the CLI without threatening of a EULA violation.

As I write this, I can't help but get the feeling that there is a misunderstanding of what Burp Probe is. Or perhaps this is simply a branding issue. I'd appreciate the opportunity to speak about this via live conversation for further clarification. Again, I am not trying to win an argument, but rather understand what the problem is so that I can move forward in a way that serves everyone well.

Thank you.

Tim Tomes

---

Hi James,

I tried to get back to you with enough time to resolve this situation today, but I realize that by this point the weekend has begun for you. With the expectation that you'll honor your offer to discuss and clarify, I have temporarily taken down the project in good faith. Have a great weekend, and I look forward to resolving this early next week.

Tim Tomes

---

Hi Tim,

Thanks for your prompt response, and we appreciate you taking down the project in the meantime.

I am currently waiting to discuss the questions in your email with our legal team to get clarification for you and will be back in touch soon with the details.

Kind Regards,

\[omitted\]<br>
PortSwigger

---

Thanks James.

I'm still interested in what prompted the initial email. Someone believed I had done something wrong enough to send the original email and I'd like to know what that is. Please clarify. 

I also find curious that a threat was sent without legal review in the first place. That makes all this seem more like an emotional response than an actual problem. I spent the entire weekend concerned about what I might have done wrong in this situation, only to find out that it is just now being reviewed for any legal wrongdoing.

I look forward to your response and the legal team's thoughts on the situation.

Tim Tomes

---

Hi Tim,

We appreciate your patience.

To clarify, we have not issued any threats, purely a polite request. You have asked for clarification around specific legal aspects concerning our license agreement, which we need to discuss with our legal team before we come back to you. They are already aware of the situation. I hope that makes sense.

Kind Regards,<br>
\[omitted\]

---

It does. Thank you.

To add some additional context to my original response, which may help the legal team better understand my position, consider the attached image.

[![](/static/images/posts/2024-04-18-blowing-the-whistle-on-legal-bullying/exhibit-1.png)](/static/images/posts/2024-04-18-blowing-the-whistle-on-legal-bullying/exhibit-1.png)

The image is from my personal PortSwigger account, which is also the account that owns Burp Probe's Github repository. As you can see, I personally do not own a Burp Suite Pro license. Burp Probe was developed using the API documentation (provided by PortSwigger  for this purpose) by a person (me) that does not personally own a Burp Suite Pro license. This could have been done by anyone, with or without a Burp Suite Pro license.

I do realize that the EULA transfers to anyone that uses a Burp Suite Pro license, even if it doesn't belong to them. However, the code base could easily belong to someone who has never used Burp Suite Pro and never agreed to the EULA. The EULA and Burp Suite Pro are completely independent of Burp Probe. If there is a EULA violation, and that's a big "if" given all of the other evidence I have presented, then the violation is not with me the developer of Burp Probe, or Burp Probe itself, but with users that choose to integrate their own deployment of Burp Probe with their own instance of Burp Suite Pro, which falls under their own agreement with PortSwigger through their own acceptance of the EULA.

This is no different than an application that integrates with a third party like Google, Twilio, etc. Any user of the application would have to go to the third party, create an account, accept a EULA, get an API key, and then add that to the application. Same as they do with PortSwigger for integrating Burp Suite Pro with Burp Probe. The developer of the application is not responsible for the user's relationship with the third party. That is between the user and the third party.

Again, this isn't even taking into account the other evidence that I presented in my initial response, which includes the fact that the API documentation is readily provided by PortSwigger for the purpose of users being able to interact with the API, which is exactly what this software does.

I hope this helps. Let me know if anyone needs further clarification.

Tim Tomes

---

Hi Tim,

Thanks again for your patience.

We can see that you have an existing Burp Suite Professional license, which was purchased last September, under your account tim.tomes@practisec.com.

**_\[The representative is referring to the license that belongs to my business, which is not my personal account and is legally separate from me as an individual. It is my personal account that shares contact information with the Github account that owns the Burp Probe repository. My company, which owns the license referenced by the representative, has a separate Github account that is not associated with Burp Probe. This point is irrelevant to the argument, but provided for clarity.\]_**

Here's some clarity on the license agreement terms:

General Terms and Conditions: Section 1.2.6
"Burp Probe" looks to be explicitly designed to integrate and interact specifically with Burp Suite Professional. Section 1.2.6 of the license agreement prohibits a licensee from permitting the software to be combined or incorporated with another program. This section still applies, regardless of whether Burp Suite Professional is packaged within your application offering or not.
 
License Agreement: Section 1.1 - Grant and scope of license 
Specifies that Burp Suite Professional is licensed to a single, named individual. Each license is non-transferable, and each individual user must have their own license.
 
"Burp Probe" looks to be a server-based web application with a user login function designed to be accessed by multiple users. This would go against the specific licensing terms that require each Burp Suite Professional user to have their own individual license. A setup like this can enable the shared use of a single license among multiple individuals, which contradicts the stipulation that each license is for a single, named individual.

Kind Regards,<br>
\[omitted\]

---

Hi James,

I appreciate the response, but somehow after all of the evidence and explanations I have provided, the point has still been completely missed.

It can't be said any clearer than this. EULA stands for "End User License Agreement". Burp Suite Probe is not an End User and cannot agree to a EULA, so by definition, it cannot be subject to any EULA. Period. The only reason we can be having this conversation is because I am a USER of Burp Suite Pro, NOT because I am the developer of an application. Anyone in the world, without a Burp Suite Pro license, can download and use Burp Probe without any relationship with PortSwigger. Burp Probe is irrelevant to this conversation. Your issue has to be with me, a Burp Suite Pro user. It's literally in the name of the agreement in question.

Regarding "General Terms and Conditions: Section 1.2.6", someone from PortSwigger should decide what their definition of a REST API is. The Oxford dictionary defines an API as "a set of functions and procedures allowing the creation of applications that access the features or data of an operating system, application, or other service." PortSwigger appears to agree with this definition because below is an image taken directly from PortSwiggers website which says explicitly "The REST API enables external tools to integrate with Burp Suite."

[![](/static/images/posts/2024-04-18-blowing-the-whistle-on-legal-bullying/exhibit-2.png)](/static/images/posts/2024-04-18-blowing-the-whistle-on-legal-bullying/exhibit-2.png)

How can your documentation say one thing and the EULA be loosely interpreted to something that completely contradicts it? Your website literally says it provides the ability to do what your email says a user can't do. This point demands explanation because it simply makes no sense.

Regarding "License Agreement: Section 1.1 - Grant and scope of license", your email said Burp Probe was a, "web application with a user login function designed to be accessed by multiple users", but if anyone had bothered to look at the tool, they would have seen that this is a completely false statement. There is only one user account, no registration system, and no user management feature. Burp Probe is a single user tool. Therefore, this point is invalid. Ironically, Burp Probe has more access control than Burp Suite Pro, which doesn't require any form of authentication to use. Reasonable measures have been taken to ensure that only the person that runs the software, and is sitting on the server's terminal when it is launched, has access to the credentials, and only the first time it is launched. Again, the software itself cannot be the subject of a EULA violation, but this shows that even a licensed Burp Suite Pro user does not violate this section of the EULA by using Burp Probe.

This all seems so unnecessary James. It is painfully clear that no one is taking the time and effort to make sure this situation is fully understood by whoever is making these statements. Given that both of PortSwigger's concerns have been simply and thoroughly refuted, I must ask, what is PortSwigger's real concern and desired end game? What is the root problem? Because all of this back and forth and refusal to accept what is plainly documented and understood is just silly.

I am available 0900 and 1600 Eastern Time, except today from 1130-1330. Please schedule a time when we can talk on the phone between today or tomorrow, in that window. That is the same amount of time you gave me to respond to your original email, so I hope that you will afford me the same level of respect that I afforded you. Thank you.

Tim Tomes

---

Hi Tim,

Thank you for sharing your perspective on this matter.

While we value your input and the discussion thus far, sorry, but we will not be engaging further on this topic.

We trust that you will continue to comply with the removal of the repository as requested and refrain from further distribution or development that may conflict with our license agreement.

Thank you for your understanding and cooperation.

Kind Regards,

\[omitted\]<br>
PortSwigger

---

FIN
