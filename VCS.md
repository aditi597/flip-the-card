###     **WHAT IS VCS ? WHAT IS ITS IMPORTANCE ?**  

VCS stands for **Version Control Systems**. Version Control Systems are a category of software tools that help a software team manage changes to the *source code* over time. Version control is sometimes referred to as **revision control** or **source control**. It’s an important component of software configuration management. Version control software keeps track of every modification to the code  in a special kind of database. Version control system is a kind of *database* . It lets you save a *snapshot* of your complete project at any time you want. When you later take a look at an older snapshot , your VCS shows you exactly how it differed from the previous one.

Version control is important for today’s development teams. It needs to do more than just manage and track files. It should help you develop and ship products faster. 

That’s because using version control:

- Improves visibility.

- Helps teams collaborate around the world.

- Accelerates product delivery.

  

  ### **CLONING A GIT REPOSITORY **

  #### What is cloning ? 

  When you create a repository on GitHub, it exists as a *remote* repository. You can clone your repository to create a *local* copy on your computer and sync between the two locations.

  #### How is it done ? 

  We can clone a repository by following these simple steps:

  1. On GitHub, navigate to the main page of the repository.

  2. Under the repository name, click **Clone or download**. Under the repository name, click **Clone or download**.

  3. In the Clone with HTTPs section, click  to copy the clone URL for the repository.

  4. Open Git Bash.Open Git Bash.

  5. Change the current working directory to the location where you want the cloned directory to be made.

  6. Type **git clone** , and then paste the URL you copied in Step 2.

  7. Press **Enter**. Your local clone will be created.

     

  ### Pull/Push to remote repository

  #### What is pushing and pulling/fetching a repository ?
  
  When we make a change to a local repository, we can push a change to a Git remote repository. Likewise, when the remote gets changed, we can pull the changes back to our local repository.We can update our local **repositories** with new data from the central server by an operation called “**pull**” and affect changes to the main **repository** by an operation called “**push**” from our local **repository**.
  
  #### **How to pull from a Git remote repository**?
  
  Usually, another person working on the same project makes a change to the remote. They change the code on their computer, and they push it to the remote repository.Once the remote repository changes, you can pull it back to your local repository to get the updated version. 
  
  **Pulling from remote-** To get data from remote projects, we can run *git fetch [remote-name]* .This command goes out to the remote project and pulls down all the data from that remote project that we don't have yet.
  
  **Pushing to remote-** When we have project at a point that we want to share  it, we have to push it upstream. The command for doing this is, *git push [remote-name] [branch name].* 
  
  ### STATUS OF THE REPOSITORY
  
  The command checks the status and reports that there’s nothing to commit, meaning the repository stores the current state of the working directory, and there are no changes to record. The main tool we use to determine which files are in which state is the git status command. 
  
  #### How to check the status of the repository ?
  
  We will use the command, *git status*, to keep monitoring the states of both the working directory and the repository.
  
  If we run this command directly after a clone, we should see something like,"nothing to commit, working directory clean", which means there are no tracked and modified files. If  we added a new file that didn't existed before, the git status will show up, "Untracked files: " , which means we didn't commit anything to this file yet.
  
  ### BRANCHES IN GIT
  
  #### What are branches?
  
  A branch in Git is simply a movable pointer to one of the many commits. The default branch name in Git is **master**. As we start making commits, we're given a master branch that points to the last commit we made. Everytime we commit, it moves forward automatically.
  
  #### Creating a new branch
  
  Creating a new branch means creating a new pointer for ourselves to move around. How does Git know what branch we're currently on? it keeps a special pointer called **head**. The *git  branch* command creates only a new branch, and doesn't help in switching.
  
  #### Switching branches
  
  To switch to an existing branch, we run the *git checkout new* command. This moves the **head** to the new branch.
  
  ### CONNECT TO A REMOTE REPOSITORY
  
  In Git, every developer working in the project gets their respective copy of the project repository. So, they have their own respective local development environment, branches and repository history.  
  
  Now, to connect with other developer's repository or to connect with the central repository we take help of the *git remote* command. When we clone a repository from a remote server, Git automatically remembers this connection for us. It saves it as a remote called "origin" by default.
   In other cases where we started with a fresh local repository, no remote connections are saved. In that situation, we need to connect our local repository to a new remote before we can try some remote interactions. We run, *git remote  add xyz*.
  
  ### MERGING TWO BRANCHES
  
  Merging is Git's way of putting a forked history back together again. The *git merge*  command lets you take the independent lines of development created by *git branch* and integrate them into a single branch.The current branch will be updated to reflect the merge, but the target branch will be completely unaffected. Again, this means that *git merge*  is often used in conjunction with *git checkout*  for selecting the current branch and *git branch -d* for deleting the obsolete target branch. The following steps are taken,
  
  1. *git checkout a*  -will switch you to branch a.
  
  2. *git merge b*  - will merge all the changes from branch b into branch a.
  
  3. *git commit -a*  - will commit your changes.
  
     
  
  ### HOW TO RESOLVE MERGE CONFLICTS USING COMMAND LINE
  
  The most direct way to resolve a merge conflict is to edit the conflicted file. Open the  file in your favorite editor.Once the file has been edited use *git add xyz*  to stage the new merged content. To finalize the merge create a new commit .Git will see that the conflict has been resolved and creates a new merge commit to finalize the merge.
  
  **Tools to resolve merge conflicts**.
  
  The *git status* command is in frequent use when a working with Git and during a merge it will help identify conflicted files.. Passing the *--merge*  argument to the *git log* command will produce a log with a list of commits that conflict between the merging branches. *diff*  helps find differences between states of a repository/files. This is useful in predicting and preventing merge conflicts.
  
  ### COMMIT CHANGES
  
  A commit is used to record changes made in a repository. After a staging area is set up, finally we need to commit our changes. Anything that is still unstaged, any files we have created or modified that we haven't run *git add* on since we edited them, won't go into this commit. They will stay as modified files on our disk. If everything is staged on running *git status* , we're ready to commit our changes. The simplest way to commit is to type *git commit*. 
  
  ### STASHING CHANGES  
  
  Often, when you’ve been working on part of your project, things are in a messy state and you want to switch branches for a bit to work on something else. The problem is, you don’t want to do a commit of half-done work just so you can get back to this point later. The answer to this issue is the  *git stash* command. Stashing takes the dirty state of your working directory — that is, your modified tracked files and staged changes — and saves it on a stack of unfinished changes that you can reapply at any time.



