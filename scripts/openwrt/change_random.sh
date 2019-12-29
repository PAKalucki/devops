#!/bin/bash
#script assumes you are using *.ovpn configuration files not .conf
set -e

echo "Pick random configuration"
server=$(ls /etc/openvpn/*.ovpn | shuf -n 1)

echo "Setting $server"
uci set openvpn.nordvpn.config="$server"
uci commit

echo "Restarting openvpn"
/etc/init.d/openvpn stop
/etc/init.d/openvpn start

exit 0