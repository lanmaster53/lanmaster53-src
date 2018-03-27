title: DOM-based Cross-Site Scripting, Revisited
publish: True
categories: [application security]

Disclaimer: I am not an subject matter expert in DOM-based XSS (D-XSS). In fact, I have yet to see an exploitable D-XSS flaw in all my years of application security testing. However, I have a curious mind and love code, so I am always looking to learn more about web application flaws and uncover new ways to approach finding and exploiting them. That being said, if you have experience dealing with D-XSS and would like to contribute to this topic, whether to correct an inaccuracy in this article or provide insight, please send me an email or tweet. I welcome and appreciate all input.

<!-- READMORE -->

The best way to learn about a web application flaw is to experience the flaw from the position of the developer and the attacker. This can be done by conducting the following exercises.

- Write an application that intentionally implements the flaw in a realistic scenario.
- Practice exploiting the application through modern day browsers.
- Modify the application to successfully mitigate the flaw.

I make a habit of doing this for every type of flaw that gets discovered and have found that it helps to truly understand the flaw and how to prevent it through writing secure code. Repeating this exercise routinely sharpens my understanding of the flaw and provides insight into how exploit payloads are handled by modern browsers.

A few days ago I decided to revisit DOM-based XSS, as things have changed considerably from a browser perspective since I last played with the flaw. For those that are not familiar with D-XSS, it is a flaw that occurs when a developer creates dynamic content from pieces of the DOM that can be easily manipulated by the user. D-XSS differs from other types of XSS in the following ways:

- Reflected and Stored XSS
    - The payload is sent to the server, processed, and used by the application in a response.
    - The flaw exists in the server-side code.
- DOM-based XSS
    - The payload doesn't have to be sent to the server to exploit the flaw.
    - The flaw exists in the client-side code.

When a URL is given to a browser, the browser immediately begins building the Document Object Model (DOM) for the given page, even before it sends the request to the desired resource. At that point, the DOM contains all of the components required to make the request to the server including the resource URL and accompanying parameters. The request is eventually sent to the server hosting the desired resource and a response is received. D-XSS comes into play when the client-side code of the response (usually JavaScript) parses these DOM elements and creates dynamic content from them. Consider the following example code.

``` html
You are here: <span id="location"></span>
<script>
    var loc = document.location.href;
    document.getElementById("location").innerHTML = loc;
</script>
```

In the example above, the developer uses JavaScript to retrieve the value of the current page URL from the `document.location.href` DOM attribute and assigns it to a variable named `loc`. The developer then modifies the DOM and sets the `innerHTML` value of a `span` element to the value of the `loc` variable. The URL can now be used to inject malicious client-side code into the page via D-XSS.

Similar techniques are often used to parse parameter values from the URL and update the client UI for applications that make few synchronous requests to the server due to the use of AJAX. In years past, this behavior made it quite simple to set the parameter value to valid HTML content that would be parsed and added to the page, leading to exploitable D-XSS flaws. Exploiting these D-XSS flaws was as easy as injecting a `<script>` HTML element into the parsed parameter's value. Consider the following example code and exploit.

- Code

``` html
Hello
<script>
    var name = document.URL.substring(document.URL.indexOf("name=")+5);
    document.write(name + "!");
</script>
```

- Exploit

```
http://example.com?name=<script>alert(42)</script>
```

- Result

``` html
Hello <script>alert(42)</script>!
```

In the example above, the developer uses JavaScript to retrieve the value of the "name" parameter from the `document.URL` DOM attribute. The developer then writes the parameter value directly to the page as part of a greeting. The "name" parameter and anything appearing after it in the URL can now be used to inject malicious client-side code into the page via D-XSS.

Modern day browsers have begun protecting users and developers from this type of vulnerability by encoding DOM objects that contain input from the client. However, developers still desire the ability to parse DOM objects to create dynamic client-side content. Given the current browser controls, if the parameter value includes anything but valid URL characters, the value is URL encoded, giving developers URL encoded strings to work with rather than unencoded plain text. To compensate, developers decode these values with the `unescape` or `decodeURIComponent` JavaScript functions. By decoding the URL encoded values from the DOM, developers reverse the defenses that browsers have employed and reintroduce the potential for D-XSS. But this is not always the case. Sometimes developers only expect to parse one word strings without URL restricted characters. In this case, decoding is not necessary. This leaves the browsers built-in defenses in place and makes D-XSS nearly impossible to exploit. I say "nearly", because some browsers don't protect applications from D-XSS as well as others. But before we get into that, let's talk about the hash (#) character.

The hash (#) character in a URI denotes the beginning of a URI fragment. According to the RFC 3986, clients are not supposed to send URI fragments to the server, as the client should recognize that they reference a resource secondary to the current, or primary, resource. What does this mean for D-XSS? First, the fragment is stored in the DOM as a part of the `document.location` object, as well as in the `document.location.href` and `document.URL` attributes. If a developer parses either of these elements, the fragment will be included. Depending on how the developer parses the URL to extract parameter values, the use of a hash may have no effect on the parser, allowing an attacker to use a hash to inject the payload into the URL, but prevent the payload from being sent to the server where it may be scrutinized. Below is the same example as before, but the exploit is changed by introducing the hash character.

- Code

``` html
Hello
<script>
    var name = document.URL.substring(document.URL.indexOf("name=")+5);
    document.write(name + "!");
</script>
```

- Exploit

```
http://example.com?name=Tim#<script>alert(42)</script>
```

- Result

``` html
Hello Tim#<script>alert(42)</script>!
```

In this example, the parameter value of `Tim` is still sent to the server, but `Tim#<script>alert(42)</script>` is parsed from the `document.URL` DOM attribute and added to the HTML of the page, exposing the target to the payload. This exploit bypasses any server-side mitigation to D-XSS.

The second impact that the hash character has on D-XSS is that not all browsers treat URIs and URI fragments the same way. I tested Internet Explorer 11, Chrome v33, and Firefox v27 by using the above vulnerable code snippets and the following exploit payload: `?<b>Tim</b>=<b>Tim</b>#<b>Tim</b>` This payload tests for encoding in the parameter name, parameter value, and URI fragment sections of the URL. My testing yielded the following results:

- Internet Explorer 11 does not encode anything.

[![](/static/images/posts/d-xss_ie.png)](/static/images/posts/d-xss_ie.png)

- Chrome v33 does not encode the URI fragment portions of the URL.

[![](/static/images/posts/d-xss_chrome.png)](/static/images/posts/d-xss_chrome.png)

- Firefox v27 encodes everything.

[![](/static/images/posts/d-xss_firefox.png)](/static/images/posts/d-xss_firefox.png)

Therefore, if our target is using Chrome or Internet Explorer, we can use the hash character to inject D-XSS payloads without requiring the developer to decode the injectable parameter value prior to updating the DOM, all while bypassing server-side mitigations.
