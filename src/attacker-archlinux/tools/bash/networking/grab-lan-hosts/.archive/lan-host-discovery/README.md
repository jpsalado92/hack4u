# Bash Active-Host Discovery

This is a Bash script used to scan a local network for active hosts.

## Usage

The main part of the script is a loop that goes from `1` to `254`. For each number i in this
range, it runs a command that pings the IP address `192.168.1.i`.

The `timeout 1` command ensures that the ping command doesn't hang if there's no response.

The `&>/dev/null` part discards the standard output and standard error of the ping command.

If the ping command succeeds (which means that there's a host at that IP address), it prints
a message saying that the host is active.

The `&` at the end of the ping command runs the command in the background, which allows the script
to ping multiple IP addresses in parallel. The wait command at the end of the script waits for all
background jobs to finish before exiting the script.
