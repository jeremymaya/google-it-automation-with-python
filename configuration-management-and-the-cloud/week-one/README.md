# Crash Course of Python - Week 1

## Learning Objectives

Look into how automation can be applied to manage fleets of computers by:

* Learn how to use **Puppet**, the current industry standard for configuration management
* Learn about the benefits and challenges of moving services to the Cloud
* Learn the best practices for handling hundreds of virtual machines running in the Cloud

---

## Introduction to Automation at Scale

### What is scale

Being able to **scale** means keep achieving larger impacts with the same amount of effort. A scalable system is a **flexible**.

**Automation** is an essential tool for keeping up with the infrastructure needs of a growing business.

### What is configuration management

**Unmanaged configuration** manually deploys the installation and configuring a computer.

**Managed configuration** uses a **configuration management system** to handle all of the configuration of the devices in the **nodes** which aims to solve the scaling problem.

* Typically you'll define a set of rules that have to be applied to the nodes you want to manage and then have a process that ensures that those settings are true on each of the nodes

Configuration management system allows a way to make changes to a system or group of systems in a **systematic**, **repeatable way**.

### What is infrastructure as code

**Infrastructure as Code** or IaC is the paradigm of storing all the configuration for the managed devices in version controlled files. This is then combined with automatic tooling to actually get the nodes provisioned and managed.

The principals of Infrastructure as Code are commonly applied in __cloud computing environments__, where machines are treated like __interchangeable resources__, instead of individual computers.

IaC allows the followings:

* Makes the deployment consistent
* Applies the benefits of the version control system to the infrastructure
* Run automated tests on the files

In a complex or large environment, treating your IT Infrastructure as Code can help you deploy a flexible scalable system. A configuration management system can help you manage that code by providing a platform to maintain and provision that infrastructure in an automated way.

Managing your Infrastructure as Code it means that the fleet of nodes are **consistent, versioned, reliable, and repeatable**.

---

## Introduction to Puppet

---

## The Building Blocks of Configuration Management

---

## Credit

* [Coursera - Configuration Management Cloud Week 1](https://www.coursera.org/learn/configuration-management-cloud/home/week/1)
