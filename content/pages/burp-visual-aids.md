title: Burp Suite Visual Aids

### Open Web Proxy

Sometimes you need a quick open web proxy. I mention an example in [this](/2016/12/01/proxying-thru-virtual-client-vpns/) article where I use an open proxy to proxy tools on my host system through a VPN that terminates inside a virtual client. Burp Suite Free is great for this. The two key configuration options are configuring the Burp Proxy to pass through SSL, and to not record any traffic. We're not doing anything in this scenario but proxying traffic, so we don't want this instance of Burp terminating TLS, and we definitely don't need to waste resources on storing traffic we'll never use.

[![](/images/burp-visual-aids/open_proxy.png)](/images/burp-visual-aids/open_proxy.png)

### Disable Browser XSS Protections

Here's a cross-platform technique for disabling those pesky browser XSS protections. The rule to add the `X-XSS-Protection` header exists as a default rule in Burp, but you'll have to add the rule that removes any existing `X-XSS-Protection` header or browser XSS protections will not be disabled for applications that explicitely enable them. The reason is, the RFC specifically states that the values of multiple headers with the same name are concatenated under one header and separated with a semicolon. Therefore, if the target application sets the header `X-XSS-Protection: 1; mode=block`, and we have Burp set an additional header of `X-XSS-Protection: 0`, the parsed value at the browser becomes `X-XSS-Protection: 1; mode=block; 0`, which in my testing resulted in only the first value being processed and the protection still enabled.

[![](/images/burp-visual-aids/xss_protection.png)](/images/burp-visual-aids/xss_protection.png)

### SSL Stripping Configuration

Do this before visiting the website. After making the configuration change, type the target URL  without the protocol into the address bar and hit enter. If the target is vulnerable, Burp will strip the SSL and render the page over an unencrypted session. At this point, I typically click on the address bar where the lock, etc. would normally be and take a screen shot of the message stating that the page is not protected.

[![](/images/burp-visual-aids/ssl_strip.png)](/images/burp-visual-aids/ssl_strip.png)

### Quick'n'Easy Method Interchange

Don't be like me and manipulate protocol data manually to test for Method Interchange.

[![](/images/burp-visual-aids/method_interchange.png)](/images/burp-visual-aids/method_interchange.png)

### Scan Thoroughly

This.

[![](/images/burp-visual-aids/scanner_thorough.jpg)](/images/burp-visual-aids/scanner_thorough.jpg)

[![](/images/burp-visual-aids/scanner_thorough.png)](/images/burp-visual-aids/scanner_thorough.png)

### Scan Defined Insertion Points

For scanning, I use this almost exclusively. This provides a lot of control over what gets scanned and allows for scanning all parts of the protocol.

[![](/images/burp-visual-aids/scan_param.png)](/images/burp-visual-aids/scan_param.png)

### Disable Intercept by Default

Don't lie... you've sat there staring at your browser, wondering why the application wasn't responding. Then, after 10 minutes of troubleshooting, you realized that the Intercept tab was glowing orange in the background. Yeah, we've all been there. Burp finally solved that problem.

[![](/images/burp-visual-aids/disable_intercept.png)](/images/burp-visual-aids/disable_intercept.png)

### Filter Out the Noise

Did you know that Burp has a filter for what is displayed in the Targets, HTTP history, and Websockets history tabs? If not, it's probably because the button that opens the filter is poorly styled for its position in the interface. No worries, here's how you access the filter. This is extremely useful for filtering out unimportant content-types and out-of-scope requests/responses.

[![](/images/burp-visual-aids/filter_ribbon.png)](/images/burp-visual-aids/filter_ribbon.png)

### Configure for Privacy

Prevent leaking client information to 3rd parties.

Keep in mind that disabling performance feedback will prevent Portswigger from helping determine the reason for a crash, and fixing any issues that may have caused it.

[![](/images/burp-visual-aids/privacy_1.png)](/images/burp-visual-aids/privacy_1.png)

Burp Collaborator provides some awesome functionality, but it uses Portswigger's servers by default. This can be problematic for professional use. I highly recommend standing up your own Collaborator server (it's free afterall). Otherwise, disable it.

[![](/images/burp-visual-aids/privacy_2.png)](/images/burp-visual-aids/privacy_2.png)
