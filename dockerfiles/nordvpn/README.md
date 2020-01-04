## NORDVPN Container

Pass "random" to connect to random server or pick server name like "us1722".

docker container run -d \
--restart=always \
--name=nordvpn \
-e user=user@nordvpn.com \
-e password=your_secret_password \
-e protocol=udp
-p 1194:1194/udp \
--cap-add=NET_ADMIN \
--device=/dev/net/tun \
pakalucki/nordvpn:latest \
uk101
