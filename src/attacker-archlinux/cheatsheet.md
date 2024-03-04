# Cheatsheet

## Useful bash commands

### Process monitoring with `ps -faux`

The `ps -faux` command in Bash is used to display information about currently running processes in a detailed format. Here's what each option does:

- `ps`: This is the command for "process status".
- `-f`: This option stands for "full format listing", which includes additional details like user ID, parent process ID, start time, etc.
- `-a`: This option stands for "all", which includes processes from all users.
- `-u`: This option stands for "user format", which includes additional user-specific details like CPU usage, start time, etc.
- `-x`: This option includes processes not attached to a terminal.

So, ps -faux will display a comprehensive list of all processes, with a lot of detail about each one.

```bash
$ ps -faux

USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         263  0.3  0.1 610740 60492 ?        Ssl  09:44   0:00 /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/node -e  ????const net = require('net'); ????const fs 
root         234  0.2  0.1 612788 62972 ?        Ssl  09:44   0:00 /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/node -e  ????const net = require('net'); ????const fs 
root         170  0.0  0.0   4932  3488 ?        Ss   09:44   0:00 sh /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/bin/code-server --log debug --force-disable-user-en
root         184  3.0  0.2 963532 97204 ?        Sl   09:44   0:03  \_ /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/node /root/.vscode-server/bin/019f4d1419fbc8219a18
root         256  0.7  0.1 659640 60928 ?        Sl   09:44   0:00      \_ /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/node /root/.vscode-server/bin/019f4d1419fbc821
root         443  0.0  0.0   5328  4408 pts/0    Ss+  09:45   0:00      |   \_ /bin/bash --init-file /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/out/vs/workbench/con
root         849  0.0  0.0   5328  4640 pts/1    Ss   09:45   0:00      |   \_ /bin/bash --init-file /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/out/vs/workbench/con
root        3031  0.0  0.0   9884  4900 pts/1    R+   09:46   0:00      |       \_ ps -faux
root         289  0.6  0.1 916396 54740 ?        Sl   09:44   0:00      \_ /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/node /root/.vscode-server/bin/019f4d1419fbc821
root         301 11.7  1.3 22823168 424248 ?     Sl   09:44   0:12      \_ /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/node --dns-result-order=ipv4first /root/.vscod
root         395  0.1  0.1 607948 56936 ?        Sl   09:44   0:00          \_ /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/node /root/.vscode-server/bin/019f4d1419fb
root         629  2.1  0.5 948912 174412 ?       Sl   09:45   0:02          \_ /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/node /root/.vscode-server/extensions/ms-py
root         160  0.0  0.0   5232  3924 ?        Ss   09:44   0:00 /bin/sh
root         177  0.0  0.1 634132 47476 ?        Sl   09:44   0:00  \_ /root/.vscode-server/bin/019f4d1419fbc8219a181fab7892ebccf7ee29a2/node /tmp/vscode-remote-containers-server-ebc51706
root          26  0.0  0.0   4932  3608 ?        Ss   09:44   0:00 /bin/sh
root          20  0.0  0.0   4932  2492 ?        Ss   09:44   0:00 /bin/sh
root           1  0.0  0.0   3024  1776 ?        Ss   09:44   0:00 sleep infinity
```

### Command monitoring with `ps -eo command`

The `ps -eo command` command in Bash is used to display the commands that generated all the currently running processes. Here's what each option does:

`ps`: This is the command for "process status".
`-e:` This option stands for "every process", which includes processes from all users.
`-o` command: This option stands for "output format", where command specifies that the command line associated with each process should be included in the output.

### See open TCP ports with `ss -nltp`

The `ss -nltp` command is used in Linux to display network information.

Here's what each option means:

- `ss` stands for "Socket Statistics".
- `n`: Show numerical addresses instead of trying to determine symbolic host, port or user names.
- `l`: Display only listening sockets (which are normally the ones you're interested in if you're looking at a server).
- `t`: Display TCP sockets.
- `p`: Show the process using the socket.

So, ss -nltp will display all listening TCP sockets along with the process that's using each one.

```bash
$ ss -nltp

State              Recv-Q             Send-Q                           Local Address:Port                            Peer Address:Port             Process                                     
LISTEN             0                  4096                                127.0.0.11:45431                                0.0.0.0:*                                                            
LISTEN             0                  511                                  127.0.0.1:42493                                0.0.0.0:*                 users:(("node",pid=301,fd=41))             
LISTEN             0                  511                                  127.0.0.1:42977                                0.0.0.0:*                 users:(("node",pid=184,fd=19))
```

### See open TCP ports with `cat /proc/net/tcp`

The `cat /proc/net/tcp` command in Linux displays detailed information about all the TCP sockets currently in use by the system.

The `/proc/net/tcp` file holds a table of TCP sockets. When you cat this file, you're reading this table. Each line represents a single socket and contains a lot of information about its state, including the local and remote address and port, the current state of the socket, and more.

It's important to note that the IP addresses are displayed in hexadecimal format and the endianness is in host order, which can make them difficult to read.
