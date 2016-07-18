title: 'Validating Redirects with Hyperlinks'
date: 2015-12-02
categories: [application security]

I came across an application recently that contained an Unvalidated Redirect flaw. The flaw was pretty basic. The login page accepted a `next` parameter and blindly redirected to the value of the parameter without validating whether or not the value represented a trusted destination. The redirect occurred in client-side logic without the parameter ever hitting the server. My recommendation to the client included a pretty basic JavaScript validation filter, and they quickly implemented a fix and sent the code back for me to validate if the flaw had been remediated. In looking at the code, I realized that they had not implemented my recommended code, but did something that I had not seen before and thought was quite novel. Hence, why I am writing this.

The remediated redirect logic contained a call to a function that consumed the value of the `next` parameter and the hostname of the current location.

```
document.location = validate(next, document.location.hostname)
```

Pretty standard stuff. The interesting bit was in the called function.

```
function validate(n, c) { var r = document.createElement("a"); return r.href = n, r.hostname === c ? n : "/"; }
```

Which can be simplified to...

```
function validate(n, c) { var r = document.createElement("a"); r.href = n; return r.hostname === c ? n : "/"; }
```

Which can be further simplified to...

```
function validate(n, c) { var r = document.createElement("a"); r.href = n; if(r.hostname === c) { return r.href; } else { return "/" ; }}
```

I am including several versions of the same code because the first version can be quite confusing to folks that aren't familiar with the [Comma](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_Operator) operator.

Just in case you haven't picked up on it yet, let's look at exactly what is going on here. I am using the Chrome Developer Tools JavaScript console on the [nVisium](https://nvisium.com) web page to demonstrate this if you want to follow along. Paste one of the functions above into the console and assign a value to a variable called `next`.

```
var next = "http://lanmaster53.com"
```

Now let's follow the logic of the first simplified version of the `validate` function to see how this works. The function first creates a hyperlink tag. Don't type the following into the console. I'll let you know when we're ready to continue with the demonstration.

```
var r = document.createElement("a")
```

Hyperlink tags accept an attribute called `href` that determines the destination of the browser when the hyperlink is clicked. The function then sets the `href` attribute of the dynamically created hyperlink to the value of the `next` parameter.

```
r.href = n
```

This is where it gets interesting. Like the `document` object itself, the hyperlink tag object has a `hostname` property. Once the hyperlink's `href` attribute has a value, the `hostname` property will contain a nicely parsed hostname for the assigned `href`. What the function is essentially doing is using the browser's builtin parser to break apart URLs in a consistent manner. Pretty cool, right?

All that's left for the function to do is compare the hostname of the document (provided to the function) and the hostname derived from the dynamically created hyperlink to determine whether the value of the `next` parameter is a safe location, in this case local to the application.

```
return r.hostname === c ? n : "/"
```

This is a [Ternary](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) operator that accepts a conditional expression that evaluates to `true` or `false` and returns one of two expressions based on the result. In this case, the function returns the value of the `next` parameter if the hostnames match, or the root of the web site if they do not, effectively restricting all redirects to locations local to the application.

Let's test the validation function with our values. Enter the following into the console to continue the demonstration.

```
validate(next, document.location.hostname)
```

The function should have returned `/`, which, when assigned to `document.location` would redirect the browser to the root of the website. Now change the value of `next` to something local and test.

```
var next = "https://nvisium.com/blog"
validate(next, document.location.hostname)
```

The function should have returned the value of `next`.

Using the browser's builtin parser to break apart URLs is pretty darn cool if you ask me. And you aren't limited to the hostname. Hyperlinks also have the `origin` property if you want to restrict URLs based on similar restrictions enforced by Same-Origin Policy. In any case, I thought this was worth sharing.
