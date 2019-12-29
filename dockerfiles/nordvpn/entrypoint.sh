#!/bin/sh
set -e

echo "" > /etc/openvpn/auth
echo $user >> /etc/openvpn/auth
echo $password >> /etc/openvpn/auth

exec "/usr/sbin/openvpn --script-security 3 --auth-user-pass /etc/openvpn/auth ${1}"