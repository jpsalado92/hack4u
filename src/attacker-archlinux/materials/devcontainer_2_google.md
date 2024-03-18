# Devcontainer 2 Internet

How does the traffic between a vscode devcontainer in a Windows machine look like?

In order to answer this question, we will start exploring the actual devcontainer newtork.

## Devcontainer network

Given that we are inside the devcontainers terminal, we can run the following commands:

```bash
# This command will show the ip addresses of the newtork interfaces inside the devcontainer
ip a

# This command will show the routing table of the devcontainer
ip r
```

The output of the first command will show the ip addresses of the network interfaces of the devcontainer. The output of the second command will show the routing table of the devcontainer.

## Internet access

Now, lets see if we can communicate with the internet from the devcontainer. We can do this by running the following command:

```bash
ping google.com
```

## Exploring all the bumps until destination

Now that we know that we can communicate with the internet from the devcontainer, we can start exploring the path that the packets take until they reach the destination.

We can do this by running the following command:

```bash
traceroute google.com
```

This command will show the path that the packets take until they reach the destination.


