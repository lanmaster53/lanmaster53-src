title: 'XSS Active Defense'
publish: True
categories: [application security, hacking, projects]

While I don't do active defense in any part of my professional life, I enjoy developing active defense techniques for web technologies. Lately I've been dabbling in active defense mechanisms for Cross-Site Scripting (XSS) attacks, and as the developer of the HoneyBadger geolocation framework, incorporating the research into new reporting techniques and agents.

<!-- READMORE -->

First, the basics. XSS is a client-side code injection issue where the goal is to inject client-side code in such a way that a malicious payload executes in the JavaScript context, regardless of where the payload lands in the page. The bottom line is that the final attack executes as JavaScript. When attempting to discover XSS flaws, an attacker is always going to develop proof-of-concept payloads to validate the issue prior final exploitation. This is a universal methodology. The first active defense technique I want to share preys on this universal behavior.

The most common proof-of-concept payload used during the discovery process is typically some variation of the `alert` JavaScript function, regardless of the context. I understand that there are many options with which to conduct a proof-of-concept attack, but this technique applies to all of them and for this demonstration we're going to use `alert`. Like many other programming/scripting languages like it, we have the ability to overwrite functions in JavaScript. If we know that an attacker is going to use the `alert` function to create a proof-of-concept while validating XSS on a target application, then the `alert` function itself becomes an opportunity for detection and action when we apply what we know about JavaScript. Take the following block of code:

```js
var _alert = window.alert;
window.alert = function(msg) {
    // report malicious behavior
    _alert(msg);
}
```

This code saves the original `alert` function as `_alert`. The code then creates a new `alert` function. The new `alert` function does anything we want whenever the browser calls it, and then initiates the original behavior by calling `_alert`. Since the `alert` function usually indicates malicious behavior, this gives us an opportunity to detect an attack, and in the case of active defense, respond with some action of our own. Let's expand on the above code to do something interesting.

```js
var _alert = window.alert;
window.alert = function(msg) {
    img = new Image();
    img.src = "https://<honeybadger host>/api/beacon/<target guid>/HTML";
    _alert(msg);
}
```

The added code is a HoneyBadger HTML agent using a JavaScript image object. The cool thing about creating an image this way is that browsers immediately fire off the request for the `src` as soon as it is set, and the image never has to be added to the DOM. This means there is no visual evidence of attack in the user interface. As it stands right now, there are a variety of agents that we could place in our fake `alert` function, i.e. HTML, JavaScript (HTML5), Java Applet, etc., but you can literally do anything you'd like. Pretty cool, right?

Beyond overwriting the `alert` function, there are a few other XSS specific HoneyBadger agents that I've come up with recently: Content-Security-Policy and XSS-Protection. Both of these agents incorporate reporting functionality for debugging issues during the implementation process. However, defenders can use the reporting functionality built into these mechanisms to report back to say... a HoneyBadger server.

The Content-Security-Policy agent reports upon any violation of the configured policy, which when done correctly indicates the introduction of arbitrary client-side code. Incorporating either of these agents into a web page requires the ability to set headers for the page's response. The following headers create the Content-Security-Policy agent:

```
X-XSS-Protection: 0
Content-Security-Policy-Report-Only: <policy>; report-uri https://<honeybadger host>/api/beacon/<target guid>/Content-Security-Policy

```

The `X-XSS-Protection` header disables the browser-side XSS protection before the Content Security Policy is configured. This is because browser-side XSS protection will trigger before the Content Security Policy and prevent the agent from working.

The XSS-Protection agent reports any time the built-in browser XSS protection mechanism triggers, which indicates the presence of a known XSS attack. The following header creates the XSS-Protection agent:

```
X-XSS-Protection: 1; report=https://<honeybadger host>/api/beacon/<target guid>/XSS-Protection

```

These agents cannot be used together. Using them together will only allow the XSS-Protection agent to trigger, as described above. I recommend the Content-Security-Policy agent for any environment that already has it implemented, and the XSS-Protection agent for those that don't. However, be mindful that the headers these agents use are only supported by some browsers. To see the Content-Security-Policy agent in action, check out a target demo page on any deployed HoneyBadger instance.
