# Introduction to Git and GitHub - Week 4

## Collaboration

### Pull Requests

**Forking** is a way of creating a copy of the given repository so that it belongs to our user.

**Pull request** is a commit or series of commits that you send to the owner of the repository so that they incorporate it into their tree.

When collaborating on projects hosted on GitHub, the typical workflows is:

1. Create a fork of the repo
2. Work on that local fork

---

## Code Review

### Managing Collaboration

**Code review** means going through someone else's code, documentation or configuration and checking that it all makes sense and follows the expected patterns.

The goal of a code review is:

* To improve the project by making sure that changes are high quality
* Helps make the contents are easy to understand
* The style is consistent with the overall project
* Remind us about any important cases

### Continuous Integration

**Continuous integration** is a system building and testing code every time there's a change.

**Continuous deployment** means the new code is deployed often. The goal is to avoid roll outs with a lot of changes between two versions of a project and instead do incremental updates with only a few changes at a time.

Some of concepts that needs to be dealt with when creating CICD includes:

1. Pipelines, which specifies the steps that need to run to get the desired result
2. Artifacts, which is the name used to describe any files that are generated as part of the pipeline

---

## Managing Projects

When collaborating:

* Documenting any work is important
* As a project maintainer, reply promptly to pull requests and don't let them stagnate
* Understand any accpeted changes
* Use an issue tracker to coordinating who does what and when
* Have a way of communicating and coordinating between contributors

---

## Credit

* [Coursera - Introduction Git Github Week 4](https://www.coursera.org/learn/introduction-git-github/home/week/4)
