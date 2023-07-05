title: "Official Release: eapmd5crack.py"
publish: True
categories: [cracking, projects, tools]

---

As discussed on [PaulDotCom](http://pauldotcom.com/2011/04/eap-md5-offline-password-attac.html), [eapmd5crack.py](https://github.com/lanmaster53/ptscripts/blob/master/eapmd5crack.py) is a tool developed by myself and [Mark Baggett](http://www.indepthdefense.com/) which will crack an EAP-MD5 authentication exchange from a packet capture.

<!-- READMORE -->

Features:

- Reads from pcap capture file.
- Supports multiple exchanges within capture file.
- Supports Dictionary attacks by accepting standard word lists.
- Supports Brute Force attacks by accepting FIFO file system objects. (see usage)
- Passwords per Second timer.
- Verbosity option.
- Execution halts when password is found.

[![](/static/images/posts/eapmd5screen.png)](/static/images/posts/eapmd5screen.png)

Download [here](https://github.com/lanmaster53/ptscripts/blob/master/eapmd5crack.py).
