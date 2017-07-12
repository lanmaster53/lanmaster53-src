title: Creating Complex Password Lists with John the Ripper
publish: True
categories: [cracking]

Complex password requirements. Those wonderful things which motivate users to write their passwords on sticky notes and place them under the keyboard, or store them in text files on their desktop. 2 uppercase, 2 lowercase, 2 numbers, 2 special characters, and a minimum length of 10. This is a complex standard used by many organizations as the minimum requirement for user passwords. What's the best way to crack these complex passwords? Brute forcing would be infeasible given a time limit, most word lists are full of patterns which don't meet the criteria, and none of JTR's built-in filters and rule sets are designed to specifically attack complex passwords. That was the discussion that [Mark Baggett](http://twitter.com/markbaggett) of [PaulDotCom](http://www.pauldotcom.com/) and I were having when we decided to write our own JTR filters to build word lists for cracking complex passwords. Props to Korelogic for their kick as "Crack Me If You Can" [password generation rules](https://contest.korelogic.com/rules.txt) which we used as our baseline. Here's how it went.

<!-- READMORE -->

First, Mark pulled a rule out of the Korelogic rule set and began to rebuild it to meet specs. He passed it on to me and I finished the particulars. Below is the resulting filter. We added it to the bottom of our john.conf file.

``` c
[List.External:Filter_Complex]
void filter()
{
    int i, c ;
    int yesCAP;
    int yesLOW;
    int yesNUM;
    int yesSPECIAL;
    int yesMinLen;
    int yesMaxLen;
    int MinLen;
    int MaxLen;

    MinLen = 10;
    MaxLen = 30;

    i = 0;
    yesCAP = 0;
    yesLOW = 0;
    yesNUM = 0;
    yesSPECIAL = 0;
    yesMinLen = 0;
    yesMaxLen = 1;
    while (c = word[i++])
    {
    if (c >= 'A' && c <= 'Z') { yesCAP = yesCAP + 1; }
    else if (c >= 'a' && c <= 'z') { yesLOW = yesLOW + 1; }
    else if (c >= '0' && c <= '9') { yesNUM = yesNUM + 1; }
    else {yesSPECIAL = yesSPECIAL + 1;}
    }
    if (i > MinLen) {yesMinLen = 1;}
    if (i >= MaxLen) {yesMaxLen = 0;}
    if (yesCAP < 2 || yesLOW < 2 || yesNUM < 2 || yesSPECIAL < 2 || yesMinLen==0 || yesMaxLen==0) { word = 0; return;}
}
```

As you can see, the code is easily modified to reflect just about any complex standard. Once we added the filter to the john.conf file, we had to chose a decent sized list to run through the filter. Mark recommended the [rockyou.txt](http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2) list. We ran it through the filter:

``` bash
./john --wordlist=[path to word list] --stdout --external:[filter name] > [path to output list]
```

This gave us all of the passwords in the list which meet the complexity requirements identified within the filter. The list contained 5,641 passwords. Hmmmm... I wonder how many of those users were using the same password to log on to their corporate accounts? This list wasn't comprehensive enough for Mark and I, so we used a [custom rule set written by Matt Weir](http://sites.google.com/site/reusablesec/Home/john-the-ripper-files/john-the-ripper-sample-configs-1/john.conf?attredirects=0&d=1) to expand our list (the custom rule set is labeled 'modified_single' in the linked john.conf):

``` bash
./john --wordlist=[path to NEWLY CREATED word list] --stdout --rules:modified_single --external:[filter name] > [path to output list]
```

This gave us a list of 988,057 passwords. Much better. Time to crack some hashes. But... not so fast. Unfortunately, neither of us currently have legal authority to pentest a network which enforces a complex standard such as this. Therefore, if anyone reading this does, or has a decent set of hashes to run it against, I would be interested to hear about the effectiveness of this technique.

Next up, developing our own custom rule set which will intelligently guess the character patterns of complex passwords.
