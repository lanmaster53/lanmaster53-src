title: Recon-ng Update (v3.0.3)
publish: True
categories: [projects]

I’ve been working on some really nice features for the Recon-ng framework that I was finally able to push up to the master branch of the repo last night. Below is a quick round-up of the new features, migration requirements, and information about how the changes will effect user experience.

### Home Folder Migration

To this point, all user generated data has been saved within the Recon-ng directory structure. While this worked fine in situations where users have root privileges, the framework was unusable in restricted user environments. Therefore, I decided to standardize the framework according best practices and make use of "home" folders. Using the "home" folder provides several key advantages. It avoids write errors in restricted user environments and allows for segregated multi-user environments. I began the "home" folder migration several weeks ago by adding the ability to build a separate module tree underneath a user’s "home" directory for custom modules (see wiki for details). As of today, the migration is complete.

After pulling down the new version of the framework, users will notice that none of their workspaces or API key data is available. Don't worry. It's still there. It just needs to be migrated to the new location by following these steps.

1. Launch the framework. The framework will detect whether or not migration has occurred. If it has not, the framework will build the necessary directory structure in the "home" (\~) folder.
1. Exit the framework.
1. Move all workspaces from the "recon-ng/workspaces/" directory to the "\~/.recon-ng/workspaces/" directory.
1. Move "recon-ng/data/keys.dat" to "\~/.recon-ng/keys.dat".

Migration complete.

### Record Command Changes

I wanted to give users more flexibility on where commands are recorded by the "record" command without having to set a global framework option. Therefore, I modified the "record" command to require an additional resource filename parameter for the "record start" command, `record start <filename>`. Now users can specify the resource file at runtime rather than have to set a global option.

### Workspace Control

Something didn't feel right about having the workspace as a global framework option. Therefore, I separated workspace control from the global options by implementing a new "workspace" command to the global context. Not only does this provide segregation, but it also allows for flexibility of workspace control through future expansion of the "workspace" command.

### Configuration Migration

Both the "rec_file" and "workspace" global options were removed from the global options list to support the above changes. As a result, the saved "config.dat" files in each workspace must be changed to remove these options or the framework will behave unpredictably. This can be done in one of two ways.

- Remove the "config.dat" file from all workspaces. A new "config.dat" file will be recreated the next time the workspace is loaded.
- Edit the "config.dat" file in all workspaces and remove the "rec_file" and "workspace" options from the stored JSON string.

### Prompt Appearance

I conducted a Twitter poll asking users of the framework to choose which they preferred between two prompt formats: the current `recon-ng >` or a proposed `[workspace] recon-ng >`. Users of the framework unanimously chose the proposed prompt. However, after seeing what the prompt looked like when a module was loaded, `[workspace] recon-ng [module] >`, I elected to make it `[recon-ng][workspace][module] >`. I tried many variations, but this one seemed to be the most aesthetically pleasing. Thanks to all those who provided feedback.

### Conclusion

Testing of the new features has been limited. Please report any bugs so that I can promptly address them. Thank you, and enjoy.

[Recon-ng Home Page](http://www.recon-ng.com)
