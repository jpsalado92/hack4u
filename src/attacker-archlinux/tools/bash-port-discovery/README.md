# Bash Open-Port Discovery

This script is a simple port scanner written in Bash. It scans all TCP ports on the localhost (`127.0.0.1`) from `1` to `65535` and prints out the open ones.

## Usage

The main part of the script is a loop that goes through all possible TCP port numbers (from `1` to `65535`).

For each port, it tries to send an empty string to the port on the `localhost` using a redirection to a special file in `/dev/tcp/127.0.0.1/$port`. If this succeeds (i.e., the port is open), it prints a message indicating that the port is open.

The `2>/dev/null` part suppresses error messages (which occur when a port is closed).

The `&` at the end of the line makes the command run in the background, so the script can move on to the next port without waiting for the current one to finish. The `wait` command is used after the loop to wait for all background jobs to finish.

## About `/dev/tcp/`

The `/dev/tcp/` directory is a special directory that Bash uses to create a TCP connection to a remote server. It is not a real directory, but a feature of Bash. The syntax is:

```bash
/dev/tcp/host/port
```
