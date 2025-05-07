# Network Basics

### View available intefaces on Linux host
`ip link`

### Assign IP address to network interface/device
`ip addr add 192.168.1.10/24 dev etho`

### Add IP route

Check current routing table  
`route`

`ip route addd 192.168.2.0/24 via 192.168.1.1`

### Add default route
`ip route add default via 8.8.8.8`

### Enable IP Forwarding in Linux

Check if is enabled  
`cat /proc/sys/net/ipv4/ip_forward`  
*If output is `0`, packet forwarding is disabled*

Enable it temporary;  
`echo 1 > /proc/sys/net/ipv4/ip_forward`  
*To enable permanent IP forwarding, edit it at `/etc/sysctl/conf` file*

### Networking Commands Summary Table

| **Command**                                           | **Description**                                                                                      |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `ip link`                                              | List and modify network interfaces on the host.                                                      |
| `ip addr`                                              | Display the IP addresses assigned to interfaces.                                                     |
| `ip addr add <IP>/<prefix> dev <interface>`            | Assign an IP address to an interface (temporary unless added to config).                              |
| `ip route` or `route`                                  | View the current routing table.                                                                      |
| `ip route add <network>/<prefix> via <gateway>`        | Add entries to the routing table.                                                                    |
| `cat /proc/sys/net/ipv4/ip_forward`                    | Check if IP forwarding is enabled (returns 0 = off, 1 = on).                                         |
| `echo 1 > /proc/sys/net/ipv4/ip_forward`               | Temporarily enable IP packet forwarding (modify `/etc/sysctl.conf` for a permanent change).          |
