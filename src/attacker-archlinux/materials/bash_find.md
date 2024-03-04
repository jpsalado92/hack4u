# Bash find command

```bash
find /
```

Look for a file recursively from root

```bash
find / -name FILENAME
```

Check attributes with xargs and ls -l

```bash
find / -name FILENAME | xargs ls -l
```

Check for SUID privileges

```bash
find / -perm -4000 2>/dev/devnull
```

Check only for directories or files with `-type`

```bash
find / -name home -type d
find / -name home -type f
```

Check for everything that is writable or executable

```bash
find / -writable
find / -executable
```

Check for stuff that follows a pattern

```bash
find / -name a\*
```
