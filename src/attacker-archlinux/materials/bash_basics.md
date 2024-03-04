## Concepts
### File attributes
```bash
# Listing advanced permissions (-a for show hidden and -R for recursively)
lsattr -aR
# Setting advanced permissions (-R for recursively, -V for verbosing and -f to ignore errors)
chattr +i 
```
- `-i`: Makes a file immutable
- `-c`: Stores the file compressed in disk
- `-u`: Makes the file recoverable if deleted
- `-e`: Make a clean removal if file is deleted
- `-S`: Synchronously reflect changes in the file in the HD


More info at man `chattr`

### The sticky bit
The main purpose of the sticky bit is to prevent users from deleting or renaming files within a directory that they do not own. In a directory with the sticky bit set, only the file owner, directory owner, or superuser can delete or rename the files within it, even if other users have write permissions on that directory.

For instance, it's commonly used on directories like `/tmp`, which is a shared directory where multiple users can read and write files. The sticky bit ensures that users can create and modify files within `/tmp` but cannot delete or rename files owned by other users.

It doesn't typically make sense to set the sticky bit on a file due to its intended functionality being associated specifically with directory permissions.

In order to set it

```bash
# Set
chmod +t /test.
# Unset
chmod -t /test.
```
or use the `1` before the octal representation of the permissions for a file.
```bash
# Set
chmod 1775 test
# Unset
chmod 0775 test
```

## SUID (Set User ID)

The Set User ID (SUID) permission is used to allow users to execute a particular executable file with the permissions of the file owner rather than their own permissions. This elevated access can be crucial for certain system utilities that need to perform actions that regular users don't have permission to execute.

In order to set it:
```bash
chmod u+s /usr/bin/python3.9
chmod 4xxx /usr/bin/python3.9
```
### Examples

- The `passwd` command allows users to change their passwords. Since the password file (`/etc/passwd` or `/etc/shadow`) is typically owned by root and has restricted permissions, the passwd executable has the SUID bit set. This enables regular users to execute passwd and change their passwords, as the process temporarily runs with root permissions, enabling the necessary write access to the password file.

- Programs like `top` or `ps` display system processes. They often require access to system information that regular users wouldn't have. The SUID bit is set on these executables, allowing them to gather system information and display processes even for non-privileged users.

- `ifconfig` allows users to configure network interfaces. Since changing network configurations requires system-level permissions, `ifconfig` is often set with the SUID bit. This allows regular users to execute it to view network configurations and, if necessary, modify them without needing root access.

- **Mounting** and **unmounting** drives require elevated permissions. The SUID bit is set on these executables to allow regular users to mount and unmount filesystems without needing root access, provided they are specified in `/etc/fstab` and have appropriate options set.

## SGID (Set Group ID)

Set Group ID (SGID) is a permission in Unix-like systems that, when applied to a directory, allows newly created files and directories within it to inherit the group ownership of the parent directory. It can also be applied to executable files, ensuring that when they are executed, they run with the group ownership of the file rather than the user's primary group.

In order to set it:
```bash
chmod g+s /usr/bin/python3.9
chmod 2xxx /usr/bin/python3.9
```

### Examples
- **Collaborative Workspaces**: Project directories where multiple users collaborate often have the SGID bit set. This ensures that all files and directories created within this project directory inherit the group ownership of the project group, allowing all users in that group to access and modify the files irrespective of who created them.

- **Shared Directories**: Shared directories used by a group of users, such as those for storing shared documents or resources, might have the SGID bit set. This ensures that all files created within this directory inherit the group ownership of the shared group, facilitating easy sharing and collaboration among the designated group members.

## Capabilities
### Capabilities
Capabilities in Linux refer to the fine-grained access control mechanisms that define what specific actions a process can perform. They allow processes to have different levels of permissions beyond the traditional read, write, and execute.

**Set capability**
```bash
# Set capability
setcap cap_setuid+ep /usr/bin/python3.9
# Unset capability
setcap -r /usr/bin/python3.9
```

Some common capabilities:
- **CAP_CHOWN**: Allows a process to change file ownership.
- **CAP_DAC_OVERRIDE**: Bypass file read, write, and execute permission checks.
- **CAP_DAC_READ_SEARCH**: Bypass permission checks for read and execute on files and directories.
- **CAP_NET_BIND_SERVICE**: Bind a socket to internet domain privileged ports (< 1024).
- **CAP_SYS_ADMIN**: Perform administrative tasks.
- **CAP_SYS_PTRACE**: Trace arbitrary processes using ptrace.
- **CAP_SETUID**: Set UID on execution.
- **CAP_SETGID**: Set GID on execution.
- **CAP_LEASE**: Establish leases on arbitrary files.

https://www.etl.it.uc3m.es/Linux_Capabilities
---
## FAQ
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


