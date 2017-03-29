title: Public Facing LDAP Enumeration
publish: True
categories: [network security]

This article is more for future reference than anything else, but here's the deal. While doing an assessment, I encountered a public facing LDAP server. Not a huge deal, except that this LDAP server allowed empty base objects and NULL BINDs. Basically, this means that any anonymous Internet user could extract information from the LDAP server. This LDAP server was also tied directly into the internal Windows Active Directory infrastructure. Oops.

I tried a bunch of tools to assist me in enumerating information from the server. LdapMiner, LDAP Explorer, ldapsearch, and JXplorer to name a few. The only tool that properly leveraged the empty base object and NULL BIND vulnerabilities to produce useful results was [JXplorer](http://jxplorer.org/).

The LDAP server administrator did do one thing right. He limited the responses to all LDAP queries to 25 results. Whether or not it was intentional, I don't know, but it made it painful to extract large chunks of data. Basically, it forced attackers to use many alphabetical queries with wildcards to enumerate all entries, much like exploiting a blind SQL Injection vulnerability.

``` bash
ldapsearch -h <ldap_host> -p 389 -x -b "O=<known_dn>" "cn=aa*"
ldapsearch -h <ldap_host> -p 389 -x -b "O=<known_dn>" "cn=ab*"
ldapsearch -h <ldap_host> -p 389 -x -b "O=<known_dn>" "cn=ac*"
ldapsearch -h <ldap_host> -p 389 -x -b "O=<known_dn>" "cn=ad*"
```

Not even JXplorer could do this, and was restricted to extracting only the first 25 nodes in each identified node throughout the directory tree. The thing that set JXplorer apart was that while some of the other tools pulled the first 25 nodes from the directory using the empty base object and NULL BIND, JXplorer crawled the tree and continued to pull the first 25 nodes from each of the child nodes it discovered. This was a good start, but I would have liked to dump the entire directory, and getting data in a useful form was cumbersome. I didn't have time to write a tool (on my list of things to do), so instead of dumping the directory, I used the empty base object and NULL BIND vulnerabilities to validate email addresses harvested with Recon-ng. Here are the commands I used to do that using the ldapsearch utility.

Verify single email address:

``` bash
ldapsearch -h <ldap_host> -p 389 -x -b "O=<known_dn>" "mail=<email_address>"
```

Verify list of email addresses:

``` bash
for line in $(cat list.txt); do ldapsearch -h <ldap_host> -p 389 -x -b "O=<known_dn>" "mail=$line" | grep mail: | cut -d" " -f2; done
```

The danger of an Internet facing LDAP server configured like this should be fairly obvious. Spammers and attackers have access to the full name and email address of every person in your environment that has an account in Active Directory. This will drastically increase the amount of spam your organization receives and the likelihood of phishing attacks. In addition, if you have web facing VPNs or web applications, you are giving attackers part of what is required to authenticate. This is a very bad idea.
