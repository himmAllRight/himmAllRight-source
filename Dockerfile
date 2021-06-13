FROM fedora:latest

ARG default_bind_ip=0.0.0.0
ENV bind_ip=$default_bind_ip

RUN dnf update -y && dnf install -y hugo && dnf clean all

WORKDIR /Data

CMD ["sh", "-c", "hugo serve -F -D --bind $bind_ip -b $bind_ip"]
