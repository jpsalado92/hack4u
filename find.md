Look for files that have SUID set
```
find / -type f -perm -4000
```
Look for files that have SGID set
```
find / -type f -perm -4000
```