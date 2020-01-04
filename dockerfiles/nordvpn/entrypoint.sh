#!/bin/sh
set -e

echo ${user} >> /etc/openvpn/auth
echo ${password} >> /etc/openvpn/auth

if [[ ${1} =~ "random" ]]
then 
  server = $(ls /etc/openvpn/ovpn_${protocol} | shuf -n 1)
  exec /usr/sbin/openvpn "/etc/openvpn/ovpn_${protocol}/${server}"
else
  exec /usr/sbin/openvpn "/etc/openvpn/ovpn_${protocol}/${1}.nordvpn.com.${protocol}.ovpn"
fi