title: 'Cooling Down the Hottest Ticket in Town'
publish: True
categories: [miscellaneous, hacking]

---

We had an interesting conversation on the Proverbs Hackers mailing list today about getting tickets for popular conferences that have limited ticket sales. Security conferences most often thought of in this category are DerbyCon and ShmooCon. For anyone that has tried to get tickets to one of these conferences in the traditional fashion, you know the struggle is real. The conversation got me thinking about ways you can acquire a ticket that you may not realize are available. Below is the result of that thought exercise.

<!-- READMORE -->

1. Automate it. If you do go the traditional route, every second counts. Never more so than with DerbyCon, which has traditionally opened up ticket sales early. There was a lot of dialog on that this year as they sold out before they were actually supposed to go on sale. For conferences like DerbyCon, racing for a ticket upon release is the worst way to try and get a ticket. But if you insist, set up a `curl` or `wget` based heart beat script for the registration page and have it running 30 minutes before the scheduled start. This should give you the best chance of being one of the first to know when sales actually start. My wife and I did this for her Walker Stalker tickets this year and it worked great. Here's a one-liner to get you started: `while :; do ping -c 3 127.0.0.1 2>&1 >/dev/null; curl -s {purchase url} | grep "{text unique to pre-sale condition}" || say "go go go"; done`
2. Submit to the conference CFP. This has always been my approach. Places like ShmooCon have traditionally provided opportunities to buy tickets for every CFP submission. The system can be "gamed" a bit, but there is also always a chance that your CFP gets accepted, so be prepared to speak if you go this route.
3. Buy second hand. This has traditionally been the best way to get a ticket for these conferences. I usually just keep an eye on Twitter. Especially, the day the conference sends CFP acceptance letters. This is the day that the accepted folks off-load the ticket they bought as a back up plan.
4. Pay an accepted speaker their honorarium in exchange for the extra ticket they get offered. Many conferences offer an honorarium OR a second free ticket to the conference for accepted CFP submissions. Get in touch with someone whose CFP submission was accepted and offer to pay their honorarium in exchange for a ticket. Then, they can choose the extra ticket over the honorarium as their "gift" and sell it to you on site. This might cost a little more, as honorariums are typically more than the ticket price, but usually not by much.
5. Go to training. Most conferences include access to the seminars with a training ticket. This is the most expensive way, but you get the most too.

So, perhaps this will open a door for someone that really wants to get a ticket to a conference, but thought they were out of options. If you happen to use one of these techniques and it works, I'd love to hear your success story. Good luck, and happy hunting. It's officially conference season.
