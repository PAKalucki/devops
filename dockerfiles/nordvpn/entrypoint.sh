#!/bin/sh
set -e

echo $user >> /etc/openvpn/auth
echo $password >> /etc/openvpn/auth

exec /usr/sbin/openvpn "/etc/openvpn/ovpn_$protocol/${1}"