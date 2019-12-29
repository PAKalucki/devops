#!/bin/sh

address=$(ifconfig tun0 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1)
gateway="${address%.*}.1"
echo $gateway

/sbin/ip route del 128.0.0.0/1 via $gateway
/sbin/ip route del 0.0.0.0/1 via $gateway
/sbin/ip rule add from 192.168.3.0/24 table vpn
/sbin/ip rule add to 192.168.3.0/24 table vpn
/sbin/ip route add table vpn default dev tun0
/sbin/ip route add 192.168.3.0/24 dev br-lan2 src 192.168.3.1 table vpn