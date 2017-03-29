title: No Nmap, No Permissions, No Problem
publish: True
categories: [network security]

Thanks to the guys at [Command Line Kung Fu](http://blog.commandlinekungfu.com/2010/04/episode-89-lets-scan-us-some-ports.html), I was able to expand on some of their ideas to come up with a pretty neat way to conduct port scanning from a user level command shell without the use of any tools. Here it is:

1. Create files called ports.txt and ips.txt by piping ports and ips into the files on the compromised machine:

    ```
    echo 22>>ports.txt
    ...
    ports.txt:
    22
    80
    443

    echo 192.168.1.1>>ips.txt
    ...
    ips.txt:
    192.168.1.1
    192.168.1.44
    192.168.1.50
    ```

2. Run the following command:

    ```
    for /F "tokens=*" %j in (ips.txt) do @for /F "tokens=*" %i in (ports.txt) do @((echo open %j %i)&(echo quit)) | ftp 2>&1 | find "host" && @echo %i is open on %j >> results.txt
    ```

3. View the results:

    ```
    type results.txt
    results.txt:
    22 is open on 192.168.1.1
    443 is open on 192.168.1.1
    80 is open on 192.168.1.50
    ```

Each open port takes about 30 seconds to complete, and closed ports are instantaneous, but all take a SIGNIFICANT amount of time against a dead host. I would only use this for targeted scanning. Just for known live IP addresses and probing interesting ports. The above method only works on XP, 2003 and Windows 7, not Vista. Vista does not pipe its information to Standard Out or Standard Error, so you can't get to the data to parse it. However, I have come up with a solution. Use the following command:

```
for /F "tokens=*" %j in (ips.txt) do @for /F "tokens=*" %i in (ports.txt) do @echo %j:%i & ((echo open %j %i)&(echo quit)) | ftp
```

Your output will look something like this:

```
192.168.1.1:22
Connection closed by remote host.
192.168.1.1:80
> ftp: connect :Connection refused
192.168.1.1:443
Connection closed by remote host.
192.168.1.50:22
> ftp: connect :Connection refused
192.168.1.50:80
Connection closed by remote host.
192.168.1.50:443
> ftp: connect :Connection refused
```

Any time it says "`Connection closed by remote host.`" that means the port was open and timed out.
