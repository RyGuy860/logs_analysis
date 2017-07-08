# Welcom to my Logs Analysis project.

The objective of this project is to build queries that answer the following three questions. 

1. What are the most popular three articles of all time?

2. What are the most popular article authors of all time?

3. On which days did more than 1% of request lead to errors? 

# Getting started: 

1. Install VirtualBox
- VirtualBox is the software that actually runs the virtual machine. You can download it from https://www.virtualbox.org/wiki/Downloads. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

- Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

2. Install Vagrant:
- Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from https://www.vagrantup.com/ Install the version for your operating system.

- Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

3. Download the VM configuration:
- Fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm
- Next change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:
- You will need to unzip news.zip 
-Then cd to the news directory and this will give you access to news.py

4. Starting the virtual machine:
- From your terminal, inside the vagrant subdirectory, run the command vagrant up

5. Logging into your VM
- You can run vagrant ssh to log in to your newly installed Linux VM!

6. Load the data:
- Use the command psql -d news -f newsdata.sql.

7. Views that were created 

 ok_requests
- create view ok_requests as select date_trunc('day', time) as date, count(*) as num_ok from log where status = '200 OK' group by date;

 total_requests
- create view total_requests as select date_trunc('day',time) as date, count(*) as num_total from log group by date;

8. Run code
- python news.py from your termial. 
