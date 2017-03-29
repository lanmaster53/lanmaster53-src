title: Defending Against SSL Stripping Attacks
publish: True
categories: [application security]

SSL Stripping is an attack originally disclosed by Moxie Marlinspike (@moxie) at BlackHat DC 2009 along with a tool called SSLStrip. SSL Stripping is an attack that takes advantage of the fact that server-side redirects are used to redirect clients from HTTP versions of a page to the HTTPS, SSL encrypted, version. SSL Stripping tools, such as SSLStrip, listen for requests from clients that receive a response intended to redirect the client to a HTTPS resource. SSL Stripping tools hijack this response, make the SSL encrypted HTTPS connection to the server, convert all instances of "https" to "http" within the legitimate content, and pass the modified content to the unsuspecting client over unencrypted HTTP. The attacker can then view all of the traffic between the client and the server in clear text while brokering the half encrypted connection.

The benefit of SSL Stripping over traditional HTTPS man-in-the-middle is that HTTPS man-in-the-middle requires that the victim accept an invalid or untrusted SSL certificate in order to complete the attack. This is an obvious clue to the target that something is amiss. SSL Stripping provides very few visual clues that the target is being compromised.

SSL Stripping attacks target the client's trust of the response from the server. Therefore, in order to prevent SSL Stripping, the client must be responsible for ensuring that SSL is used where needed. Sounds dangerous right? Putting any level of control in the hands of the client is always dangerous. However, in this case, there is no other choice. The client HAS to be the decision maker. There are several ways to address this issue.

The most common approach to solving the SSL Stripping problem is to implement HTTP Strict Transport Security (HSTS). HSTS is an OPT-IN protocol that is activated by the use of a "Strict-Transport-Security" (STS) HTTP response header. the STS header tells the browser to add the origin host to its internally maintained HTTPS-only list. Any host in the HTTPS-only list will be requested via HTTPS, regardless of what the user enters as the URL. This prevents the initial HTTP request that results in the vulnerable redirection. Furthermore, some browsers utilize a HSTS preload list. Administrators can submit their hosts to the various browser vendors to be included in the preload list.

There are several problems with HSTS. The first issue is that the STS header must be transmitted from the server to the client via HTTPS. Therefore, the issue still remains that the initial connection between the client and server can be "SSL stripped" before the host ever gets added to the HTTP-only list. Getting preloaded into the HTTP-only list solves this problem, but there's a second problem that isn't as easy to remediate.

What about legacy browsers that don't support HSTS? There's really only one option, and it's not even a great one. JavaScript can be used to enforce HTTPS as opposed to waiting for a server redirect. This adds an extra (thin) layer of security by using the browser to enforce HTTPS from the client-side, preventing the vulnerable client-server exchange. Now before you start flaming this article, let me finish. It must be understood that while this will work, a man-in-the-middle still has control over all cleartext responses from the server to the client. Therefore, if a man-in-the-middle is aware of the JavaScript-based anti-SSL Stripping mechanism, they can customize their SSL Stripping tool to also strip the anti-SSL Stripping code out of the response, rendering the client defenseless. Like I said, it's not a great solution, but it is the only option for legacy browsers.

The following is an example of JavaScript code will force the client-side of an application to connect to the HTTPS version of a page.

``` JavaScript
var proto = String.fromCharCode(104,116,116,112,115,58);
if (window.location.protocol != proto) {
    window.location.href = proto + window.location.href.substring(window.location.protocol.length);
}
```

Let's walk through the code.

Line 1 creates a variable called "proto" which has a string value of "https". The reason we create the string this way is to avoid where SSL Stripping tools search and replace all instances of "https" with "http". SSL Stripping tools could add this to the search and replace, but think of how many different ways we can create and obfuscate JavaScript code to create a string equal to "https". Actually, it's limitless. Consider the following JavaScript:

``` JavaScript
var proto = String.fromCharCode(105-1,114+2,118-2,110+2,118-3,55+3)
```

This creates the string "https". As long as we're dealing with math, we have unlimited possibilities. Line 2 checks to see whether the protocol of the current location of the DOM is "https". If it is not, then line 3 redirects the client to the "https" version of the page. Since the decision is being made on the client side, SSL Stripping tools do not have the opportunity to hijack the redirect from the server, and SSL Stripping is averted.
