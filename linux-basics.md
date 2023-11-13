
### What user am I?
```bash
$ whoami
bolalelilolu
```

### What user am I? What groups do I belong to?
```bash
$ id
uid=1000(bolalelilolu) gid=1003(bolalelilolu) grupos=1003(bolalelilolu),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),108(netdev),116(bluetooth),1000(lpadmin),1001(scanner),1002(docker)
```

### Which groups are out there?
```bash
$ cat /etc/group
```

### Where is the binary that executes this command?
```bash
$ which <command>
```
### Which are the personal folders for every user in my system?
```bash
$ cat /etc/passwd
```
### Which shells are out there?
```bash
$ cat /etc/shells
```
### Which is the status code for my previous command?
```bash
$ echo $?
```
### How to get rid of errors in the console?
```bash
$ <command> 2>/dev/null
```
### How to get rid of output in the console?
```bash
$ <command> >/dev/null
```
### How to get rid of outputs and errors in the console?
```bash
$ <command> >/dev/null 2>&1
```
### How to run a command in silence, in the background, without linking it to the console?
```bash
$ <command> &>/dev/null & disown
<TASK-PID>
```
### Which type of files am I dealing with?
```bash
$ file .
```
### How to set up a user in the system?
```bash
# Create a folder for the user
$ mkdir /home/pepe
# Create a user with name `pepe` and a specific bash and home directory
$ useradd pepe -s /bin/bash -d /home/pepe
# Set a password for this user
$ passwd pepe
# Assign group `pepe` to home directory
$ chgrp pepe /home/pepe
# Make user `pepe` the owner of the home directory
$ chown pepe /home/pepe

# Quicker option for setting both user and group
$ chown pepe:pepe /home/pepe
```
### How to assign a user to a group?
```bash
# Create the group
$ groupadd Alumnos
# Add the user pepe to the group
$ usermod -a -G Alumnos pepe
```
### What is the sticky bit?

