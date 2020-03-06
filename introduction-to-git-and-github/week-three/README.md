# Introduction to Git and GitHub - Week 3

## Introduction to GitHub

### What is Github

GitHub is a web-based Git repository hosting service whle Git is a distributed version control system.

* Distributed means that each developer has a copy of the whole repository on their local machine.

For real configuration and development work, more secure and private Git server needs to be used, and limit the people authorized to work on it.

### Git Commands to Interact with Remote Repository

* git clone URL: Git clone is used to clone a remote repository into a local workspace
* git push: Git push is used to push commits from your local repo to a remote repo
* git pull: Git pull is used to fetch the newest updates from a remote repository

---

## Using a Remote Repository

### What is a remote

Remote repositories allows

* Developers contribute to a project from their own workstations making changes to local copies of the project independently of one another
* Developers to use git commands to pull code from a remote repository or push code into one when they need to share their changes

### Git Remote Cheatsheet

* git remote: Lists remote repos
* git remote -v: List remote repos verbously
* git remote show \<name>: Describes a single remote repo
* git remote update: Fetches the most up-to-date objects
* git fetch: Downloads specific objects
* git branch -r: Lists remote branches; can be combined with other branch arguments to manage remote branches

---

## Solving Conflicts

### Rebasing Your Changes

Rebasing means changing the base commit that's used for our branch.

The problem with three way merges is that because of the split history, it's hard for us to debug when an issue is found in our code, and we need to understand where the problem was introduced. By changing the base where our commits split from the branch history, we can replay the new commits on top of the new base. This allows Git to do a fast forward merge and keep history linear.

Run the command git rebase, followed by the branch that we want to set as the new base.

### Best Practices for Collaboration

* Always synchronize your branches before starting any work on your own
  * Starting from the most recent version and you minimize the chances of conflicts or the need for rebasing
* Avoid having very large changes that modify a lot of different things
  * Push your changes often and pull before doing any work to reduce the chances of getting conflict
* Have the latest version of the project in the master branch and a stable version of the project on a separate branch.
* Rebasing can help a lot with identifying bugs, but use it with caution
  * Whenever we do a rebase, we're rewriting the history of our branch
  * Do not rebase changes that have been pushed to remote repos
* Have good commit messages

---

## Credit

* [Coursera - Introduction Git Github Week 3](https://www.coursera.org/learn/introduction-git-github/home/week/3)
