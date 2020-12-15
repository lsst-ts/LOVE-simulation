ARG LSSTTS_DEV_VERSION=c0010
FROM lsstts/develop-env:${LSSTTS_DEV_VERSION}
WORKDIR /usr/src/love
COPY simulator/requirements.txt .
RUN source /opt/lsst/software/stack/loadLSST.bash && pip install -r requirements.txt
RUN source /opt/lsst/software/stack/loadLSST.bash \
    && source /home/saluser/.setup_salobj.sh \
    && setup ts_sal -t current \
    && /home/saluser/repos/ts_sal/bin/make_idl_files.py Watcher WeatherStation GenericCamera
COPY simulator ./simulator

WORKDIR /home/saluser
ENTRYPOINT ["/usr/src/love/simulator/start-daemon.sh"]
