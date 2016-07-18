title: 'Method Interchange: The Forgotten Vulnerability'
date: 2015-05-12
categories: [application security]

(Originally posted [@nvisium](https://blog.nvisium.com/2015/05/method-interchange-forgotten.html). Updated on Thursday, May 14, 2015.)

When you think of the most prolific scorers in NBA history, you think of names like Kareem Abdul-Jabbar, Bill Russell, and Karl Malone. Most casual basketball fans aren't familiar with names like Oscar Robertson, Bob Cousy, or John Stockton, but without these men, the previously mentioned scorers would have been much less effective as an offensive threat. And thus is the life of the Method Interchange vulnerability.

I've mentioned Method Interchange in several application security circles recently and have been greeted with strange looks and questions of "Method what?". Once I explained Method Interchange, the reaction changed from "huh?" to, "Oh my, I need to check for that from now on!" Quite simply, Method Interchange is the ability to send parameters via the URI query string or request payload and have them processed by the application regardless of which was originally intended. While seemingly benign, as we'll see later in the article, Method Interchange drastically increases the exploitability of other, more capable, attacks.

### GET and POST Methods

The HTTP protocol specifies two traditional methods for passing parameters from a user-agent to a server. Parameters can be passed as name-value pairs within the URI query string, or as name-value pairs within the payload of the request. When parameters are passed in the URI query string, the request is typically sent using the `GET` method. When parameters are passed within the request payload, the request is typically sent using the `POST` method.

* `GET`

```
GET /resource.ext?name1=value1&name2=value2 HTTP/1.1
Host: www.example.com
```

* `POST`

```
POST /resource.ext HTTP/1.1
Host: www.example.com

name1=value1&name2=value2
```

There are other methods for sending parameters to a server (alternate data formats such as XML and JSON, embedded in the structure of the URI as in RESTful services, other parts of an HTTP request such as custom headers), but here we are referring to the traditional methods provided by the HTTP protocol: `GET` and `POST`.

### Method Interchange Manifested

Server frameworks will either store parameters in global arrays as they parse the request, or have method calls for pulling parameter data from the request object when needed. For example, PHP stores `GET` and `POST` parameters in the `$_GET` and `$_POST` global arrays as it parses each request. The `$_GET` array stores all of the parameters that were sent as part of the URI query string. The `$_POST` array stores all of the parameters that were sent in the request payload. When a developer expects data from the request payload, he uses the `$_POST` array to fetch it. When he expects data from the URI query string, he uses the `$_GET` array. What many security testers forget, or are unaware of, is that PHP, like many frameworks, also has the `$_REQUEST` array, which holds all parameters and values regardless of whether they were sent in the URI query string or as part of the request payload. It is the use of the `$_REQUEST` array and similar implementations that allows for Method Interchange.

Below is an abbreviated list of methods and objects from several popular development frameworks that could allow for Method Interchange. With some of these frameworks, this is only one of multiple ways to introduce Method Interchange. And in some cases, vulnerability requires other conditions to exist.

| Framework | Method/Object | Description |
| :--- | :--- | :--- |
| PHP | `$_REQUEST` | Array that contains `GET`, `POST`, and Cookie values. |
| Rails | `match` | Routing method that allows for routing requests to multiple verbs e.g. `GET`, `POST`, etc. |
| Django | `HttpRequest.REQUEST` | Dictionary that contains both `GET` and `POST` parameter values. |
| Spring MVC | `HttpServletRequest.getParameter()` | Controller method that provides access to both `GET` and `POST` parameter values if the `@RequestMapping` annotation `method` paremeter is not set. |
| .NET MVC | `public ActionResult <action>(<type> <name>)` | Configuration that binds parameters from all sources e.g. `GET`, `POST`, route, etc., to Action method parameters. |

### Discovery

Discovering Method Interchange is incredibly simple. First, identify a request and move the payload from the URI query string to the request payload or vice versa. Keep in mind that `POST` requests require a `Content-Type` header to function properly, so add/remove the necessary headers as needed. While this can be done manually, Burp Suite makes this incredibly easy through the "Change request method" context menu option (thanks [Mike](https://twitter.com/mccabe615)).

[![](/images/posts/method_interchange_burp_1.png)](/images/posts/method_interchange_burp_1.png)

[![](/images/posts/method_interchange_burp_2.png)](/images/posts/method_interchange_burp_2.png)

[![](/images/posts/method_interchange_burp_3.png)](/images/posts/method_interchange_burp_3.png)

Then, fire off the request and analyze the response. If the response mirrors that of the original request, then the application is vulnerable to Method Interchange.

### Exploitation: The Great Assist

So where does the assist analogy fit in to all of this? And so what if parameters can be sent in the URI query string or request payload interchangeably? ... Have you ever tried to conduct a Cross-Site Request Forgery (CSRF) attack that leveraged parameters sent in the request payload? How about a Cross-Site Scripting (XSS) attack? Or how about exploiting a Session Fixation vulnerability where the a session variable was sent in the request payload? If Method Interchange exists, then the CSRF and XSS attacks become much simpler, and Session Fixation vulnerabilities may become exploitable.

Exploiting XSS in a `POST` parameter requires a GET-to-POST script on a 3rd party server, resulting in a suspicious link with which to exploit a user. Exploiting CSRF in a `POST` parameter requires embedding complex JavaScript into a 3rd party application, also resulting in a suspicious link. Method Interchange allows for a simple URL containing a XSS/CSRF payload to appear as a link to a trusted resource. Exploiting Session Fixation may not be possible when a session is sent via a `POST` parameter. Method Interchange allows an attacker to fixate a session via a simple URL that appears as a link to a trusted resource.

### Remediation

Preventing Method Interchange is as simple as discovering it. Use methods, objects, etc. that explicitly provide values from the URI query string (`GET`) and request payload (`POST`). All popular frameworks are capable of preventing Method Interchange. Below are a few resources that address acquiring parameters from requests for an explicitely defined method.

* Rails - [Rails Routing from the Outside In](http://guides.rubyonrails.org/routing.html)
* Django - [Request and Response Objects](https://docs.djangoproject.com/en/1.8/ref/request-response/#django.http.HttpRequest.REQUEST)
* Spring MVC - [Mapping Request Parameters to Handler Method](http://www.codejava.net/frameworks/spring/14-tips-for-writing-spring-mvc-controller#RequestParam)

Parameter binding is the recommended approach for accessing parameter values of an explicitely defined method. However, .NET MVC is only vulnerable to Method Interchange when using parameter binding. Binding parameters in .NET MVC without a `AcceptVerbsAttribute` decorator causes the framework to search all parameter sources (query string, request payload, route data, etc.) for a matching parameter name. .NET MVC is otherwise immune.

* [http://stackoverflow.com/questions/1073692/what-are-the-actionresult-acceptverbsattribute-default-http-methods](http://stackoverflow.com/questions/1073692/what-are-the-actionresult-acceptverbsattribute-default-http-methods)
* [https://bubblogging.wordpress.com/2011/12/31/mvc-data-request-controller/](https://bubblogging.wordpress.com/2011/12/31/mvc-data-request-controller/)

### Conclusion

So as you see, Method Interchange alone is rather harmless. But when combined with other vulnerabilities, Method Interchange provides the needed assist to drastically elevate the risk exposure of the vulnerability.

### Update #1

I've had a few folks reach out with regards to the similarities between HTTP Verb Tampering and Method Interchange. Quite simply, Method Interchange is a subset of Verb Tampering. The difference is that Method Interchange is a result of how an application processes parameters, specifically related to the `GET` and `POST` methods, where Verb Tampering is a result of how the server and application apply access controls around all HTTP methods (verbs). Below is a great whitepaper describing Verb Tampering. It also addresses the concept of Method Interchange.

* [Bypassing VBAAC with HTTP Verb Tampering](http://www.aspectsecurity.com/research-presentations/bypassing-vbaac-with-http-verb-tampering)
