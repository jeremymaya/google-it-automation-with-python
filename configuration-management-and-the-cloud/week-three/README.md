# Crash Course of Python - Week 3

## Learning Objectives

Dive into the details of the different Cloud services, when it makes sense to use them, and how to get the most out of the cloud deployments by:

* Learn how cloud deployments can help us quickly scale our services
* Learn the differences between when running IT infrastructure on-premise versus running it in the cloud
* Learn how we can use a variety of different tools to manage instances running in the cloud

---

## Cloud Computing

### Cloud Services Overview

A service is running in the Cloud means that the service is running somewhere else either in a data center or in other remote servers that can be __reached over via Internet__.

Cloud providers typically offer different service types such as:

* **Software as a Service** or SaaS, is when a Cloud provider delivers an entire application or program to the customer
* **Platform as a Service** or PaaS, is when a Cloud provider offers a preconfigured platform to the customer
* **Infrastructure as a Service** or IaaS, is when a Cloud provider supplies only the bare-bones computing experience

When setting up Cloud resources, **regions** need to be considered. A **region** is a geographical location containing a number of data centers, regions contain **zones** and zones can contain one or more physical **data centers**.

There are multiple factors that is detremiend based on the selected region,

* Latency
* Legal or political factors
* Other services as dependencies that is needed to run the service

### Scaling in the Cloud

capacity is how much the service can deliver.

queries per second or QPS

This capacity change is called scaling,

* Upscaling when the capacity is being increased
* Downscaling when the capacity is being decreased

There are a couple of different ways that we can scale our service in the Cloud,

* Horizontal scaling vs. Vertical scaling
  * Horizontally scaling scales the capacity by adding more nodes into the pool (eg. add more servers)
  * Vertically scaling scales the capacity by making the nodes bigger (eg. upgrade memories, CPU or disk space)
* Automatic scaling vs. Manual scaling
  * Automatic scaling uses metrics to automatically increase or decrease the capacity of the system which is controleld by the Cloud provider
  * Manual scaling are controlled by humans instead of software

### Evaluating the Cloud

In the case of cloud solutions, IT team is giving up some of its control to the cloud provider. Therefore, it's important to know what kind of support is available and select the one that fits the needs.

Treat the servers executing the workloads as a **commodity** and always use reasonable judgment to protect the machines that we deploy, whether that's on physical server is running on-premise or on virtual machines in the Cloud.

### Migrating to the Cloud

**IaaS** is especially useful to administrators using a **lift and shift strategy**.

When migrating to the Cloud, the process is somewhat similar. But instead of moving the physical server in the back of a truck, you migrate your physical servers running on-premise to a virtual machine running in the Cloud. In this case, you're shifting from one way of running your servers to another. The key thing to note with both approaches, is that **the servers core configurations stay the same**.

**PaaS** is well-suited for when you have a specific infrastructure requirement, but you don't want to be involved in the day-to-day management of the platform

**Containers** are applications that are packaged together with their configuration and dependencies.

There are different types of Cloud services:

* Public Cloud is services provided by the public Cloud providers
* Private Cloud is when one company owns the services and the rest of the infrastructure
* Hybrid Cloud is a mixture of both public and private Clouds
* Multi-Cloud is a mixture of public and/or private Clouds across vendors

---

## Managing Instances in the Cloud

There are different Cloud providers each with some specific advantages depending on what we are trying to achieve. But usually Cloud service providers implement a console to manage the services.

Regardless of the service proivder, following paramaters needs to be set when creating a VM running in the Cloud

* Name of the instance
* Region and zone where the instance will be running
* CPU, memory and boot disk options for the VM

Cloud service proivders also porvides the command line interface, which allows for us to specify what we want once, and then use the same parameters many times. __Using the command line interface lets us create, modify, and even delete virtual machines from our scripts.__

**Reference images** store the contents of a machine in a reusable format, while templating is the process of capturing all of the system configuration to let us create VM in a repeatable way. That exact format of the reference image will depend on the vendor. But often, the result is a file called a **disk image**. A disk image is a snapshot of a virtual machine's disk at a given point in time.

---

## Automatic Cloud Deployments

---

## Credit

* [Coursera - Configuration Management Cloud Week 3](https://www.coursera.org/learn/configuration-management-cloud/home/week/3)
