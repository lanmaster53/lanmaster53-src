title: Training

[![](/static/images/pages/training/pwapt-teaching.jpg)](/static/images/pages/training/pwapt-teaching.jpg)

## Why Train with Practical Security Services?

There are too many Web Application Security testing and secure development classes that waste time by discussing multiple tools that serve the same purpose, or make Web Application Security concepts feel like "magic" by not addressing the practical application of theory. Using the tools they use and the techniques they've learned from years of Web Application Security consulting and software development, Practical Security Services provides training that focuses on bringing theory and reality together to provide a true learning experience. Training also gives Practical Security Services an opportunity to share a passion for Web Application Security and software development with individuals who make a real difference in the state of security for the applications that impact our daily lives. From banks, to social media, to government agencies, the opportunity to support those on the front line of Web Application Security is a privilege Practical Security Services does not take for granted.

...but don't take our word for it. Read the [testimonials](/testimonials/) from previous students.

[Upcoming Classes](#upcoming-classes) |
[Training Options](#training-options) |
[PWAPT](#pwapt) |
[PBAT](#pbat) |
[PWAS](#pwas)

---

## <a name="upcoming-classes"></a> Upcoming Classes

{% if site.events %}
| Dates | Class | Host | Location | Registration |
|:---:|:---:|:---:|:---:|:---:|
{% for name, event in site.events.items() %}
| {{ event.date }} | {{ event.class }} | {{ event.host }} | {{ event.location }} | [{{ event.link_text }}]({{ event.link_href }}) |
{% endfor %}
{% else %}
No future classes scheduled at this time.
{% endif %}

Please [contact us](/contact/) for on-site training opportunities.

## <a name="training-options"></a> Training Options

### Open Enrollment

Practical Security Services schedules open enrollment classes all over the world. While historically open enrollment classes have only taken place in the United States, Practical Security Services is willing an able to travel abroad. Open enrollment classes are made available through several arrangements:

* Hosted by Practical Security Services directly.
* Hosted by Practical Security Services in association with a host company.
* Provided through partnerships with conferences and events.

Pricing for open enrollment classes hosted by Practical Security Services use the same pricing model as on-site training (see the "On-Site" section for details) with the exception of the inclusion of travel. However, prices may vary when training is provided through partnerships where the partner controls the pricing, or when travel costs are excessive (i.e. major city centers or international). These changes would be reflected in the individual ticket prices. For classes hosted by Practical Security Services, there is also a minimum class size of 12 students if not otherwise noted on the event page.

For companies looking to host an open enrollment class, Practical Security Services manages all of the financial logistics and the host company is only responsible for providing the training space, so there is minimal overhead for the host company. Practical Security Services also provides incentives to the host company. Please [contact us](/contact/) for details.

### On-Site

Practical Security Services charges a flat rate per person per day for on-site training, regardless of the course. Rate may vary based on location, travel duration, etc. There is also a minimum on-site class size of 10 students. Travel is billed as actual for on-site classes in addition to the class rate. If you are unable to meet the minimum class size, there is the option to pay the equivalent fee of 10 students, or host an open enrollment class and allow outsiders to register in order to meet the minimum (see the "Open Enrollment" section for details).

## Courses

---

### <a name="pbat"></a> Practical Burp Suite Pro: Advanced Tactics - PBAT

> All Burp, all the time.

#### Description

Do you feel pretty good about your Web Application Security testing methodology, but think you might be able to get more out of your tools? Years of experience providing instruction on the process of conducting Web Application Security assessments has made it clear. Even the most experienced testers lack a complete understanding of everything that is available in the industry’s #1 Web Application Security testing tool: PortSwigger’s Burp Suite Pro. It’s time to fix that with PBAT.

PBAT provides comprehensive training on the capabilities of Burp Suite Pro and the practical application of these capabilities in real world web application penetration testing engagements. The instructor will introduce the various components of Burp Suite Pro, discussing their purpose, strengths, and limitations, and lead students in realistic scenario driven hands-on exercises leveraging the components against a modern web application. As the scenarios unfold, the instructor will share tips and tricks for using Burp Suite Pro gained from years of personal usage experience and extensive research into the tool's capabilities and ongoing expansion. These scenarios include the use of lesser-known features hidden within the Burp interface, and the modification and chaining of features to solve complex problems that make testing modern applications a challenge.

As a Portswigger Preferred Burp Suite Pro Trainer, Tim is a trusted source for comprehensive training on Burp Suite Pro v2.0. Since v2.0 was announced in August 2018, Tim has been the leader in researching and identifying the differences between the old and new versions of Burp Suite Pro, and assisting Web Application Security professionals in the transition.

<!---
#### Outline
-->

#### Skill Requirements

PBAT is 100% focused on Burp Suite Pro v2.0 and does not address the methodology and process of web application penetration testing or specific vulnerabilities. However, the class is taught within the context of a web application penetration test in order to provide realistic scenarios for the tool’s usage. While not an official continuation of Practical Web Application Penetration Testing (PWAPT), PBAT is a great follow-up for students who have previously attended PWAPT.

#### Technical Requirements

* Laptop with the latest VMware Player, VMware Workstation, or VWware Fusion installed. Other virtualization software such as Parallels or VirtualBox will probably work if the attendee is familiar with its functionality. However, VMware Player should be prepared as a backup.
* Ability to disable all security software on their laptop such as Antivirus and/or firewalls (Administrator).
* At least twenty (20) GB of hard drive space.
* At least four (4) GB of RAM.

---

### <a name="pwapt"></a> Practical Web Application Penetration Testing - PWAPT

> Real world Web Application Security testing experience in a classroom environment.

#### Description

No one wants to hire a Web Application Security consultant without experience, but it's difficult to gain experience unless you already work in the field or breach ethical boundaries. This is a challenge that many "green" Web Application Security professionals face. Born out of this need, Practical Security Services designed PWAPT to provide real world experience in a classroom environment, allowing for the growth required to enter the work force with confidence and competence. PWAPT was also designed to provide experienced Web Application Security consultants with a better defined testing methodology complimented by obscure vulnerability discovery techniques and "quality of life" tips and tricks to improve on a developed skill set. Regardless of skill level, PWAPT has something for everyone.

PWAPT provides comprehensive training on the latest open source tools and manual techniques for performing end-to-end web application penetration testing engagements. After a quick overview of the penetration testing methodology, the instructor will lead students through the process of testing and exploiting a target web application using the techniques and approaches developed from a career of real world application penetration testing experiences. Students will be introduced to the best tools currently available for the specific steps of the methodology, including Burp Suite Pro, and taught how to integrate these tools with manual testing techniques to maximize effectiveness. A major goal of this course is teaching students the glue that brings the tools and techniques together to successfully perform a web application penetration test from beginning to end, an oversight in most web application penetration testing courses. The end result is an individual with the confidence and skill set to conduct consultative web application penetration testing engagements.

The majority of the course will be spent performing an instructor led, hands-on web application penetration test against a target application built specifically for this class using a modern technology stack and including real vulnerabilities as encountered in the wild. No old-school vanilla PHP stuff here folks. Students won't be given overly simplistic steps to execute independently. Rather, at each stage of the test, the instructor will present the goals that each testing task is to accomplish and perform the penetration test in front of the class while students do it on their own machine. Primary emphasis of these instructor led exercises will be placed on how to integrate the tools with manual testing procedures to improve the overall work flow. This experience will help students gain the confidence and knowledge necessary to perform web application penetration tests as a Web Application Security professional.

PWAPT is a PortSwigger preferred [Burp Suite Training course](https://portswigger.net/training/). PWAPT students will learn basic and advanced usage techniques for Burp Suite Pro, as well as discover obscure functionality hidden within the vast capabilities of the tool. Students will also receive a trial license for Burp Suite Pro to use during and after the course.

For additional insight into the origin, mission, and benefits of PWAPT, listen to our interview with [Timothy De Block](https://twitter.com/TimothyDeBlock) for the [Exploring Information Security podcast](http://www.timothydeblock.com/eis/54) on the topic of "What is Practical Web Application Penetration Testing?" The course has developed significantly since the interview, but the discussed principles behind the development of the course remain the same.

<audio controls>
    <source src="{{ url_for('static', filename='downloads/EIS-ep54-PWAPT.mp3') }}" type="audio/mpeg">
</audio>

#### Outline

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

Note: The three day offering requires a minimum of 24 hours of classroom time in order to get through the core content. Be prepared for three full days of training with the potential for overtime in the evenings.

#### Skill Requirements

Students taking this course should have introductory knowledge of the OWASP Top 10 and a thorough understanding of the HTTP protocol. Students do not need to be comfortable finding or exploiting common web vulnerabilities, but a general understanding is ideal. However, understanding the HTTP protocol is vital. PWAPT does not cover basic HTTP, but will reference it repeatedly assuming students are familiar with the protocol. PWAPT may also do this with some vulnerabilities, but will discuss them in further detail at a later time during the class.

Knowledge of web technologies and programming constructs will also be helpful, but are not required. PWAPT uses code to explain and demonstrate some vulnerabilities, and in the 4-day format contains exercises where the instructor and students modify the application's source code to implement mitigating controls.

While this is not an advanced course, PWAPT will strive to cover advanced topics if the ability level of the student population allows. Please prepare yourselves for the above requirements if you do not already meet them coming into the course. Anyone looking to get into Web Application Security or hone their craft should be working on their software development skills. If not already doing so, this is a good time to get started.

#### Technical Requirements

* Latest VMware Player, VMware Workstation, or VWware Fusion installed. Other virtualization software such as Parallels or VirtualBox will probably work if the attendee is familiar with its functionality. However, VMware Player should be prepared as a backup.
* Ability to disable all security software on their laptop such as Antivirus and/or firewalls (Administrator).
* At least twenty (20) GB of hard drive space.
* At least four (4) GB of RAM.

---

### <a name="pwas"></a> Practical Web Application Security - PWAS

> Fully customized Web Application Security training.

#### Description

No single Web Application Security training class fits every need, and developing and managing custom training courses is a difficult task often resulting in additional expense for you, the purchaser. It doesn't have to be that way. Practical Security Services has developed a proprietary content management and presentation platform that quickly and effortlessly builds custom training courses based on client specified needs, removing the overhead and expense associated with providing customized training. This saves you money and results in a consistent high-quality product.

Clients choose from a menu of 150+ Web Application Security modules and our system creates a training deck and associated booklet with the push of a button. Available training modules include content related to vulnerability theory, remediation techniques, secure development, testing methodology (dynamic, static and hybrid), hands-on exercises and labs, tooling, web-based protocols, etc. New modules can also be created upon request. Once a course is built, it is delivered as a blend of lecture and lab exercises that the students and instructor will do together so that the students can see, feel, and think what the instructor has learned through years of software development and Web Application Security consulting.

With this kind of interactive, fully customized, framework agnostic, Web Application Security training, clients can provide their developers, quality assurance personnel, and security engineers with the in-depth knowledge of web-based software vulnerabilities required to meet Web Application Security objectives. Please [contact us](/contact/) to begin the discussion on how customized training can meet your Web Application Security training needs.
