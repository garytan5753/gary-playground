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

### Ping
Ping is a network diagnostic tool used to test **reachability** of a host on an IP network and to measure **round-trip time (RTT)** for messages sent from the source to a destination.

- Ping send **ICMP Echo Request** packets to destination
- The destination replies with **ICMP Echo Reply**
- Calculates Packet Loss, Round-trip time (RTT), Jitter (in some advanced tools)
- It used a protocol call **ICMP (Internet Control Message Protocol)** - Layer 3 
- `ping` is ideal for basic connectivity tests, but does not show path.

        ping google.com
        PING google.com (142.250.72.14): 56 data bytes
        64 bytes from 142.250.72.14: icmp_seq=0 ttl=117 time=23.9 ms
        64 bytes from 142.250.72.14: icmp_seq=1 ttl=117 time=24.1 ms
        --- google.com ping statistics ---
        2 packets transmitted, 2 packets received, 0.0% packet loss

### Traceroute / Tracert
Maps the path that packets take from the source to a destination host across an IP network, identifying each hop (router) on the way. 

- Sends packets with increasing **TTL (Time To Live)** values.
- Each router decreases TTL by `1`. When TTL hits `0`, the router replies with 
- **Round-trip time (RTT)** is the amount of time it takes for data to get to and from a certain point on a network.  
**ICMP Time Exceeded**
- Logs the address and time of each hop
- Protocols used;  
**Linux/Unix** usually send **UDP** packets to high-numbered ports (33434+)
**Windows** uses **ICMP Echo Requests** (like ping) and replies come as **ICMP Time Exceeded** messages.

        traceroute google.com
        1  192.168.1.1 (192.168.1.1)  1.000 ms  0.800 ms  0.750 ms
        2  10.0.0.1 (10.0.0.1)        2.300 ms  2.100 ms  2.000 ms
        3  203.116.1.1                10.200 ms 10.300 ms 10.100 ms


- If there are lines with `***` represent hops from which packets were not returned; this can happen when routers are configured to ignore traceroute packets.
- `traceroute` helps to pinpoint which hop is causing delay or failure

### My Tracecorute (MTR)
**MTR** is a dynamic network diagnostics tool that combines **ping** and **traceroute**. 

- A tool to diagnose problems in a network path. 
- To understand the path IP packets are taking from one computer (source IP address) to another (destination IP address).
- Shows constantly updating information about the latency and packet loss along the orute to the destination. 
- Allows to see what's happening along the network path in real-time.
- MTR can use **ICMP** or **UDP** for outgoing packets but relies on **ICMP** for return
- Instead of using **ICMP** packets, use **TCP (TCP MTR)**.
- Or use **UDP (UDP MTR)** instead of **ICMP**. This can be used to circumvent routers that are blocking **ICMP** packet, of for the purpose of testing a specific port.

        mtr google.com
        Host              Loss%   Snt   Last   Avg  Best  Wrst StDev
        1. router.local     0.0%   10    0.5    0.6   0.5   0.7   0.1
        2. 10.0.0.1         0.0%   10    2.3    2.2   2.0   2.5   0.2
        3. 203.116.1.1      0.0%   10   10.1   10.3   9.9  10.7   0.3

- Useful for troubleshooting intermittent issues

### Summary Comparison Table

| Tool         | Purpose                     | Protocol Used           | Key Benefit                          |
|--------------|-----------------------------|--------------------------|---------------------------------------|
| `ping`       | Test basic connectivity     | ICMP                     | Simple and fast RTT & loss check      |
| `traceroute` | Map path (hops) to host     | UDP (Linux), ICMP (Win) | Identifies hop-by-hop route           |
| `mtr`        | Dynamic traceroute + ping   | ICMP (default)           | Live stats on latency & packet loss   |

### Telnet

- For remote management & port connectivity testing
- `telnet` only uses **TCP** and does not support **UDP**
- Default port - **23** but you can test any **TCP port** using the Telnet client

        telnet smtp.gmail.com 587

