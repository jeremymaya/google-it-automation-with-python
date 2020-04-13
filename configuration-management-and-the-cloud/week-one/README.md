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

### What is Puppet

Puppet is the current industry standard for managing the configuration of computers in a fleet of machines. Puppet is:

* Cross-platform
* Open source project

Puppet is typically deploy using a client-server architecture.

* The client is known as the Puppet agent
* Te service is known as the Puppet master

When using this model,

1. The agent connects to the master and sends a bunch of facts that describe the computer to the master
2. The master then processes this information, generates the list of rules that need to be applied on the device
3. The master sends this list back to the agent
4. The agent is then in charge of making any necessary changes on the computer

Below example says that the package 'sudo' should be present on every computer where the rule gets applied.

```puppet
class sudo {
    package { 'sudo':
        ensure => present,
    }
}
```

Tasks Puppet can accomplish includes

* Install packages
* Add, remove, or modify configuration files stored in the system
* Change registry entries on Windows
* Enable, disable, start, or stop the services
* Configure crone jobs
* Schedule tasks
* Add, remove, or modify Users and Groups
* Execute external commands

### Puppet Resources

**Resources** are the basic unit for modeling the configuration that we want to manage in Puppet.

* Each resource specifies one configuration that we're trying to manage, like a service, a package, or a file

Below example is s a simple rule that ensures that etc/sysctl.d exists and is a directory.

```puppet
class sysctl {
    # resource type: file
    # resource title: '/etc/sysctl.d'
    file { '/etc/sysctl.d':
        # resource attributes
        ensure => directory,
    }
}
```

Below examples uses a file resource to configure the contents of etc/timezone, a file, which is used in some Linux distributions to determine the time zone of the computer.

```puppet
class timezone {
    # resource type: file
    # resource title: '/etc/timezone'
    file { '/etc/timezone':
        # resource attributes
        # this will be a file instead of a directory or a symlink
        # the contents of the file will be the UTC time zone
        # the contents of the file will be replaced even if the file already exists
        ensure => file,
        content => "UTC\n",
        replace => true,
    }
}
```

When we declare a resource in our puppet rules. We're defining the desired state of that resource in the system. The puppet agent then turns the desired state into reality using providers.

### Puppet Classes

**Classes** in Puppets are used to collect the resources that are needed to achieve a goal in a single place.

Below example groups all of the resources related to NTP in the same class to make changes in the future eaiser.

```puppet
# a class with three resources related to the Network Time Protocol, or NTP
# rules make sure that the NTP package is always upgraded to the latest version
class ntp {
    package { 'ntp':
        ensure => latest,
    }
    # contents of the file will be based on the source attribute
    file { '/etc/ntp.conf':
        source => 'puppet:///modules/ntp/ntp.conf',
        replace => true,
    }
    # enable and run the NTP service
    service {
        enable => true,
        ensure => running,
    }
}
```

---

## The Building Blocks of Configuration Management

### What are domain-specific languages

```puppet
if $facts['is_virtual']{
    package{ 'smartmontools':
        ensure => purged,
    }
}
else {
    package{ 'smartmontools':
        ensure => installed,
    }
}
```

### The Driving Principles of Configuration Management

```puppet
exec {'move example file':
    command => 'mv /home/user/example.txt /home/user/Desktop',
    onlyif => 'test -e /home/user/example.txt',
}
```

---

## Credit

* [Coursera - Configuration Management Cloud Week 1](https://www.coursera.org/learn/configuration-management-cloud/home/week/1)
