title: 'Proxying thru Virtual Client VPNs'
date: 2016-12-01
categories: [application security, network security]

Random OS crashes got you down? Is Burp inexplicably blowing up and corrupting days of valuable data? If this is you, then you probably have a case of Ihavetoomuchsoftwareinstalledandhaventrefreshedmyosinyears-itis. I kid... mostly.

So, I'm sorta OCD. Anyone that knows me will attest to that. When it comes to my computing environments, I can't stand clutter. That includes both the external and internal components of my computing environment. One particular point of interest for me is the number of applications installed on my system. I've always felt like limiting the amount of software on my system to only what I needed, and avoiding endless install and uninstall cycles, has resulted in a more stable system. I have no scientific proof to back this up, but it's always worked for me, so I like to keep my system clean and tidy. However, in my line of work, where one-off tools for testing and research abound, this is a daily challenge.

One particular annoyance in my quest to keep a clean and tidy system is VPN. This is because when it comes to remote access into client environments, in the words of Roseanne Rosannadanna, "It's always something." For example, the VPN client software doesn't work on OS X. The VPN requires host checking that isn't compatible with OS X. Every client uses a different VPN solution and software client, resulting in a dozen VPN clients residing on the same system and conflicting with one another. The end result is a delayed engagement and a mess of installed software.

The way I address this issue is by using VMs to create compatible environments where I install everything that is needed for remote access. Easy enough, right? But now we're faced with the problem of having our favorite tools, some of which may be commercial or incompatible with the VM OS, configured and licensed on our host machine. It's one thing to tunnel a VM through a VPN on the host. That's a simple as configuring the VM interface in NAT, or shared mode. Tunneling a host through a VPN on the VM is another challenge altogether, and not as easily solved. Here's a step-by-step for how I approach the problem. Perhaps you'll find it useful in your daily struggles against VPN software clutter.

1. Configure a VM with the required VPN client software and configuration, and validate that it works.
2. Shut down the VM and add a second network adapter to the VM.
3. Configure network adapter 1 (original) as bridged mode.
4. Configure network adapter 2 (new) as host-only mode.
5. Start the VM and install a proxy. I use Privoxy. No particular reason why. I think it was on the top of the list when I Googled for standalone Windows proxies. There's probably something better. Suggestions welcome.
6. Configure the proxy to listen on all interfaces.
7. Note the IP address of the host-only interface on the VM.
8. Connect to the VPN on the VM.
9. Configure Burp on host with the host-only interface as an upstream proxy.
10. Profit. Man I hate it when people say this.
