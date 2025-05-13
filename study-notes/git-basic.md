# Git Basic

### Git Workflow Overview
Git operates in three main steps:

**Initialization**: Set up a new repository.  
**Staging**: Track your file changes.  
**Committing**: Capture and save the state of your project.  

### Check Version
        git version

### Repository Initialization
To start tracking code, initialize a Git repository by running the following command in project’s root directory:

        git init

`This will creates a hidden directory name ".git", which stores all metadata and information about the repository.`

### Check Repository Status
        git status

Initially, Git will classify all files as untracked. To track files while excluding, for example the following files;

- FileA.txt
- FileB.txt
- FileC.txt
- README.md

        git add FileA.txt FileB.txt FileC.txt README.md

If after `git add` a file and you make modifications to it, it will be marked as modified. Than it will require to stage the changes again.

Example;  
`After modify FileA.txt`  
        
        git add FileA.txt

### Commit Changes

        git commit -m "Commit Messsage"

### Connect your local repository to the remote repository

       git remote add github https://github.com/mmumshad/my-application.git 

### Push Local changes to remote repository

        git push -u github master

`-u` stands for `--set-upstream`  
Since the remote branch doesn't yet exist, use the --set-upstream option to establish a connection between local branch (by default, "master") and the remote branch.

### Clone
        git clone https://github.com/mmumshad/my-application.git

### Synchronize local copy with the remote repository
        git pull

### View All the Configured Remotes
        git remote -v

