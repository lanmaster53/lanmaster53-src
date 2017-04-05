title: 'Proxying thru Virtual Client VPNs'
publish: True
categories: [application security, network security]

So, I'm sorta OCD. Anyone that knows me will attest to that. When it comes to my computing environments, I can't stand clutter. That includes both the external and internal components of my computing environment. One particular point of interest for me is the number of applications installed on my system. I've always felt like limiting the amount of software on my system to only what I needed, and avoiding endless install and uninstall cycles, has resulted in a more stable system. I have no scientific proof to back this up, but it's always worked for me, so I like to keep my system clean and tidy. However, in my line of work, where one-off tools for testing and research abound, this is a daily challenge.

One particular annoyance in my quest to keep a clean and tidy system is VPN. This is because when it comes to remote access into client environments, in the words of Roseanne Rosannadanna, "It's always something." For example, the VPN client software doesn't work on OS X. The VPN requires host checking that isn't compatible with OS X. Every client uses a different VPN solution and software client, resulting in a dozen VPN clients residing on the same system and conflicting with one another. The end result is a delayed engagement and a mess of installed software.

The way I address this issue is by using VMs to create compatible environments where I install everything that is needed for remote access. Easy enough, right? But now we're faced with the problem of having our favorite tools, some of which may be commercial or incompatible with the VM OS, configured and licensed on our host machine. It's one thing to tunnel a VM through a VPN on the host. That's a simple as configuring the VM interface in NAT, or shared mode. Tunneling a host through a VPN on the VM is another challenge altogether, and not as easily solved. Here's a step-by-step for how I approach the problem. Perhaps you'll find it useful in your daily struggles against VPN software clutter.

### Update

##### Tuesday, March 28, 2017

A co-worker and I were struggling through configuring Privoxy on a recent test when it hit me, "Why not use Burp Suite Free as the proxy on the VM?" So I started looking through the Burp Suite Free configuration and discovered some settings that allowed me to replace Privoxy with Burp Suite Free on the VM. There are several advantages to using Burp Suite Free over Privoxy. First, Burp Suite Free is a tool that we are familiar with. Second, Burp Suite Free is easier to install and configure than Privoxy. Finally, Burp Suite Free performs much better than Privoxy. There was a noticeable speed increase when I switched from Privoxy to Burp Suite Free. All this being said, below is a revised guide using Burp Suite Free as the proxy instead of Privoxy.

1. Configure a VM with the required VPN client software and configuration, and validate that it works.
2. Shut down the VM and add a second network adapter to the VM.
3. Configure network adapter 1 (original) as bridged mode.
4. Configure network adapter 2 (new) as host-only mode.
5. Start the VM and install Burp Suite Free. I prefer the installer to the stand-alone jar file, as it seems to be more stable and doesn't require a separate Java install.
6. Configure the VM's Burp proxy to listen on all interfaces.
7. Configure the VM's Burp Proxy to pass through SSL. This is fine, as we're not doing anything here but forwarding the Host OS's traffic to the VPN. We don't want this instance of Burp terminating TLS.
8. Configure the VM's Burp Proxy to not record any traffic. We definitely don't need to waste resources by storing traffic we'll never use.
9. Note the IP address of the host-only interface on the VM.
10. Connect to the VPN on the VM.
11. Configure Burp on the host with the host-only interface as an upstream proxy (IP address from step 9 and port from step 6).
12. Profit. Man I hate it when people say this.

See the [Burp Suite Visual Aids project page](/burp-visual-aids/) for a picture of what this configuration looks like.
