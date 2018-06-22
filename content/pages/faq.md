title: FAQ

**As someone who didn't meet the prerequisites going into the class, what are the next steps I should take moving forward from PWAPT?**

PWAPT is definitely not an introductory class with regards to the theory behind the vulnerabilities, so I applaud you for tackling it head on. There are other training courses that can help to solidify those things, but my biggest concern in PWAPT is communicating the methodology and thought process, which doesn't require much of the technical piece to grasp.

To develop skills on the technical side, there are other training courses that focus on vulnerability theory. The Web Application Hackers Handbook is another good resource. Picking something then using Google to research it is what I do when I want to deep dive into a protocol, vulnerability, etc. Reading bug bounties and other people's pentest reports are one of the best ways to learn. Unfortunately, there's no simple way to do it. But if I had to create a checklist, it would look like this.

* Seek training. While this is usually the first step, it can also be a follow on step where advanced training is provided. This is not common though. Most training is designed to cast the widest net, making it basic by nature.
* Read other's reports. This includes assessment reports where possible, and bug bounty write-ups.
* Research the vulnerabilities to gain a theoretical understanding of the issue.
* Implement the vulnerabilities in code to gain a practical understanding of the issue.
* Share your discoveries with others, whether it be blog articles, hosting lunch & learns, speaking at conferences, or providing training of your own.

---

**I heard that you love developing. Did you work as a developer before you got into security, and is that the best approach?**

I have never been a professional developer, but I have been writing code since I was 10. I have avoided developing as a profession because I fear that it will cause me to fall out of love with it. Therefore, no, I've never been a professional developer, nor do I believe it to be a prerequisite. However, understanding code is a key skill in application security, as much of what we do is reverse engineering software.

Being a developer before moving into the security space would give you additional perspective of what development teams face on a daily basis. This will better equip you to provide actionable recommendations that reduce engineering overhead and account for the internal struggles that development teams deal with.

**Did you have to get a Computer Science degree or something related specifically to Cyber Security to experience success? Does not having a degree in the Cyber Security field actually matter when seeking a career there?**

As far as college degree goes, I think there is a general understanding that academia provides little skill in the way of security with respect to the depth we see it in private industry. But it also depends on where you want to land. Upper management and executive level roles have a different set of requirements than a consultant would. From a technical perspective, when I am hiring consultants I prioritize the following things in order:

1. Passion
2. Aptitude
3. Personal Accomplishments
4. Certifications
5. Degrees

---

**I try to take one or two training courses a year. I'm finding that there is a lot of overlap between Web Application Security classes, and rarely do they focus on assessing the security of modern technologies such as Angular and React. Are you aware of any resources for information on testing these types of technologies?**

Unfortunately, there is a serious lack of training content in this area. I do include some aspects of this in PWAPT, probably more than you'll find anywhere else, but not nearly enough to be comprehensive. You've identified a gap that certainly exists. While I don't have a good direct answer to your question, I will share my approach with you.

1. Review the documentation. Most documentation for modern technologies have a security section which outlines some of the known configuration and implementation pitfalls. Check for these first.
2. Research the technology. Even if there isn't a structured resource meant to educate you on testing the technology, there are typically resources available where others have published security research into those technologies. Find these resources and consume them.
3. Check the CVE database. Always check the CVE database for issues in any technology you're assessing, and validate potential vulnerability. This is just too easy once you've fingerprinted the technology.
4. Develop something in the framework. You'll never learn more about a technology from any one resource than you will by using it. Take a crash course on a cheap training site and build an application. If you're going to find anything in the next step, chances are it will start here.
5. Dig in to the code. This one isn't for the faint of heart. Roll up your sleeves, open the code base, and find flaws in the technology yourself. I'll be brutally honest here. In most cases someone smarter than you and me has already scoured the source code for vulnerabilities and the likelihood of us finding something they didn't is slim. But that doesn't mean we won't. This is where doing our due diligence applies.

I know this isn't a great answer, but it's the reality of the situation right now. However, take comfort in knowing you are not alone. If there were a surplus of experts in these technologies, there would probably be more training classes on the topic.

---

**I am currently enrolled in a self-study course to learn more about Python-based web technologies. My intention in pursuing this training is so that I can use these skills for web application testing. However, I'm having a hard time finding companies that use Python in their everyday technology stack. Should I focus elsewhere?**

Almost everyone I know in Cyber Security that stands out from their peers does so largely based on their ability to code. The ability to code makes you more efficient and effective in any technical role, whether be administrative, defensive, or offensive. Coding is not a skill that is unique to Application Security. Whether you're in Exploit Development, Incident Response, Forensics, Network Security, Systems Security, Application Security, whatever, the ability to code will separate you from your peers.

That being said, to answer your question more directly, based on my experience there are two main enterprise technology stacks in use by the majority of the industry right now. Those are C# and Java, and the various flavors and frameworks built on these technologies. Node is catching momentum, but you're right, Python, Ruby, Go, etc. based frameworks aren't nearly as common. When I hire a consultant, I prefer that they have a decent amount of experience in one of the enterprise technologies, and at least dabble in something more trendy. This makes them immediately useful in all types of assessments, while indicating that they have passion to learn other technologies. However, knowing one language, no matter what it is, is all you need to be an effective Penetration Tester. When you're Penetration Testing, most vulnerabilities manifest themselves in similar ways regardless of the technology stack. Therefore, when you're inputing data and analyzing the output (black box testing), whether you reverse the server-side code in your head using the native language or something you know doesn't matter. It's understanding the logic that matters. I am on the fence about adding a requirement to also know a client-side framework. These are just too common to ignore any longer.
