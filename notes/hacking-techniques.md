## Path hijacking
Security threat where an attacker modifies the system's search path to execute malicious code instead of the intended
program. Path hijacking can be used to gain unauthorized access to system resources or execute malware on unsuspecting users.
When a user executes a command, the operating system searches for the executable in the directories listed in the PATH variable. The attacker modifies this list to insert their malicious code before the intended program's path so that when the user enters the command, the attacker's malware is executed instead of the actual program. This technique can be used to gain access to sensitive files or data, steal information, or carry out other nefarious activities.

Path hijacking can occur in various ways, including environment variable manipulation, local system modification, and exploitation of vulnerabilities in software applications.