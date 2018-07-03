title: FAQ

As someone that openly offers mentorship, I get a lot of emails asking similar questions to which I provide similar replies. These questions range from specifics about PWAPT training to general Information Security career stuff. Rather than continuing to type three page emails, I've decided to consolidate most of the information here for wider dissemination. And who knows, perhaps by placing it here someone will stumble upon and benefit from it.

Also, please keep in mind that much of this is opinion and/or based on personal experience. My experience is bound to differ from others, so please consume this information with that in mind. As always, feedback is welcome.

Thank you, and enjoy.

---

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

---

**Did you have to get a Computer Science degree or something related specifically to Information Security to experience success? Does not having a degree in the Information Security field actually matter when seeking a career there?**

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

Almost everyone I know in Information Security that stands out from their peers does so largely based on their ability to code. The ability to code makes you more efficient and effective in any technical role, whether be administrative, defensive, or offensive. Coding is not a skill that is unique to Application Security. Whether you're in Exploit Development, Incident Response, Forensics, Network Security, Systems Security, Application Security, whatever, the ability to code will separate you from your peers.

That being said, to answer your question more directly, based on my experience there are two main enterprise technology stacks in use by the majority of the industry right now. Those are C# and Java, and the various flavors and frameworks built on these technologies. Node is catching momentum, but you're right, Python, Ruby, Go, etc. based frameworks aren't nearly as common. When I hire a consultant, I prefer that they have a decent amount of experience in one of the enterprise technologies, and at least dabble in something more trendy. This makes them immediately useful in all types of assessments, while indicating that they have passion to learn other technologies. However, knowing one language, no matter what it is, is all you need to be an effective Penetration Tester. When you're Penetration Testing, most vulnerabilities manifest themselves in similar ways regardless of the technology stack. Therefore, when you're inputing data and analyzing the output (black box testing), whether you reverse the server-side code in your head using the native language or something you know doesn't matter. It's understanding the logic that matters. I am on the fence about adding a requirement to also know a client-side framework. These are just too common to ignore any longer.

---

**There are so many things to do in Information Security and I just don't think I can keep up with all of them. What is the expectation and how can I be successful?**

Your assessment of the Information Security field is correct. There are so many things one can do within the industry. As someone looking to work in the industry, you have two options: specialize, or be a jack of all trades, which is an expert of none. If you're going to do anything in this field at a technical level, you need to be an expert. Companies don't want someone in a technical role to be pretty good at everything, but not great at the thing they hired them for. They want someone great at what they were hired for! Since there is way too much to know to be an expert at everything, you have to specialize. It's okay to dabble in everything, but commit the majority of your time becoming an expert at something. What defines a "something"? Let me give you my example. I was pretty good at a lot of things at one point, but an expert at nothing. I decided I loved code more than anything else and wanted to only work with code. That landed me in Application Security. But being an expert in Application Security was even a bit too much to ask for my mediocre brain, so I specialized further in Web Application Security. This put me in a niche where I could become a subject matter expert, and comfortably keep up with the rapidly changing environment.

---

**I'm seeking a college-level internship. I have an opportunity to work on an internal team right now, but want to be a consultant when I graduate. Should I take this internship or keep looking for one at a consulting firm?**

Consulting is a fast-paced, intense business. I'm not going to say that it's the case everywhere, but most interns for consultancies do not get used in a capacity typical of a consultant. The company simply cannot afford to do so. There's too much risk to time lines, backlogs, and quality. As a result, interns end up with busy work or something unrelated to front-line work, and learn very little about consulting or how consulting companies function.

Working for internal teams gives interns the opportunity to see a lot of different parts of the industry i.e. defense, incident handling, forensics, attack, etc. It will also give the intern additional perspective of the challenges companies face when dealing with security issues. This could be invaluable when working as a consultant.

I would lean towards interning on an internal team now in preparation for consulting later. This description may not be indicative of every possible situation regarding Information Security internships, but is something to keep in mind.

---

**What are some good ways to stay involved and informed in the world of Information Security?**

For me, it all comes down to Twitter and conferences. RSS feeds are decent if you've got the right folks in the feed, but it's tough casting a wide enough net this way. I know lots of folks that use Reddit, but I never really figured out how to make it a good source of information. Magazines are way too slow and books are even slower. However, books quite often serve as great on-the-job references and preparatory training material.

The Information Security community has found a way to use Twitter that goes well beyond it's original intent as a social network. As a community, we use it to:

* Share quick thoughts on a topic.
* Conduct full blown discussions on a topic. It's like an online panel where everyone is invited.
* Disclose vulnerabilities.
* Share links to articles, whitepapers, and tools.
* Offer short challenges and puzzles.
* Troll each other with pictures of cats and clever memes.

Even though Twitter (as an Information Security resource) took a decent hit in 2016 due to all of the political drama and trolling, it's still the #1 place to go for up-to-the-minute Information Security information... provided you follow the right people. It's all about who you follow, and who you follow will have a lot to do with which part of Information Security you're interested in. Follow the people that talk about what you're interested in. If you want to be even more efficient, follow people that scour Twitter themselves and retweet what you're interested in. Basically, use other people that spend more time on Twitter than you as a filter. This is probably really bad social network etiquette, but I did say we don't really use it as a "social" network... at least I don't.

Conferences are great too, but probably not for why you think they are. To me, conferences aren't about the presented material anymore. Most conferences are recorded these days, and all the talks can be watched later. Lobbycon is where it's at. Lobbycon is just hanging out in the Lobby of the venue where the conference is being hosted. Lobbycon is invaluable with regards to networking, sharing ideas, and discussing topics. I've walked away from Lobbycon with so many great ideas over the years. Heck, I know people that won't go to a conference, but will pay travel costs just get a room in the same hotel as the conference and do Lobbycon. It really is a great resource. All that being said, watch the talks. Whether you do it in person or on video, there is so much good information being shared this way, and you don't want to miss it. I'll usually go through the conference booklet on the first day and mark all of the talks I want to see. If I get tired of gabbing, or have some free time, I'll go see one of them in person. Otherwise, I'll keep my booklet around and watch them on video later.

---

**There are so many Information Security conferences these days. What conferences do you recommend?**

Without a doubt, DerbyCon. Then, any BSides. DerbyCon is great for so many reasons, but the main reason I prefer it is because it's a community event with a family atmosphere, and not a culture. Honestly, I'm not a fan of the hacker culture and don't identify with it at all. You won't see me at DEF CON for that very reason. However, it can be tough to get a ticket to DerbyCon (see my [article](/2017/08/26/cooling-down-the-hottest-ticket-in-town/) on the topic if you agree, missed out, and are still looking for a ticket), and it requires travel. The thing about BSides is they are all over the place, are pretty consistent in terms of quality, and getting tickets is easy. On any given year, I attend DerbyCon, BSides Greenville, and BSides Augusta at a minimum. I will say that I thoroughly enjoyed Wild West Hackin' Fest last year in South Dakota. It had some of the best Lobbycon ever. Since it was in the middle of nowhere, and there was nothing else for anyone to do, everyone congregated at the same bar and restaurant every night.

---

**I keep hearing people in Information Security refer to something called a personal brand. What exactly is a personal brand, and how does it apply to me as an Information Security professional?**

As you saw in my list of priorities for hiring people (above), the first tangible item is personal accomplishments, above both certifications and degrees. Status in the Information Security industry relies heavily on notoriety. This is true for the black hat side of things as well as the white hat side. Notoriety comes when you've publicly accomplished something, whether in a positive or negative fashion. The collection of your public accomplishments and how you relate to others in the industry becomes your personal brand. Whether seeking a job or starting a company, success will have little to do with your traditional credentials and everything to do with your personal brand. A good enough personal brand will take you beyond the need to apply for a job or submit a resume. Companies will come looking for you. There is simply too much work and not enough good people to do it. If your personal brand is known for expertise in something, the job offers will come.

---

**How does the dynamic of a personal brand work when employed by a company, which has its own independent brand?**

Because of the nature of how you develop a personal brand, personal brands and company brands thrive in a synergistic symbiotic cyber relationship (three in a row, bingo!). When you speak in front of a group, you're wearing the company's logo. When you teach a workshop or write an article, you're referring to experiences gained at the company. As long as your ethics and efforts are in line with the company's, your personal brand will boost the company's brand. This make you a more valuable asset to the company, resulting in the company providing more opportunities for you to grow your personal brand. It's a beautiful thing to see companies embrace this. The results are a better security team and culture for the company, and a major brand boost when the security team itself becomes known as a contributor to the community.

---

**How do you build a personal brand?**

Basically, by being outspoken and not being selfish. Share your discoveries with others, whether it be blog articles, hosting lunch & learns, speaking at conferences, or providing training. Share your creations with others by open sourcing your scripts and tools that you use to make your own job easier. While these things may be differentiators at times, remember that there is more work than there are skilled people. Don't be greedy. I've seen people throw away personal brand growth opportunities while trying to make a quick buck. Don't underestimate the value of giving stuff (ideas, software, techniques, etc.) away. It may make you more in the long run giving it away than it would in a short term money grab. Open sourcing Recon-ng has done more for my career than I can quantify, yet there were people in the beginning that told me I was crazy for giving it away. I'm glad I didn't listen.
