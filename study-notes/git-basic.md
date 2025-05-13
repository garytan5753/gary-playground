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

*`git add .` to stage all changes*

### Commit Changes

        git commit -m "Commit Messsage"

### Connect your local repository to the remote repository

       git remote add github https://github.com/mmumshad/my-application.git 

### Push Local changes to remote repository

        ### Syntax
        git push -u origin feature-branch
        git push -u github master

`-u` stands for `--set-upstream`  
Since the remote branch doesn't yet exist, use the --set-upstream option to establish a connection between local branch (by default, "master") and the remote branch.

### Clone
        git clone https://github.com/mmumshad/my-application.git

### Synchronize local copy with the remote repository
        git pull

### View All the Configured Remotes
        git remote -v

### Set Global User (Default for All Repos)

        git config --global user.name "Your Name"
        git config --global user.email "you@example.com"

### Set Local User (Per Repository)
Navigate to the repo, then;

        git config user.name "Work Name"
        git config user.email "you@work.com"

### View Current Config

        git config user.name
        git config user.email

To see all levels;

        git config --list --show-origin

### Using Multiple SSH Keys (Advanced)
Use different GitHub/GitLab accounts, can manage them with SSH keys and custom SSH config.

1) Generate different keys:

        ssh-keygen -t rsa -C "work@example.com" -f ~/.ssh/id_rsa_work
        ssh-keygen -t rsa -C "personal@example.com" -f ~/.ssh/id_rsa_personal

2) Add to SSH agent:

        ssh-add ~/.ssh/id_rsa_work
        ssh-add ~/.ssh/id_rsa_personal

3) Create SSH config:

        # Work account
        Host github.com-work
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_rsa_work

        # Personal account
        Host github.com-personal
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_rsa_personal

4) Use appropriate remote URL:

        git remote set-url origin git@github.com-work:your-work-username/repo.git
        or
        git remote set-url origin git@github.com-personal:your-personal-username/repo.git

### git checkout / git switch

        git checkout main
        git checkout -b feature-xyz   # Create and switch to new branch

        # Or modern version:
        git switch main
        git switch -c feature-xyz

### git merge / git rebase

        git merge feature-xyz       # Merge changes
        git rebase main             # Replay commits on top of another base

Use merge to combine completed feature branches into main

### git fetch
Download new changes from remote, without merging them  

        git fetch origin

### git log
View commit history  

        git log
        git log --online

### git diff

        git diff               # Compare working directory and staged
        git diff --staged      # Compare staged files to last commit

### git stash
Temporary save uncommitted changes. When require to switch branches but aren't ready to commit.

        git stash
        git stash pop

### git branch

        git branch             # List branches
        git branch -d branch   # Delete branch

### git reset / git revert
Undo changes  

        git reset HEAD file.txt    # Unstage
        git reset --hard           # Dangerous! Wipes local changes
        git revert <commit-hash>   # Safely undo a commit

### git cherry-pick
Used to copy a specific commit from one branch and apply it to anotehr branch.  
It applies the changes from an existing commit onto current branch. 

        git cherry-pick <commit-hash>

| Tip                          | Description                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------ |
| Cherry-pick multiple commits | `git cherry-pick <hash1> <hash2>`                                                    |
| Range of commits             | `git cherry-pick A^..B` (from A's parent to B)                                       |
| Resolve conflicts            | If conflicts occur, Git will pause — resolve them, then `git cherry-pick --continue` |
| Abort cherry-pick            | `git cherry-pick --abort` if you want to cancel during conflict                      |




