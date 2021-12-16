FROM debian:latest
RUN apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade && apt-get -y install xinetd && apt-get clean
RUN useradd -s/bin/bash -m alf
COPY chal.sh /home/alf/chal.sh
COPY xinetd.conf /etc/xinetd.d/alf
COPY flag.txt /flag
RUN chmod 0555 /home/alf/chal.sh

CMD ["/usr/sbin/xinetd", "-dontfork"]
