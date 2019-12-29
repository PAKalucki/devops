docker run -d --restart=always \
--name=nordvpn \
-p 1194:1194/udp \
--cap-add=NET_ADMIN \
pakalucki/nordvpn:latest /etc/openvpn/ovpn_udp/pl81.nordvpn.com.udp.ovpn