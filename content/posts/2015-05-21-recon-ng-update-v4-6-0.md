title: Recon-ng Update (v4.6.0)
publish: True
categories: [projects, tools, Recon-ng]

Recon-ng v4.6.0 is the largest single framework commit to date. Most of the changes are behind the scenes and won't effect the average user's experience. Below is a summary of the important changes, including the one change that will affect everyone: dependencies.

<!-- READMORE -->

### Dependencies

Starting with Recon-ng v4.6.0, the framework no longer includes dependencies within the code base. Rather, the framework requires users to install dependencies before the dependent modules can be used. I know, I know. I've been quite public about how much I dislike requiring the installation of 3rd party libraries for my tools to function. However, I recently came to the realization that managing the integration of other software packages within my own was a waste of time and effort. Package managers exist for a reason. So I elected to go against my own personal preference and enforce 3rd party dependency installation. For Kali users, this is seamless, as dependencies are installed alongside the framework. For those not using Kali, you'll want to use the Python Package Index (PyPI or PIP) to install the dependencies listed in the REQUIREMENTS file. Follow the guidance on the Recon-ng Wiki [Usage Guide](https://bitbucket.org/LaNMaSteR53/recon-ng/wiki/Usage%20Guide) for installation instructions. I recommend using virtual environments (virtualenv) to install the required packages and prevent clutter in your local Python instance.

All current dependencies are module specific, so the core framework is still completely functional without the dependencies. The framework conducts a module dependency check at runtime and disables the modules that fail to load due to missing dependencies. The framework will provide a warning for each disabled module.

### Module Changes

As always, the update includes lots of module changes. I added threading to several modules, made lots of bug fixes, removed a few defunct modules (jigsaw, breachalarm), and merged a few new modules (unmangle, fullcontact). In addition, all modules were updated to the new module template discussed below.

### Developer Changes

The biggest changes in Recon-ng v4.6.0 are for module developers and include new structures for both the framework's core package and the module template.

The files that make up the framework have been rearranged into a Python package. Therefore, importing API elements is a bit different now. Browse the package structure to get an idea of how to access API elements. As the framework moves forward, internal functionality will be moved into modules that can be imported from logical locations within the package. Several utilities have already been moved. Also, in order to properly handle missing module dependencies, some internal functionality has been abstracted out into mixins. The mixins and utilities are located at "recon/mixins" and "recon/utils" respectively.

The framework now loads all of the modules into memory when the framework launches as opposed to when the user invokes the module. This was originally how the framework behaved, but in a lapse of judgment, the developer perspective was favored over the user's, which led to the poor design choice and current loading system. Loading the modules when the framework launches is slightly slower, but affords the opportunity to capture load errors in modules, disable them, and notify the user of issues before they begin using the framework. With this comes the reintroduction of the "reload" command. The reload command is available in the global context and reloads all of the modules without the developer having to restart the framework.

[Recon-ng Home Page](http://www.recon-ng.com)
