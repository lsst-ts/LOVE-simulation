FROM lsstts/simulation_tests:latest
WORKDIR /home/saluser/repos/ts_sal
RUN source /opt/lsst/software/stack/loadLSST.bash && \
    source /home/saluser/repos/ts_sal/setup.env && \
    make_salpy_libs.py ATDome 
RUN source /opt/lsst/software/stack/loadLSST.bash && \
    source /home/saluser/repos/ts_sal/setup.env && \
    make_salpy_libs.py ATMCS
RUN source /opt/lsst/software/stack/loadLSST.bash && \
    source /home/saluser/repos/ts_sal/setup.env && \
    make_salpy_libs.py ScriptQueue

WORKDIR /usr/src/love
COPY requirements.txt .
RUN source /opt/lsst/software/stack/loadLSST.bash && pip install -r requirements.txt
COPY . .
WORKDIR /home/saluser
ENTRYPOINT ["/usr/src/love/start-daemon.sh"]