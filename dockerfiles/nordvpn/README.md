docker container run -d \
--restart=always \
--name=nordvpn \
-e user= \
-e password= \
-p 1194:1194/udp \
--cap-add=NET_ADMIN \
--device=/dev/net/tun \
pakalucki/nordvpn:latest \
conf.ovpn