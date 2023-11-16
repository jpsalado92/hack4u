# LINUX Directory Structure

## Directory types

### Static Directory
A static directory typically refers to a location in the file system that contains files or resources that are not expected to change frequently or are essential for the system's operation.

For example, directories like `/bin`, `/sbin`, `/lib`, and `/usr` often contain essential binaries, system commands, libraries, and user-specific programs. These directories usually hold static content that the system and its applications rely on for functioning.

### Shareable Directory
This term could refer to a directory that is accessible and meant to be shared among users or systems within a network.

A shareable directory might be set up using network file sharing protocols like NFS (Network File System) or Samba. These directories allow multiple users or systems to access and use the files stored within them. They're often used for collaborative work, file exchange, or providing shared resources across a network.

### Variable Directory
There isn't a standard term called "variable directory" in Linux. It's possible that it might refer to directories where the content is subject to change or can be modified frequently.

Most directories in a Linux system are writable to some extent by users or applications, allowing them to create, modify, or delete files within those directories. Directories like /home or /var often contain user-specific files and variable data (such as logs, caches, spool files, temporary files) that can change over time as users interact with the system and applications run.

## Directories at root
### `/`
The root directory, symbolized by the symbol `/`, is the main directory from which all other directories branch.

### `/bin` and `/sbin`
The `/bin` directory is a static and shareable directory in which binary/executable files necessary for the basic operation of the system are stored. These binary files can be used by all users of the operating system.

The `/sbin` directory is a static and shareable directory. Its function is similar to the `/bin` directory, but unlike the `/bin` directory, the `/sbin` directory stores binary/executable files that can only be executed by the root user or system administrator.

Files in this directory and are intended for operations related to the OS.

### `/boot`
It is a non-shareable static directory that contains all the files necessary to boot the computer except the configuration files.

Some of the files essential for booting the system that the `/boot` directory usually stores are the **kernel** and the **Grub boot loader**.

### `/dev`
The GNU-Linux OS treats hardware devices as if they were a file. These files that represent our hardware devices are stored in the `/dev` directory.

Some of the basic files that we can find in this directory are:
- `cdrom`, which represents our CDROM device.
- `sda`, which represents our sata hard drive.
- `audio`, that represents our sound card.
- `psaux`, representing the PS/2 port.
- `lpx`, which represents our printer.
- `fd0`, which represents our floppy drive.

### `/etc`
The `/etc` directory is a static directory that contains the operating system configuration files.

This directory also contains configuration files to control the operation of various programs.

Some of the configuration files in the `/etc` folder can be replaced or supplemented by configuration files located in our personal `/home` folder.

### `/home`
The `/home` directory is a variable and shareable directory. This directory is intended to house all the personal files of the different users of the operating system except for the root user.

Some of the personal files stored in the /home folder are photographs, office documents, videos, etc.

### `/lib`
The `/lib` directory is a static directory and may be shareable. This directory contains shared libraries that are necessary to start the executables that are stored in the `/bin` and `/sbin` directories.

### `/lost-found` directory
Directory that is created on disk partitions with an ext file system after running tools to restore and recover the operating system such as `fsch`.

If our system has not had any problems, this directory will be completely empty. In the event that there have been problems, this directory will contain files and directories that have been recovered after the operating system crashed.

### `/mnt`
The `/mnt` directory is intended to house the mount points of the different storage devices such as external hard drives, external drive partitions, etc. Typically, non-removable devices.

### `/media`
The function of the `/media` directory is similar to that of the `/mnt` directory. This directory contains the mount points for removable storage media such as USB sticks, CD-ROM drives, floppy drives, etc.

### `/opt`
The content stored in the `/opt` directory is static and shareable. The function of this directory is to store self-contained program that do not come with our operating system, such as Spotify, Google-earth, Google Chrome, Teamviewer, etc.

### `/proc`
The `/proc` directory is a virtual file system. This virtual file system provides us with information about the different processes and applications that are running in our operating system.

### `/root`
The `/root` directory is a non-shareable variable directory. The `/root` directory is the `/home` directory of the system administrator (root user).

### `/srv`
The `/srv` directory is used to store directories and data used by certain servers that we may have installed on our computer.

### `/sys`
Directory that contains information similar to that of the `/proc` directory. Inside this folder we can find structured and hierarchical information about the kernel of our computer, our partitions and file systems, our drivers, etc.

### `/tmp`
The `/tmp` directory is where temporary files and variables are created and stored so that programs can function properly.

### `/usr`
The `/usr` (user system resources) directory is a shared, static directory. This directory is the one that contains the vast majority of programs installed in our operating system. All content stored in the `/usr` folder is accessible to all users and its contents are read-only.

### `/var`
The `/var` directory contains variable and temporary data files such as system records (logs), program records that we have installed in the operating system, spool files, etc.

The main function of the `/var` directory is to detect problems and solve them. It is recommended to place the `/var` directory in its own partition, and if this is not possible, it is advisable to place it outside the root partition.
