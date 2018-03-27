title: Training

[![](/static/images/pages/training/pwapt-teaching.jpg)](/static/images/pages/training/pwapt-teaching.jpg)

## Why Train with Me?

There are too many application security classes that waste time by discussing multiple tools that serve the same purpose, or make application security concepts feel like "magic" by not addressing the practical application of theory. Using the tools I use and the techniques I've learned from years of application security consulting, I provide training that focuses on bringing theory and reality together to provide a true learning experience.

No one wants to hire a consultant without experience, but it's difficult to gain experience unless you already work in the field, or breach ethical boundaries. This is a challenge that many "green" application security professionals face. My training provides real world experience in a classroom environment, allowing for the growth required to enter the work force with confidence and a developed skill set.

Above all, training gives me an opportunity to share my passion for application security with individuals who make a real difference in the state of security for the applications that impact our daily lives. From banks, to social media, to government agencies, the opportunity to support those on the front line of application security is a privilege I don't take for granted.

...but don't take my word for it. Scroll down to see testimonials from previous students.

## Upcoming Classes

| Dates | Class | Host | Location | Registration |
|:---:|:---:|:---:|:---:|:---:|
{% for event in site.events %}
| {{ event.dates }} | {{ event.class }} | {{ event.host }} | {{ event.location }} | [{{ event.link_text }}]({{ event.link_href }}) |
{% endfor %}

Please [contact me](/contact/) for on-site training opportunities.

## Practical Web Application Penetration Testing - PWAPT

### Description

PWAPT provides comprehensive training on the latest open source tools and manual techniques for performing end-to-end web application penetration testing engagements. After a quick overview of the penetration testing methodology, the instructor will lead students through the process of testing and exploiting a target web application using the techniques and approaches developed from a career of real world application penetration testing experiences. Students will be introduced to the best tools currently available for the specific steps of the methodology, including Burp Suite Pro, and taught how to integrate these tools with manual testing techniques to maximize effectiveness. A major goal of this course is teaching students the glue that brings the tools and techniques together to successfully perform a web application penetration test from beginning to end, an oversight in most web application penetration testing courses. The end result is an individual with the confidence and skill set to conduct consultative web application penetration testing engagements.

The majority of the course will be spent performing an instructor led, hands-on web application penetration test against a target application built specifically for this class using a modern technology stack (Python Flask and React) and including real vulnerabilities as encountered in the wild. No old-school vanilla PHP stuff here folks. Students won't be given overly simplistic steps to execute independently. Rather, at each stage of the test, the instructor will present the goals that each testing task is to accomplish and perform the penetration test in front of the class while students do it on their own machine. Primary emphasis of these instructor led exercises will be placed on how to integrate the tools with manual testing procedures to improve the overall work flow. This experience will help students gain the confidence and knowledge necessary to perform web application penetration tests as an application security professional.

PWAPT is a PortSwigger preferred [Burp Suite Training course](https://portswigger.net/training/). PWAPT students will learn basic and advanced usage techniques for Burp Suite Pro, as well as discover obscure functionality hidden within the vast capabilities of the tool. Students will also receive a ~2 week trial license for Burp Suite Pro to use during and after the course.

For additional insight into the origin, mission, and benefits of PWAPT, listen to my interview with [Timothy De Block](https://twitter.com/TimothyDeBlock) for the [Exploring Information Security podcast](http://www.timothydeblock.com/eis/54) on the topic of "What is Practical Web Application Penetration Testing?"

<audio controls>
    <source src="{{ url_for('static', filename='downloads/EIS-ep54-PWAPT.mp3') }}" type="audio/mpeg">
</audio>

### Outline

Day 1:

* Methodology
* Reconnaissance
* Mapping
* Content Discovery
* Vulnerability Discovery

Day 2:

* Vulnerability Discovery (cont.)

Day 3:

* Vulnerability Discovery (cont.)
* Exploitation
* Web Services
* Advanced Burp Usage

Day 4 (optional):

* Remediation

Note: The Conference Edition is an abbreviated version of the course designed to fit into the typical 2-day conference schedule. While not all content can be covered during the Conference Edition courses, all of the content will be provided for self-study.

### Skill Requirements

Students taking this course should have introductory knowledge of the OWASP Top 10. Students do not need to be comfortable with with explaining, finding, or exploiting common web vulnerabilities, but some level of exposure is ideal. This is not an advanced course. However, we will strive to cover advanced topics if the ability level of the student population allows.

This course contains code remediation content that includes discussions on the proper techniques for mitigating vulnerabilities, and exercises where the instructor and students modify the application's source code to implement mitigating controls and test them for effectiveness. While not required, a basic understanding of programming concepts will allow students to better relate to the terminology and techniques demonstrated for properly remediating the discussed vulnerabilities.

### Technical Requirements

* Laptop with at least one (1) USB port.
* Latest VMware Player, VMware Workstation, or VWware Fusion installed. Other virtualization software such as Parallels or VirtualBox will probably work if the attendee is familiar with its functionality. However, VMware Player should be prepared as a backup.
* Ability to disable all security software on their laptop such as Antivirus and/or firewalls (Administrator).
* At least twenty (20) GB of hard drive space.
* At least four (4) GB of RAM.

## Testimonials

{{ site.testimonials|safe }}
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
