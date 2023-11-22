# Learn Git and VS Code
## Copyright (c) 2023 TigerPointe Software, LLC

### Start with VS Code
* On the extensions tab, be sure to install "GitHub Repositories"
* Log into GitHub through VS Code
    * Connect to a repository
    * Log in through the browser
    * Authorize the workstation, if requested
* Set a local folder to hold the account repositories

### Create a New Repository
* Open a new folder in VS Code
* On the source control tab, initialize a new repository
* (Optional) Set local user account and email config  from a command shell
    * Change directory to the repository folder (contains ".git" folder)
    * `git config --local user.name jsmith`
    * `git config --local user.email jsmith@sample.com`

### Clone an Existing Repository
* Get the ".git" URL from the GitHub web site "<> Code" repository menu
* On the source control tab, clone the repository using the URL
* (Optional) Set local user account and email config  from a command shell
    * Change directory to the repository folder (contains ".git" folder)
    * `git config --local user.name jsmith`
    * `git config --local user.email jsmith@sample.com`

### Commit Changes
* On the file tab, add a new file (status is "U" untracked)
* In the editor, modify an existing file (status is "M" modified)
* On the source control tab, click "+" to stage changes
    * Stage an individual file by clicking the nearest "+"
    * Stage all files by clicking the "Changes" section "+"
* On the source control tab, click "Commit" to commit changes locally
* Enter a comment into the editor and click the "check mark" icon to close
* Click the "Cloud" icon initially to push changes to the remote repository
* For subsequent updates, click the "Sync" button or icon

### Notes
* New repositories default to private (free, but restricted features)
* Setting visibility to public makes the code available to anybody
* Visibility can be be changed on GitHub - Settings - Danger Zone
* On GitHub, add the description and topics
