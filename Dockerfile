FROM ubuntu:latest
LABEL authors="bulla"

ENTRYPOINT ["top", "-b"]