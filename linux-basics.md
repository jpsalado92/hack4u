## Concepts
### File attributes
```bash
# Listing advanced permissions (-a for show hidden and -R for recursively)
lsattr -aR
# Setting advanced permissions (-R for recursively, -V for verbosing and -f to ignore errors)
chattr +i 
```
`-i`: Makes a file immutable
`-c`: Stores the file compressed in disk
`-u`: Makes the file recoverable if deleted
`-e`: Make a clean removal if file is deleted
`-S`: Synchronously reflect changes in the file in the HD


More info at man `chattr`

### The sticky bit
The main purpose of the sticky bit is to prevent users from deleting files within a directory that they do not own. In a directory with the sticky bit set, only the file owner, directory owner, or superuser can delete or rename the files within it, even if other users have write permissions on that directory.

For instance, it's commonly used on directories like /tmp, which is a shared directory where multiple users can read and write files. The sticky bit ensures that users can create and modify files within /tmp but cannot delete or rename files owned by other users.

It is also to enforce keeping in memory the programs that have it set, even if they have been executed already.


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

**SUID (Set User ID):**

The SUID permission allows a file to be executed as if it were the owner, regardless of the user executing it, the file will be executed as the owner.

Of course, one thing to keep in mind and quite important, is that the SUID permission does not work in scripts, it only works in compiled binaries. This is done for security reasons. In any case, if you wanted to enable the execution of a script as another user, you can always use sudo.

The SUID does not apply to directories because there is no compelling reason why it should.

In order to set it:
```bash
chmod u+s /usr/bin/python3.9
chmod 4xxx /usr/bin/python3.9
```
## SGID (Set Group ID)

SGID permission is related to groups, it has two functions:

- If set to a file, allows any user to run the file as if they were a member of the group to which the file belongs.
- If set to a directory, any file created in the directory will be assigned as a group belonging to the directory's group.

For directories, the logic of the SGID and the reason for its existence is if we work in a group, so that we can all access other people's files. If SGID did not exist, every time each person created a file, they would have to change it from their group to the project's common group. Likewise, we avoid having to assign permissions to "Others".

When the SGID permission is assigned, we can notice it because in the permissions, in the group part, in the execution permission an s will be assigned. Be careful, two distinctions must be made here:

- If the file has executable permissions, it will be assigned a lowercase `s`.
- If the file does NOT have executable permissions, it will be assigned a capital `S`.

This really has no relevance for directories, only for files. In any case, this characteristic of upper or lower case s depending on the execution permission is always applied, included in the SUID permission.

In order to set it:
```bash
chmod g+s /usr/bin/python3.9
chmod 2xxx /usr/bin/python3.9
```

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


