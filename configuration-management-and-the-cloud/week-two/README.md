# Crash Course of Python - Week 2

## Learning Objectives

Dive deeper into baisc congfiguration management concepts and Puppet by:

* Learn how to install Puppet on your computer and how to use a simple test setup to check your rules work as expected
* Learn how to configure the typical client-server set-up with Puppet clients connecting and authenticating to the Puppet server to get the rules that they should apply
* Learn how to use testing techniques and releasing best practices to safely deploy changes to clients of our configuration management system

---

## Deploying Puppet

### Applying Rules Locally

The **manifest** is a file with .pp extention where we'll store the rules that we want to apply.

Checkout tools.pp file as an example.

The **catalog** is the list of rules that are generated for one specific computer once the server has evaluated all variables, conditionals, and functions.

### Managing Resource Relationships

Checkout ntp.pp file as an example.

### Organizing Your Puppet Modules

In puppet, manifests are organized into **modules**. A module is a collection of manifests and associated data.

* Manifest directory which stores manifest and init.pp where it defines a class with the same name as the created module
* Templates directory which stores any files that stores rules to be used

---

## Deploying Puppet to Clients

---

## Updating Deploymnets

---

## Credit

* [Coursera - Configuration Management Cloud Week 2](https://www.coursera.org/learn/configuration-management-cloud/home/week/2)
