FROM alpine:3.7

ENV username user
ENV password pass

EXPOSE 1194/udp

RUN apk add --update openvpn iptables openvpn-auth-pam wget unzip && \
    wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip && \
    unzip ovpn.zip -d /etc/openvpn && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/* ovpn.zip

COPY entrypoint.sh /usr/local/bin/

ENTRYPOINT ["entrypoint.sh"]
CMD ["--help"]