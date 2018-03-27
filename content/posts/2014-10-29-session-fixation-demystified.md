title: Session Fixation Demystified
publish: True
categories: [application security]

I've recently been approached by quite a few junior consultants having issues with understanding, discovering, and exploiting Session Fixation. Rather than continue to provide impromptu training, I decided to brain dump everything I know about Session Fixation into an article for reference.

<!-- READMORE -->

While not as sexy as many of the other vulnerabilities we deal with in Application Security, Session Fixation is quite common and exposes applications and users to substantial risk. I see Session Fixation behavior in approximately 60% of the applications I test, with it being exploitable in approximately a quarter of those instances.

### Session Fixation Defined

Session Fixation is a vulnerability that allows an attacker to predetermine the session token value of a victim. Like Session Hijacking, Session Fixation allows the attacker to assume the identity of the victim user in the context of the application. The root cause of Session Fixation is when an application does not provide a new session identifier, or token, upon successful authentication. In many cases, application's unnecessarily issue session tokens prior to authentication. In other cases, application's contain core business functionality in the pre-authentication pages that require an active session (e-commerce). These 2 conditions, if not handled properly, can result in Session Fixation.

Let's use Amazon as an example. When a user goes to Amazon.com, they can shop the catalogue of items and add items to their shopping cart prior to authenticating. In order for Amazon to maintain state with the user, Amazon must create a session to manage the user's data and issue a token to the user's browser. When the user decides to purchase the items they have added to their unauthenticated shopping cart, they must authenticate to Amazon. This is the important part. When the user successfully authenticates, Amazon must take all of the information associated with the user's unauthenticated session and associate it with a new session. Amazon must then expire the old session token, and replace it with the token associated with the new session. If Amazon does not create a new session upon successful authentication, then theoretically, an attacker could go to Amazon first, be issued a session token for a valid unauthenticated session with the application, fixate that session into a victim's browser, and wait for the victim to log in. After the victim logs in with the attackers fixated session, all the attacker has to do is refresh their browser and they will be authenticated as the victim.

### Discovering Session Fixation

Determining if an application is susceptible to Session Fixation is easily accomplished with the following steps.

1. Map the unauthenticated portion of the application.
2. Determine if a session cookie has been set in the browser. This can be done by looking at the `Set-Cookie` headers generated through mapping, using the browser's Developer Tools to view cookies associated with the current domain, or by looking at the `Cookie` header sent with the most recent request.
3. If a session token exists, note the value.
4. Authenticate to the application.
5. Compare the post-authenticated session token to the pre-authenticated session token. If they are the same, Session Fixation exists.

Regardless of exploitability, which we'll discuss shortly, I consider the existence of Session Fixation behavior to be a low risk finding because it shows failure to design a Session Management system according to security best practices.

### Exploiting Session Fixation

If you are the inquisitive type, then you immediately picked up on the statement, "...fixate that session into a victim's browser..." in the Amazon scenario above and said to yourself, "How do you do that?". Good question. This is the second, and more difficult, part of Session Fixation. The previously discussed behavior means that the potential for Session Fixation exists, but exploitability is still in question. In order to exploit Session Fixation, one of several conditions must exist.

- Cookieless sessions used for session management.
- Cross-Site Scripting (XSS) in the unauthenticated portion of the application.
- XSS in another application on the same domain.

#### Cookieless Sessions

Cookieless sessions are sessions that are managed by a token that is passed in some form other than a cookie. This means that the session token is passed between the client and server as a parameter in the URL, a parameter in the POST payload, or embedded in the URL. Below is an example of a .NET cookieless session. .NET rewrites each URL on the page to include the session token.

```
http://www.example.com/s(lit3py55t21z5v55vlm25s55)/orderform.aspx
```

There are several reasons for using cookieless sessions. Cookieless sessions allow for multiple sessions with the same browser instance. Have you ever tried to log into a cookie based application on 2 different tabs with 2 different accounts in the same browser instance? It doesn't work in most cases. It is difficult for an application to allow for multiple simultaneous sessions when using Cookies. Cookieless sessions allow for it seamlessly. Cookieless sessions also allow for session management in browsers that don't support cookies. Nowadays cookie support shouldn't be an issue, but you never know what kind of technical restrictions your client may be operating under.

The problem with cookieless sessions is that they provide the potential for several vulnerabilities. They can result in Information Disclosure as they may allow the session token to be disclosed in logs, Referer headers, proxies, and caches. They also allow Session Fixation to be exploited by providing a mechanism for an attacker to fixate a session into a victim's browser. Let's revisit the Amazon example and pretend that Amazon uses cookieless sessions where the session token is embedded in the URL, and does not issue new session tokens upon successful authentication. An attacker can go to Amazon and be issued a valid unauthenticated session token. The attacker can then craft a link to Amazon with the valid session token embedded in the URL and send it to the victim as part of a Social Engineering attack. The victim opens the link, sees that they are not authenticated to Amazon, and authenticates. The attacker refreshes his browser and assumes the identity of the victim in the context of the application. The ability to dictate the session token value through a request parameter or URL makes exploiting Session Fixation trivial.

I consider Session Fixation that is exploitable via cookieless sessions a high risk finding as it is extremely easy to exploit, requiring only the click of a link, and provides a likely vector of attack for privilege escalation.

#### Cross-Site Scripting (XSS)

The Document Object Model (DOM) within the browser allows for cookies to be created and overwritten with JavaScript. If XSS exists somewhere in the application prior to authentication, then JavaScript can be used to overwrite the current session token cookie with an attacker's predetermined session token. One catch with this attack vector is that if the current session token cookie was created using the `HttpOnly` flag, then the cookie will not be accessible through the DOM and cannot be overwritten. However, XSS on another application within the same domain may bypass this restriction. More on this in a moment. META tags are another option for overwriting cookies where HTML injection is possible. Below are examples of injection payloads that create or overwrite a browser cookie.

- JavaScript

```
<script>document.cookie='SESSION_ID=THISISAFIXATEDCOOKIE; expires=Thu, 18 Dec 2015 12:00:00 UTC; path=/; domain=google.com; path=/'</script>
```

- HTML Injection

```
<meta http-equiv=Set-Cookie content="SESSION_ID=THISISAFIXATEDCOOKIE; expires=Thu, 18 Dec 2015 12:00:00 UTC; path=/; domain=google.com; path=/">
```

An application won't arbitrarily issue a new session token if a session token already exists. Therefore, an attacker may be able to use a XSS vulnerability in another application on the same domain to create the cookie for the target application before the victim visits the site and is issued a `HttpOnly` flagged session token cookie. This is possible because any host within a domain can create cookies that will be passed to the root domain and any host associated with it. I tested this functionality with Google using Chrome's Developer Tools and JavaScript Console. 

First, I added an arbitrary cookie to the DOM of the application running on `mail.google.com` to simulate writing a cookie via XSS.

[![](/static/images/posts/fixation_1.png)](/static/images/posts/fixation_1.png)

I then visited the root Google domain and several other hosts on the Google domain. The created cookie was passed along to each resource.

[![](/static/images/posts/fixation_2.png)](/static/images/posts/fixation_2.png)

This behavior allows us to bypass the `HttpOnly` restriction and fixate sessions on applications in the same domain via XSS.

I consider Session Fixation that is exploitable via XSS to be a medium risk finding as it still provides a likely vector of attack for privilege escalation, but requires another vulnerability to exploit. The XSS flaw is obviously rated separately and will probably receive the higher risk rating.

### Preventing Session Fixation

Preventing Session Fixation is simple. If no pre-authenticated session is required, do not issue session tokens until successful authentication has occurred. If a pre-authentication session is required, always issue new session tokens upon successful authentication. This can be done several ways. The first option focuses on the session token itself. Create a new session token, associate the new session token with the existing session, disassociate the old session token, pass the new session token to the client. The second option focuses on the entire session. Create a new session, copy all of the session data from the old session to the new session, destroy the old session, pass the token associated with the new session to the client.

### Conclusion

I'm certain that there are other ways to exploit (header injection via network attack) and prevent (anomaly detection) Session Fixation, but the approaches I mention here are the simplest and most common based on my experience as an Application Security consultant. I encourage you to continue researching the topic. I leave you with this flow chart for discovering and assigning risk ratings to Session Fixation vulnerabilities. I hope you find it useful. Enjoy!

[![](/static/images/posts/fixation_3.png)](/static/images/posts/fixation_3.png)
