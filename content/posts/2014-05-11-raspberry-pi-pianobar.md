title: Raspberry Pi - Pianobar
publish: True
categories: [automation]

I tweeted a while back that I am using a Raspberry Pi and Pianobar to stream music to my whole-home audio system. I received a lot of requests to publish how I configured my system. At the time I didn't have any organized notes, so I didn't publish anything. However, the Pianobar developer changed some stuff recently that broke my old install, so I had to troubleshoot and rebuild. This time I took good notes and put this article together. The notes below are hastily thrown together and often use links in place of raw data, so if things seem confusing and you have questions, please hit me up on Twitter and I'll see what I can do to help.

I'm more comfortable in Debian environments, so I use Raspbian with my Raspberry Pi. Here are a few resources I used to get mine up and running. Rather than one resource giving me everything I needed to get started, I found bits and pieces from the various resources worked best.

- [http://www.dingleberrypi.com/2013/05/install-and-run-raspbian-from-a-usb-flash-drive/](http://www.dingleberrypi.com/2013/05/install-and-run-raspbian-from-a-usb-flash-drive/)
- [http://elinux.org/RPi\_Easy\_SD\_Card\_Setup](http://elinux.org/RPi\_Easy\_SD\_Card\_Setup)
- [http://xmodulo.com/2013/11/configure-raspberry-pi-first-time.html](http://xmodulo.com/2013/11/configure-raspberry-pi-first-time.html)

With the Raspberry Pi up and running, I updated Raspbian and installed screen. Screen comes in handy during some of the lengthy steps involved with the manual install of Pianobar. Plus, screen is always a good tool to have around when working with a remote terminal.

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install screen
screen
```

I then proceeded to install Pianobar manually using the following steps.

```
# install dependencies
sudo apt-get install git libao-dev libgcrypt11-dev libgnutls-dev libfaad-dev libmad0-dev libjson0-dev make pkg-config
# install FFmpeg manually from source
git clone https://github.com/FFmpeg/FFmpeg.git
cd FFmpeg
./configure
make clean
# 'make' can take several hours
make
sudo make install
cd ..
# install pianobar manually from source
git clone https://github.com/PromyLOPh/pianobar.git
cd pianobar
make clean
make
sudo make install
# configure alsa
sudo nano /usr/share/alsa/alsa.conf
# pcm.front cards.pcm.front => pcm.front cards.pcm.default
```

I used the following resource to configure Pianobar.

- [http://raspberrypiserver.no-ip.org/pianobar\_pandora\_remote\_control.html#install](http://raspberrypiserver.no-ip.org/pianobar\_pandora\_remote\_control.html#install)

Notice the TLS fingerprint directive in the configuration file. For whatever reason, it is critical. If it is not correct, Pianobar will throw TLS errors and will not function. If I encounter TLS errors, the first thing I do is use the following command and check to see if Pandora has changed their TLS signature.

```
openssl s_client -connect tuner.pandora.com:443 < /dev/null 2> /dev/null | openssl x509 -noout -fingerprint | tr -d ':' | cut -d'=' -f2
```

If you didn't already notice, the previous link was actually the walkthrough to configuring the Android client for Pianobar. This is what I use to control Pianobar on my Raspberry Pi, but it isn't required. However, the configuration example still applies, with the exception of the "eventcommand" directive.

The Pianobar remote is only available for Android, so it doesn't work when I want to control music from my Macbook, iPad, or wife's iPhone. Therefore, I use an open source implementation of Airplay called ShairPort to enable Airplay streaming to my Raspberry Pi. Below is a good resource for configuring ShairPort on a Raspberry Pi.

- [http://www.raywenderlich.com/44918/raspberry-pi-airplay-tutorial](http://www.raywenderlich.com/44918/raspberry-pi-airplay-tutorial)

Here is a summary of the commands I used to install ShairPort.

```
sudo apt-get install git libao-dev libssl-dev libcrypt-openssl-rsa-perl libio-socket-inet6-perl libwww-perl avahi-utils libmodule-build-perl
git clone https://github.com/njh/perl-net-sdp.git
cd perl-net-sdp
perl Build.PL
sudo ./Build
sudo ./Build test
sudo ./Build install
cd ..
git clone https://github.com/hendrikw82/shairport.git
cd shairport
make
sudo make install
sudo cp shairport.init.sample /etc/init.d/shairport
cd /etc/init.d
sudo chmod a+x shairport
sudo update-rc.d shairport defaults
sudo nano shairport
#DAEMON_ARGS="-w $PIDFILE -a AirPi"
sudo reboot
```

The Raspberry Pi audio sounded pretty terrible in its default configuration, so I used the `alsamixer` tool to tune the sound. I've found that a setting of 78 sounds really well with my system and allows me to elevate the volume to a reasonably high level before distortion occurs.

Let it be known that Raspberry Pis do not handle power outages well. After countless hours of troubleshooting and rebuilding due to power outage induced corruption, I finally got smart and decided it was time to make an image of a complete install for recovery purposes. Below is the process for doing so on OSX.

```
# gracefully shutdown the RPi
sudo shutdown -h now
# plug the USB drive/SD card into OSX
diskutil list
# note the device ID i.e. /dev/disk2 of the Raspberry Pi media
# using rdisk is preferable (quicker) as its the raw device
sudo dd if=/dev/rdisk2 of=backup.img bs=1m
```

So there you have it. Whew.
