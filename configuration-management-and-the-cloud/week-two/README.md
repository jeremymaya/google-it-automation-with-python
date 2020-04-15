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

### Puppet Nodes

In Puppet terminology, a **node** is any system where a Puppet agent can run. To apply different rules to different systems is to use separate node definitions.

Below example is the default node with two classes, the sudo class and the ntp class.

```puppet
node default {
    class { 'sudo': }
    # sets an additional servers parameter which can be used to get the network time
    class { 'ntp':
            servers => [ 'ntp1.example.com', 'ntp2.example.com' ]
    }
}
```

Below example shows how to apply some settings to only some specific nodes by adding more node definitions.

```puppet
node default {
    class { 'sudo': }
    # sets an additional servers parameter which can be used to get the network time
    class { 'ntp':
            servers => [ 'ntp1.example.com', 'ntp2.example.com' ]
    }
    class { 'apache': }
}
```

Below example shows how specific nodes in the fleet are identified by their FQDNs, or fully qualified domain names.

```puppet
node webserver.example.com {
    class { 'sudo': }
    # sets an additional servers parameter which can be used to get the network time
    class { 'ntp':
            servers => [ 'ntp1.example.com', 'ntp2.example.com' ]
    }
    class { 'apache': }
}
```

### Puppet's Certificate Infrastructure

Puppet uses __public key infrastructure (PKI)__, __secure sockets layer (SSL)__, to establish secure connections between the server and the clients.

__Puppet comes with its own certificate authority__, which can be used to create certificates for each clients.

why do we care so much about the identity of the nodes? There's a bunch of reasons.

One of the reason why identity of the nodes matter is that the Puppet rules can sometimes include confidential information.

* Automatic sign all requests feature is available in Puppet, it should be limited to test deployment and never used for real computers being used by real users

---

## Updating Deploymnets

### Modifying and Testing Manifests

```puppet
describe 'gksu', :type => :class do
    let (:facts) { { 'is_virtual' => 'false' } }
    it { should contain_package('gksu').with_ensure('latest') }
end
```


---

## Credit

* [Coursera - Configuration Management Cloud Week 2](https://www.coursera.org/learn/configuration-management-cloud/home/week/2)
