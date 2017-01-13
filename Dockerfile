FROM ubuntu:14.04

WORKDIR /opt

RUN apt-get update \
    && apt-get -y install python2.7

COPY dist/aflaskapp-*.pex apps/aflaskapp.pex

ENV PEX_SCRIPT gunicorn

EXPOSE 8000

ENTRYPOINT ["apps/aflaskapp.pex", "aflaskapp.app:app"]
CMD ["-b", "127.0.0.1:8000"]
