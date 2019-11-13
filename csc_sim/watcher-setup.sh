#!/usr/bin/env bash

# Source this file when starting the container to set it up

echo "#"
echo "# Loading LSST Stack"
. /opt/lsst/software/stack/loadLSST.bash
setup lsst_distrib
echo "#"
echo "# Loading sal environment"
. repos/ts_sal/setup.env
echo "#"
echo "# Setting up sal, salobj and scriptqueue"

setup ts_xml -t current
setup ts_sal -t current
setup ts_salobj -t current
setup ts_scriptqueue -t current
setup ts_config_attcs -t current

if [[ $LSST_DDS_IP != *"."* ]]; then
  echo "Unset LSST_DDS_IP"
  unset LSST_DDS_IP
fi

#WRITE CONFIG
cd /home/saluser/repos/ts_config_ocs/Watcher/v1
echo "rules:
- classname: test.ConfiguredSeverities
  configs:
  - severities: [2, 3, 1, 3, 1]
    interval: 5
    name: Rule1
  - severities: [2, 1, 2, 1, 2, 1]
    interval: 3
    name: Rule2
  - severities: [3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]
    interval: 3
    name: Rule3" > default.yaml

#RUN WATCHER
cd /home/saluser/repos
git clone https://github.com/lsst-ts/ts_watcher.git
cd ts_watcher
setup -r .
scons install declare
python bin/run_watcher.py