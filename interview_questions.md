Linux
-----
* what is your favorite linux distribution
* what is zombie process and how to kill it
* what is going to happen when you run this command in linux shell, how would you protect the host against this? (ulimits)
* chmod a+x test.txt what does this do
1. What is the purpose of the shebang line in scripts? Provide an example.
2. How do you list all files, including hidden ones, in a directory?
3. What command would you use to find the IP address of a Linux server?
4. Explain the difference between a hard link and a symbolic link.
5. How would you display the first 10 lines of a file?
6. Write a Bash script that outputs the current date and time every 5 minutes.
7. How do you change the permissions of a file to be readable, writable, and executable by the owner, and only readable by the group and others?
8. What does the command `sudo` do?
9. Describe how to compress a folder and its contents using `tar`.
10. How can you find and replace the string "hello" with "world" in all `.txt` files in the current directory?
11. Explain what a process in Linux is and how you can view running processes.
12. What does the `&` symbol at the end of a command do?
13. How do you schedule a cron job to run every day at 3 pm?
14. Describe the purpose of the `/etc/passwd` file.
15. Write a command to count the number of lines in a file.
16. How would you add a new user with a home directory to the system?
17. What is the difference between `>` and `>>` operators in shell scripting?
18. How do you check disk usage of a directory?
19. Explain the significance of the PATH environment variable.
20. Write a one-liner to display the top 5 processes in terms of memory usage.


```
:(){ :|:& };:
```

Python
-----
1. What is the difference between a list and a tuple in Python?
2. How do you create a virtual environment in Python and why would you use one?
3. Write a Python function that checks if a given word is a palindrome.
4. Explain the concept of list comprehension and provide an example.
5. What is a decorator in Python? Give a simple example of how to use one.
6. How can you handle exceptions in Python? Provide a code example.
7. What is the purpose of the `__init__` method in Python classes?
8. How do you manage packages and dependencies in a Python project?
9. Describe how to iterate over a dictionary and access both the keys and the values.
10. How do you convert a string to a number in Python?
11. What is the difference between the `deepcopy` and `copy` functions in the `copy` module?
12. Write a Python script that reads a file line by line and prints each line.
13. Explain the concept of generator functions and why they are used in Python. Provide an example.
14. How do you perform unit testing in Python? Mention a framework and give an example.
15. Describe the difference between the `==` operator and the `is` operator in Python.
16. How can you improve the performance of a Python script that processes large amounts of data?
17. Explain how the Global Interpreter Lock (GIL) affects multi-threading in Python.
18. Write a Python one-liner that removes duplicates from a list.
19. How do you make an API request in Python and process the JSON response?
20. Explain the use of the `with` statement in Python, especially in the context of file operations.

                                                                                                                                                                                                                                    
Git
---
- difference between merge and rebase
- how to squash commit and why
- how would you remove secrets from git repository
- what git branching strategies you know and give example of projects where they are best fit

AWS
---
- explain private and public subnets in AWS
- how can you create static site on AWS S3 with https and custom domain name?
- what are AWS load balancer types, main differences between them and when to use which
- how could you monitor AWS Aurora Mysql database for slow/long queries
- propose a secure network setup for 3-Tier application with frontend, backend running on ec2 and database
- migrate from RDS instance to Aurora RDS Cluster with zero downtime
- how can you configure secure ssh connection to EC2 instance without public ip
- suggest how to optimize costs on AWS account
- RDS how to analyze performance
- S3 do names need to be unique?
- How would you automate security patching of EC2 instances
- How can you migrate from RDS Postgres to Aurora RDS Postgres
- How can you ensure high availability of RDS database
- How would you automate extending disk space on Linux EC2 instance
- describe process of upgrading EKS cluster

Jenkins
-------
- your job is to setup Jenkins for client in the AWS cloud for building and deploying docker containers to ECR, how would you do it?

CI/CD
------
""
https://codesandbox.io/s/exciting-andras-951gi1?f
what is continious integration
continious integration with feature branches?
- what git branching strategies you know and give example of projects where they are best fit
difference between Continous deployment and Continous delivery
what does shift left mean? give examples
how would you create CI/CD pipeline for database schema and logic changes
what deployment strategies 
- are you familiar with dora metrics?

Terraform
---------
what is terraform workspace
what happens when you run terraform init
design secure CI/CD pipeline for terraform
how can you create resources in two different regions with terraform

Ansible
-------
- what is ansible role
- you have to run ansible playbook against AWS EC2 instances with ansible, there is auto scalling and instances keep changing, how would you make sure that your inventory always has all the ec2 instances automaticaly?

Azure
-----
- design Azure architecture for classic n-tier application (presentation,application,data)
- user assigned idenity vs system assigned identity
- what deployment strategies you know, their pros and cons
- how would you implement blue/green deployments on azure vm / app service / aks
- application running in azure needs access to Azure Storage blob, what is best way to grant it access
- how to allow app service read configuration values directly from Key Vault
- how can you create image of VM without breaking the VM

Questions
=========

General
* What branching strategies do you know, describe one and when would you use it
* do you know what semantic versioning is, describe how it works
* explain cloud native and cloud agnostic
* explain ServiceLevelAgreement ServiceLevelObjective ServiceLevelIndicator
* do you know what Postmortem is?

CI/CD
* difference between Continous deployment and Continous delivery
* describe how would you do CI/CD pipeline for database changes, tools you would use etc

Linux
* what is zombie process and how to kill it
* what is your favorite linux distribution
* what is going to happen when you run this command in linux shell, how would you protect the host against this? (ulimits)
```
:(){ :|:& };:
```

Docker/Kubernetes
* what are docker layers
* what is the difference between docker image and docker container
* what is pod in kubernetes
* what is container runtime? name some container runtimes supported by Kubernetes
* signal handling, which should you use and why:
ENTRYPOINT "/app/bin/your-app arg1 arg2"
ENTRYPOINT ["/app/bin/your-app", "arg1", "arg2"]
* control plane and data plane in K8S
* types of services
* service account in EKS
* what is Operator. Did you use any operators
* PDB
* taints and tolerations
* How can you assign iam role only to single pod in EKS


* lets say you have to create dockerfile that builds and runs java application, how would you do it, what are the best practices when writing dockerfiles
  * version vs latest tag
  * layer ordering
  * jar unpacking if its fat jar
  * multistage build
  * how to store configuration - env
  * logs? to stdout
  * dockerignore
  * which java version? - 1.8.0_191 or later, preferably 11+

* you have dockerized python application, what will be the PID of application process in running container?

Ansible
* what is needed on remote host to use Ansible - linux and windows

AWS
* private vs public subnet?
* SG vs ACL
* types of load balancers and their use cases in AWS
* explain what is Lambda cold start and how to mitigate that
* What is AWS Route53 Alias Record and why do you use it, difference between Alias and Cname record in route53
* how to expand EBS volume on EC2 instance running Linux
* client asked you to design active-passive architecture, explain what that means and how to do that
* lets say you have AWS VPC and Aurora database that should not be available publicly. You need to create lambda that will have network access both to internet and the database. How can you do that?
* do you know what bastion host / jumpbox / jumphost is? how would you create and secure linux bastion host in AWS?
* you are administrator of AWS account and you store multiple secrets in Parameter Store as secure strings, you need to configure it in a way that allows non-administrator users to see the secrets in SSM but not their values, how would you do that
- how can you create static site on AWS S3 with https and custom domain name?
- propose a secure network setup for 3-Tier application with frontend, backend running on ec2 and database
- how can you configure secure ssh connection to EC2 instance without public ip
- suggest how to optimize costs on AWS account
- how can you automate EC2 os security patching
- blue/green deployment of applications on EC2 instances


Terraform
* your job is to write terraform module that will be used by multiple teams, in that module you have variable and you need to ensure that only one of two values can be assigned "1" or "2", how would you do this?
* client has multiple AWS accounts dev, qa, staging, production and managment account. He wants to use terraform, terraform should always run using user credentials from managment account and store state in managment account s3. How can you configure terraform and aws to achieve this?

Jenkins
* you are working on Jenkins shared library and see method definiton with annotation @NonCPS - do you know what is that?

```
@NonCPS
def compileOnPlatforms() {
  ['linux', 'windows'].each { arch ->
    node(arch) {
      sh 'make'
    }
  }
}
```

* how would you host Jenkins in cloud environment
* you have to setup jenkins master on ec2 instance, how would you harden it