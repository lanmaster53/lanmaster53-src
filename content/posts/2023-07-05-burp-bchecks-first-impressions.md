title: 'Burp BChecks: First Impressions'
publish: True
categories: [application security, Burp Suite, consulting, development, tools, training]

---

With the introduction of PortSwigger Burp BChecks, I immediately became curious to see if the feature would be powerful enough to replace the existing Burp integrated Python interface I use to achieve similar results. The Python solution is a topic I cover in great detail in #PBAT (https://www.practisec.com/training/pbat/).

<!-- READMORE -->

I spent some time with Burp BChecks yesterday and set out to do a side-by-side comparison with the Python approach. I quickly discovered that BChecks are so limited that I couldn't conduct a true side-by-side comparison, even with one of the simplest and most common use cases I have for this functionality. Therefore, instead of a side-by-side comparison, I am sharing my initial impressions of BChecks, and will contrast those with the capabilities of the existing Python approach.

The use case for my capabilities analysis was something we do in #PBAT with Python: Create a simple passive scan rule that looks for specific headers that are known to leak useful information, i.e. `X-Powered-By`, `Server`, `X-*`, etc. Here are the takeaways from trying to implement this with BCheck.

1. The BChecks interface is well done. Definitely the best part of the feature. Templates make it easy to get started, and the ability to import/export checks encourages community sourcing and sharing.
2. Debugging BChecks is limited to vague errors about line numbers and character positions and don't provide enough detail of what is causing the error. Fixing bugs and determining limitations took a lot of trial and error because I simply did not know what was wrong with each attempt. I had to try enough variations in all situations to exhaust all possibilities. With this approach, I either stumbled upon a fix at some point, or determined that something simply was not possible. PortSwigger's documentation, while not bad, was not comprehensive enough to help with this.
3. BChecks require learning a proprietary syntax in a field where there is already an abundance of syntax to know. Since it is a proprietary syntax, users are forced to learn something that will not be applicable to anything else in their career.
4. BChecks provide a single looping (iterating) mechanism, `run for each`, that only allows for the use of static, explicitly defined values and does not allow looping through existing arrays. BChecks actually provides arrays of data ( i.e. `response.headers`), but provides no mechanism to loop through them. This is either a gross oversight, or something they surely plan to incorporate in the future. Regardless, it is a crippling gap in functionality at the moment and the main reason why I couldn't do the side-by-side comparison.
5. BChecks do not provide a mechanism for nested loops. Even if it was possible to loop through an existing array, BChecks would only be able to conduct analysis for one static thing for each iteration. For example, it is not possible to check multiple headers for a match with multiple regular expressions or strings. The only way to achieve nested behavior is to create a new BCheck for each item that would normally be in the nested array. Obviously, this is far from ideal, and still doesn't work for anything dynamic because of point 4.
6. BChecks only apply to the scanner, and can't be used with any other tool, i.e. Intruder, Repeater, etc.

Here's how Python in Burp stacks up to the same use case.

1. There is a well designed interface for Python (Python Scripter BApp).
2. Python debugging is verbose and helpful.
3. Python is well known and useful outside of Burp. It's a positive career move and a good investment of one's time to learn Python.
4. Python allows for defining and looping through dynamic arrays.
5. Python allows for nested loops.
6. Burp integrated Python works for every tool in Burp Suite Pro and has limitless scoping capabilities.

These points of comparison are not unique to Python, and this is where I'm going to get on my soapbox. Would it not have been easier for PortSwigger to implement similar behavior with Python, JavaScript, Ruby, etc. than it was to create a new syntax that is full of limitations? More effort for less functionality seems like an odd design choice to me. I'm sure that BChecks will get better over time, but given the above analysis, I'm left to wonder... why? Why didn't PortSwigger embrace what is already being done? Seems to me that the Python solution (or any existing language for that matter) would have been easier to implement (the work is already done for Python) and way more capable than BChecks right out of the box. I'm interested to see how the feature evolves, but I don't see how it will ever be more useful than what already exists with Python. But maybe that's by design.

I must acknowledge the possibility that I could be misunderstanding PortSwigger's intended use case for BChecks, or am missing some key component of the feature. Perhaps I'm trying to use BChecks for something they simply weren't designed to do, although they are explicitly marketed for creating passive scan rules. I made sure to read every resource I could find that PortSwigger had published on BChecks at the time I conducted this analysis, but it's certainly possible that I just missed something.

I will continue watching the progress of the BChecks feature. Even if Python remains my preferred mechanism for achieving this functionality, which it certainly is for now, I will be prepared to share this feature with students in all future PractiSec training courses for which it applies.
