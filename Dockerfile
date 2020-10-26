FROM python:3.5
LABEL git_repo=https://github.com/herochang/test

COPY mac_lookup.py /tmp/mac_lookup/
COPY docker_helper.sh /tmp/docker_helper.sh

ARG MAC_ADDRESS_IO_API_KEY
ENV MAC_ADDRESS_IO_API_KEY ${MAC_ADDRESS_IO_API_KEY}

ENV PATH $PATH:/tmp/mac_lookup/

WORKDIR /tmp/mac_lookup/
CMD [ "/bin/sh", "/tmp/docker_helper.sh" ]
