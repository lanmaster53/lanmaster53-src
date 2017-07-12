title: Multi-POST Cross-Site Request Forgery
publish: True
categories: [application security]

A co-worker of mine, [Ethan Robish](https://twitter.com/EthanRobish), and I encountered several complicated CSRF situations for which he came up with a brilliant solution. A solution worthy of recording here for future reference.

<!-- READMORE -->

Let's say you encounter a situation where an attack requires multiple CSRFs in order to conduct some sort of undesirable action i.e. transfer funds between accounts or manipulate a forgot password system. This is easily accomplished if the target accepts GET requests. The attacker can set up a couple of dummy images and launch multiple CSRF requests with ease. However, what if the target application only accepts POST requests? While this complicates things, the attack can still be accomplished as long as the attacker doesn't mind engaging the target user once for each POST request. But what if the attacker has one opportunity to engage the target user? This is the situation that Ethan and I were faced with.

Rather than blindly explain the technique, let's consider the following code that Ethan provides as a template for the attack:

``` html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <script language="javascript">

            window.onload = function() {
                document.getElementById("csrfForm1").submit();
                // to make 2nd form wait for 1st, put the following in a function and use as a callback for a new timer
                document.getElementById("csrfForm2").submit();
            }

            // defeat frame busters
            window.onbeforeunload = function() {
                return "Please click 'Stay on this page' to allow it to finish loading.";
            }

        </script>
    </head>
    <body>

        <form id="csrfForm1" action=<!-- fill in POST URL here --> method="POST" target="csrfIframe1">
            <input type="hidden" name="" value="" />
            <!-- fill in form data here -->
        </form>

        <form id="csrfForm2" action=<!-- fill in POST URL here --> method="POST" target="csrfIframe2">
            <!-- fill in form data here -->
        </form>

        <!-- hidden iframes -->
        <iframe style="display: hidden" height="0" width="0" frameborder="0" name="csrfIframe1"></iframe>
        <iframe style="display: hidden" height="0" width="0" frameborder="0" name="csrfIframe2"></iframe>

    </body>
</html>
```

Let's break it down.

Basically, we need to POST multiple forms. In order to do this without user interaction, we need JavaScript. Nothing new at this point. Where it gets tricky is that upon submitting a form via POST, whether we use JavaScript or a Submit button, the user will be taken to the resulting content. In the case that we need to submit multiple forms, this will prevent any form but the first from submitting. That's a show stopper. The idea here is that we want to use JavaScript to submit all of the forms necessary to carry out the attack without leaving the current page.

In the template code scenario we need to submit two forms to carry out the attack, so we place 2 forms on the page: "csrfForm1" and "csrfForm2". The inputs in the template are blank, but this is where you would put each of the parameters required for the form. Inputs with a type of "hidden" will be most effective. Also, there's no need for a "submit" input type, as we will be using JavaScript to do so.

Next, look at the "head" of the template. We write some JavaScript that will submit both forms upon the page loading with the "onload" event. But wait a second. Didn't we just say that we can't submit two forms on one page? Yes, we did. Take another look in the "body" of the template. You'll notice that there are two iframes at the bottom named "csrfIframe1" and "csrfIframe2". Then look at the forms again and notice that their "target" attributes are set for the respective iframes. This is the trick. By submitting the forms within the target of multiple iframes, we maintain control over the primary page and can continue to submit forms on behalf of the target. Totally cool, right? Also, by sizing the iframe to be invisible, the user continues to see the content of the current page unchanged as the attack plays out.

While this was good enough to solve my problem, Ethan ran into another issue in his situation. His target application had a JavaScript frame busting countermeasure that prevented this attack by hijacking any window that attempted to frame the application. The frame busting JavaScript was similar to this:

``` html
<script type="text/javascript">
if (top != self) {
    top.location = self.location;
}
</script>
```

As the above frame busting JavaScript hijacks the top window, it triggers the top window's "unload" event. Ethan discovered that he could use the "onbeforeunload" event in the top window to ask the user if they wanted to stay on the page. If the user elected to stay, then the unloading of the page would halt, the application would to load in the frame as normal, and the next form would POST. I don't know about you, but when I'm on a page that all the sudden tries to redirect somewhere else, I click the "Stay on this page" button. The result of Ethan's counter-countermeasure is that the attack will ask the user to stay on the page for each form that POSTs through an iframe whose target application is protected by the frame busting JavaScript. As long as the user clicks "Stay on this page", the attack resumes. Pretty handy stuff.

And that, my friends, is how we do multi-POST CSRF at [Black Hills Information Security ](http://www.blackhillsinfosec.com). Enjoy the template and please share your success stories and improvements with us.

### Additional References

This is not the first disclosure of multi-POST CSRF. Below is a list of links to similar articles and tools which assist in executing the above attack. We will continue to update this list as we come across additional resources. Enjoy!

- Articles
    - [Two-stage CSRF attacks](http://ceriksen.com/2012/09/29/two-stage-csrf-attacks/)
- Tools
    - [OWASP CSRFTester Project](https://www.owasp.org/index.php/Category:OWASP_CSRFTester_Project)
