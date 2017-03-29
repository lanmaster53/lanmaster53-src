title: Recon-ng Update (v4.0.0)
publish: True
categories: [projects]

For those that have been following on social media, I have been referencing the "next verson of Recon-ng" for quite some time. I've made claims to new features, new modules, and increased usefullness. All of these promises come to fruition in the release of Recon-ng v4.0.0.

The sweeping changes of this revision come as a result of the revelation that the Metasploit Framework model of data storage and manipulaton dosen't fit well into the reconaissance methodology. Therefore, Recon-ng's approach to reconnaisance has changed, and users will notice that Recon-ng has begun to move away from feel of the Metasploit Framework to a structure and system that better fits the demands of a solid reconnassaince framework. Below is a summary of the changes users can expect to see in the new version of the Recon-ng framework.

### Global Option Changes

One of the first things users will notice is that there are significantly fewer global options in the new version of Recon-ng. This is a result of the global options used as starting points (domain, company, netblock, etc.) being moved into the database. More on this in a moment. Another change that users will notice is the addition of the "STORE\_TABLES" global option. This option sets a flag that tells the framework to store every ASCII table that is created by a framework module to the database. At the time of this update, the only modules that are impacted by this are the jigsaw/purchase\_contact and pwnedlist/domain\_ispwned modules.

### Enhanced Framework Seeding

The most frequent feature request I've received since the release of Recon-ng has been the ability to use more than one domain, company name, netblock or location as starting points or "seeds". In the new version of Recon-ng, the seed information has been moved from the global options to independent tables in the database, allowing for multiples of each seed. This change allows me to introduce a new concept to the framework; that every piece of information stored in the database is a potential input "seed" from which new information can be harvested. This supports Recon-ng's new approach to infromation harvesting; transforming information into other types of information, similar to the approach of Maltego with its "transforms". In addition to the seed information types, other tables have also been added to the database for storing vulnerabilty and port scan information.

Now that users can no longer "set" the seed information as global options, the "add" command has been added to the framework to compensate. The "add" command allows users to add a record to any table in the database without the use of SQL. Users will now use the "add" command to add initial records to the database which will become seed information for the modules.

The "del" command has also been added to the framework to assist with deleting records. The "del" command requires the table name and "ROWID" of a record in the database. In order to facilitate this requirment, the SQLite built-in primary key "ROWID" column has been added to the `show <table>` command output.

### Flexible Input Options

Originally, for this realease of Recon-ng, I wanted the framework to only interact with the database for IO. However, personal preference and the requests of others forced me to develop a system which allows for flexiblity in what modules can use as inputs. Previosuly, some modules had an option named "SOURCE" which allowed users to specify the source information in the form of the database, a single string, a text file, or a custom SQL query. Users will notice that the "SOURCE" option is now present in every module. This is a result of a change in the way modules are developed. Module developers are now required to provide a default SQL query which serves as the default input source for the module. The framework takes that data and dynamically creates the "SOURCE" option allowing the user to also take advantage of the other input options: single string, text file, or custom SQL query.

I've been asked, "Why provide a custom SQL query input option if the database is already the default?" The reason is that there will be times when users have 15 domains in the domains table, but may only want to use 2 of them as input into a module. The custom SQL query source option setting allows the user to set the "SOURCE" option to something like `query select domain from domains where rowid between 1 and 2` which sets the input of the module to the domain column of the first 2 records in the domains table. It must be understood that this advanced usage of the "SOURCE" option requires knowledge of SQL. Additional information has been added to the `show info` command which explains the "SOURCE" options available and displays the default query set by the developer.

### Module Changes

One of the issues with managing an open source project that consists largely of community developed pieces is that the project manager is held responsible for bugs that arrise in the contributed code. When contributors are unresponsive to requests to fix their code, the project manager is held accountable for the bad code and the reputation of the project  and the project manager suffers. There have been many cases where I have received bug reports for modules that I didn't write, don't use, or preceive to have limited value, and I have elected to begin removing these modules from the framework. If I have removed a module that was previously useful, I will consider adding them back in a case-by-case basis or providing the code so that the module can be used locally.

Some new modules have been added with the new version of Recon-ng. The BuiltWith API has added the ability to enumerate contacts for target domains, so the builtwith contacts module was added. A module replicating the hash reversing script PyBozoCrack has also been added to the framework as another means to reverse harvested hashes. The pybozocrack module has been enhanced from the original script to support of any type of hash supported by the Python "hashlib" library.

I mentioned previously that the nature of the framework has changed from collecting information to that of transforming it. This required a restructuring of the module tree to provide visibility into what information is expected as input and what type of information results from each module. Therefore, the recon branch of the module tree now follows the following path structure: `recon/<input table>-<output table>/<module>`. This provides simplicity in determining what module is available for the action the user wants to take next. If the user wants to see all of the modules which accept a domain as input, they can simple search for the input table name "domains" followed by a dash: `search domains-`. If the user wants to see all of the modules which result in harvested hosts, they can simply search for the output table name "hosts" with a preceding dash: `search -hosts`.

Changes to the framework have impacted some module's behavior as well. The HTML reporting module is now much more comprehensive, as all of the data in the database is included in the report: static and dynamically generated tables. Also, modules which result in vulnerability or port infromation, such as the shodan\_net, shodan\_hostname, punkspider and xssed modules, have been modified to add the respective information to the database.

### Other Framework Changes

Several less impactful changes have also been made to Recon-ng. API key data is no longer stored in a JSON file. The JSON file has been replaced with a SQLite database and all of the framework methods have been updated to compensate.

Auto migration has been implemented into the framework. Beginning with this version of Recon-ng, any required migrations will be conducted automatically the first time a workspace is loaded into the new version of the framework. Users should be advised that the new workspaces are not backwards compatible, so it is recommended that users backup workspaces before allowing the migration to take place.

I have received several feature requests to allow for more workspace manipulation from within the framework. Therefore, the "workspace" command has been changed to "workspaces" and a set of subcommands have been added to list, add, select and delete workspaces.

### Data Flow

The changes to Recon-ng require users to understand the new flow of information through the framework. For example, users will want to make sure they have harvested all possible domains before they begin to run modules which use domains as input. Otherwise, repeated runs of modules will be required, exhausting API quotas or requiring complex custom SQL queries to prevent duplicate "SOURCE" inputs. Below is a step-by-step approach developed by using the new version of Recon-ng on several assessments. WARNING: The following example is not 100% complete. Please use it as a guide, not as an official methodology.

- Add known seed information (domains, netblocks, company names, locations, etc.).
- Run modules that leverage known netblocks. This exposes other domains and hosts from which domains can be harvested.
    - `search netblocks-`
- Add new domains gleaned from the results if they have not automatically been added.
- Run modules that conduct DNS brute forcing of TLDs and SLDs against current domains.
- Have list of domains validated by the client.
- Remove out-of-scope domains with the "del" command or generate a query which only selects the scoped domains as input.
- Run modules that conduct DNS brute forcing of hosts against all domains.
- Run host gathering modules. The timeout global option may need to be extended for the ssl\_san, shodan\_*, and vpnhunter modules.
    - `search -hosts`
- Resolve IP addresses.
- Run vhost enumeration modules.
- Run port scan data harvesting modules.
    - `search -ports`
- Use JOIN queries for data analysis.
    - `query select hosts.ip_address, hosts.host, ports.host, ports.port from hosts join ports using (ip_address)`
- Run vulnerability harvesting modules.
    - `search -vulnerabilities`
- Resolve geolocations of harvested hosts.
- Add distinct locations to the db.
    - `query select distinct(latitude || ',' || longitude) as locations from hosts where locations not null`
- Run contact harvesting modules.
    - `search -contacts`
- Mangle contacts into email addresses.
- Run modules that convert email addresses into full contacts.
- Run credential harvesting modules.
    - `search -creds`

### Developer Changes

Many of the changes discussed above impact the way that modules are now developed. Therefore, developers will need to account for developmental changes. Below is quick list of the changes. See the [Development Guide](http://www.recon-ng.com/wiki/Development%20Guide) for more details.

- Sensitive module options such as usernames and passwords have been moved to the API key processing system.
- The module template has been changed to satisfy the default query requirement.
- New methods have been added to support framwork changes: get\_tables, add\_&lt;table&gt;, summarize, debug 
- Methods have been removed: api\_guard

### Conclusion

Be sure to back up the `~/.recon-ng` folder prior to using the new version of the framework, as the migrated workspaces may not be backwards compatible. Also, this is by far the largest revision the framework has undergone to date, so bugs are sure to exist. Please report any bugs to the [issue tracker](http://www.recon-ng.com/issues?status=new&status=open) so that they can be resolved in a timely manner.

If you're interested in contributing to the framework, please see the [issues page](http://www.recon-ng.com/issues?status=new&status=open) for module ideas, feature requests, and bug reports. All contributions are welcome from individuals with any level of Python experience, including no experience. I manage this project not only to provide a tool to the community, but to share my love of coding, mentor developers, and learn from others. Thanks again, and enjoy the framework.

[Recon-ng Home Page](http://www.recon-ng.com)
