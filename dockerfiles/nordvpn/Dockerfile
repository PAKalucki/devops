FROM arm64v8/alpine:3.7

RUN apk add --update openvpn iptables openvpn-auth-pam wget unzip && \
    wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip && \
    unzip ovpn.zip -d /etc/openvpn && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/* ovpn.zip