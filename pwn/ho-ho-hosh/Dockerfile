FROM alpine:3.15

RUN apk add --no-cache openssh python3 && rm -rf /tmp/* /var/cache/apk/*

ADD ./src /home/hohohosh

RUN adduser -s /home/hohohosh/run.sh -k /dev/null -H -D hohohosh \
    && echo "hohohosh:montrehack" | chpasswd \
    && echo -e "Port 47422\nProtocol 2\nMaxSessions 100\nPasswordAuthentication yes\nPubkeyAuthentication no\nPermitRootLogin no\nClientAliveInterval 180\nAllowAgentForwarding no\nAllowStreamLocalForwarding no\nGatewayPorts no\nPrintMotd no\nAllowUsers hohohosh\nSubsystem sftp /bin/false\nPermitTunnel no" > /etc/ssh/sshd_config \
    && chown -R hohohosh:hohohosh /home/hohohosh

EXPOSE 47422
ENTRYPOINT ["/home/hohohosh/entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D"]
