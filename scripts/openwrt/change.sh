#!/bin/sh
set -e

echo "Setting $1"
uci set openvpn.nordvpn.config="$1"
uci commit

echo "Restarting openvpn"
/etc/init.d/openvpn stop
/etc/init.d/openvpn start

exit $?