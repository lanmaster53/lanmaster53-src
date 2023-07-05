title: Defeating 802.1x with Marvin
publish: True
categories: [network security]

---

[Mark Baggett](http://www.indepthdefense.com/) of [PaulDotCom](http://www.pauldotcom.com/) and I were asked to conduct an insider pentest of a network using 802.1X for port security. Mark was not able to join me during the initial phases of the test, so I was left with the task of figuring out how to bypass the port security so we could attack local targets. As I began to put my plan together, I came up with the following 802.1X attack vectors:

<!-- READMORE -->

1. Use a hub to sniff traffic on the network. Information gathering.
2. Spoof an authenticated supplicant off the hub. Allows for passing of UDP and ICMP traffic.
3. Write/use a tool which acts as a layer 2 gateway to MitM the authenticated supplicant and ride the 802.1X session.
4. If EAP-MD5 is in use, attempt to crack the captured exchange with [eapmd5cracker.py](https://github.com/lanmaster53/ptscripts/blob/master/eapmd5crack.py) and authenticate to the switch.
    - Allows for passing TCP traffic.

EAP-TLS authentication was in use for the supplicants which were on the segment I wanted access, so vector 3b was not an option at this juncture. Here is what my initial setup looked like:

[![](/static/images/posts/hub.png)](/static/images/posts/hub.png)

Once in this configuration, I was able to execute attack vectors 1 and 2. However, the problem with the above configuration is that neither machine can pass TCP traffic while both are connected. When one of the machines sends out a SYN, both receive the SYN/ACK. The machine not expecting the SYN/ACK will send a RST and kill the connection for the other machine. While I realize that unplugging the authenticated supplicant would allow for successful TCP connections, if the switch is forcing 802.1X re-authentication, connectivity would break during the re-auth process. As Red Teamers, we err on the side of transparency, and don't want to take chances creating unnecessary error log entries. Hence, the need for a tool.

Before dedicating myself to writing a tool to do this, I did some quick research which yielded [this](http://www.gremwell.com/marvin-mitm-tapping-dot1x-links). Marvin. A tool written by abb of [Gremwell](http://www.gremwell.com/) (thanks abb!!) which "diverts and re-injects network connections while preserving the original network addresses, including layer 2." Perfect. My setup for attack vector 3 looked like this:

[![](/static/images/posts/marvin.png)](/static/images/posts/marvin.png)

In order to conduct the attack as passively as possible, I gathered all the necessary configuration information from the network prior to using Marvin. Here's the step-by-step of what I did.

1. Put the sniffer interface in promisc mode.
2. Sniffed the wire using tcpdump.
3. Stored to a pcap file.
4. Analyzed with [NetworkMiner](http://networkminer.sourceforge.net/) (thanks [carnal0wnage](http://carnal0wnage.attackresearch.com/)!!).
5. Determined all layer 3 and layer 2 information about the network gateway and authenticated supplicant.
6. Configured and started Marvin.
7. Connected physical adapters (client first to avoid unknown 802.1X auth log entry).
8. Connected to tap gateway with my attack platform.
9. Hacked away at the internal network.
10. VICTORY!
