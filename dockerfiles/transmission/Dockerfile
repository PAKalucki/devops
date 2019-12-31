FROM linuxserver/transmission:arm32v7-latest

RUN find / -name "config.json" -exec sed -i 's/"rpc-whitelist-enabled": false,/"rpc-whitelist-enabled": true,/g' {} \; && \
    find / -name "config.json" -exec sed -i 's/"rpc-whitelist": "127.0.0.1",/"rpc-whitelist": "proxy",/g' {} \;