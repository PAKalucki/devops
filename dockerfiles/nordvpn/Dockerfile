FROM alpine:3.7

ENV username user
ENV password pass
ENV protocol udp

EXPOSE 1194/udp

RUN apk add --update openvpn iptables openvpn-auth-pam wget unzip && \
    wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip && \
    unzip ovpn.zip -d /etc/openvpn && \
    sed -i 's/auth-user-pass/auth-user-pass \/etc\/openvpn\/auth/g' /etc/openvpn/ovpn_udp/*.ovpn && \
    sed -i 's/auth-user-pass/auth-user-pass \/etc\/openvpn\/auth/g' /etc/openvpn/ovpn_tcp/*.ovpn && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/* ovpn.zip

COPY entrypoint.sh /usr/local/bin/

ENTRYPOINT ["entrypoint.sh"]
CMD ["--help"]