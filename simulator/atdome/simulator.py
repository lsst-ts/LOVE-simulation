import asyncio
import json
from lsst.ts import salobj


def read_atdome_cscs_from_config(path):
    """ Reads a given config file and returns the list of CSCs to run

    Parameters
    ----------
    path: `string`
        The full path of the config file

    Returns
    -------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print('ATDome   | Reading config file: ', path)
    data = json.load(open(path, 'r'))
    emitters_list = []
    for csc_key, csc_value in data.items():
        if csc_key != 'ATDome':
            continue
        for csc_instance in csc_value:
            if csc_instance['source'] == 'command_sim':
                emitters_list.append((csc_key, csc_instance['index']))
    return emitters_list


async def main(path, sal_base_index):
    """ Runs the ATDome simulator

    Parameters
    ----------
    path: `string`
        The full path of the config file
    sal_base_index: `int`
        The base SAL index, which is summed to every SAL index read from the config file
    """
    print('\nATDome   | **** Starting ATDome command simulator loop *****')
    csc_list = read_atdome_cscs_from_config(path)
    print('ATDome   | List of CSCs to start:', csc_list)

    domain = salobj.Domain()
    for csc in csc_list:
        name = csc[0]
        index = int(csc[1]) + int(sal_base_index)
        print('ATDome   | - Creating remote (CSC, index): (', name, ', ', index, ')')
        r = salobj.Remote(domain=domain, name=name, index=index)

        await r.cmd_start.start(timeout=30)
        await salobj.set_summary_state(r, salobj.State.ENABLED)
        await r.evt_heartbeat.next(flush=True, timeout=5)

        azimuth = 0
        shutter = 'closed'

        loopCount = 0
        while True:
            loopCount += 1
            r.cmd_moveAzimuth.set(azimuth=azimuth)
            azimuth = (azimuth+50) % 360
            if loopCount % 4 == 0.:
                if shutter == 'closed':
                    await r.cmd_openShutter.start()
                else:
                    await r.cmd_closeShutter.start()
            await r.cmd_moveAzimuth.start()
            await asyncio.sleep(10)

if __name__ == '__main__':
    print('***** Running ATDome command simulator as standalone *****')
    asyncio.get_event_loop().run_until_complete(main())
