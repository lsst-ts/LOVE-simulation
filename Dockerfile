FROM lsstts/develop-env:20190705_sal3.10.0_salobj

WORKDIR /usr/src/love
COPY simulator/requirements.txt .
RUN source /opt/lsst/software/stack/loadLSST.bash && pip install -r requirements.txt
COPY simulator ./simulator
COPY config ./config

WORKDIR /home/saluser
ENTRYPOINT ["/usr/src/love/simulator/start-daemon.sh"]
