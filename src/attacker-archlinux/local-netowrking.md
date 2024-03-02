# LAN Networking

## Private IPs

The Internet Assigned Numbers Authority (IANA) has reserved certain IP address ranges for private networks.
These ranges are not routable on the public internet, meaning they are reserved for use
within private networks like home, school, or office networks.

The ranges are:

- `10.0.0.0` to `10.255.255.255`
- `172.16.0.0` to `172.31.255.255`
- `192.168.0.0` to `192.168.255.255`

## Grab current LAN IP

```bash
ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}'
```

## Grab current subnet mask

```bash
ifconfig | grep "inet " | grep -v



