title: 'No-Knowledge API Discovery'
publish: True
categories: [hacking, application security, API, discovery]

I recently received an email from a previous student asking a question about API discovery during a no-knowledge test. The question was, "How can one discover API's across an organization's external IP range when the API's are not linked like URLs and can't be crawled using traditional means?" I thought my answer might be useful for others, so I'm documenting it here.

<!-- READMORE -->

The student's assumption was to use something like Dirbuster or Burp's Content Discovery Engagement Tool to brute force guess API endpoints. But like I'm sure you're thinking right now, that's incredibly tedious and a poor use of time. While I can't say I've ever been asked to do this, here's the approach I would take and the answer I provided to the student.

Start by port scanning of all the available IP addresses and ports that are normally associated with HTTP (80, 8080, 8000, 443, 8443, etc.). Directly browse to each of the resulting services by IP address to determine whether they are dedicated servers or virtually hosted. Dedicated servers will provide access to the hosted application by the IP address alone, while virtually hosted servers will likely display a default web page for the IP address and require the proper `Host` header to be provided in order to reach the virtually hosted application. Use this behavior to determine whether the server is a dedicated server or virtually hosted. A tool that might be useful here is one that will screen shot all of the IP addresses and ports and provide output that allows for quickly viewing all of the available interfaces to determine what they are. For example, [EyeWitness](https://github.com/FortyNorthSecurity/EyeWitness).

For dedicated servers, the next action would depend on what the service provides. If it's a web application, move along unless it's some sort of browser interface for the API itself, which would be the ideal situation. This is actually quite common in modern applications. However, if it's obviously not a web application, and doesn't expose an API interface, then it's most likely an obfuscated service and the next step would be trying to guess the endpoints. Recon may be useful, but there's no easy way forward from here. Time to start brute forcing/guessing.

For virtually hosted servers, reverse DNS lookups on the IP addresses with exposed HTTP services can expose DNS records and provide the proper host names for the virtually hosted applications or APIs. If the IP address exposes any services with a TLS certificate, looking at Subject Alternative Names (SAN) on the certificate may also reveal this information. If a virtually hosted server is successfully discovered, then treat it like a dedicated server (above) to determine what it is hosting.

This about all I can think to do without some sort of inside information about the targets themselves. I hope this is helpful!
