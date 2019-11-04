import asyncio
from lsst.ts import salobj


async def main_csc(name, index, domain):
    """ Runs the Watcher simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print('\nWatcher      | **** Starting Watcher command simulator loop *****')
    print('Watcher      | - Creating remote (CSC, index): (', name, ', ', index, ')')
    r = salobj.Remote(domain=domain, name=name, index=index)
    try:
        r.cmd_start.set(settingsToApply='default.yaml') 
        await r.cmd_start.start(timeout=30)
        await r.cmd_enable.start(timeout=30)
    except Exception as e:
        print(e)

    while True:
        try:
            await asyncio.sleep(30)
            await r.cmd_disable.start()
        except Exception as e:
            print(e)    
        try:
            await r.cmd_enable.start()
        except Exception as e:
            print(e)


async def main(csc_list):
    """ Runs the Watcher simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print('\nWatcher      | **** Starting Watcher command simulator loop *****')
    domain = salobj.Domain()
    for csc in csc_list:
        name = csc[0]
        index = None
        asyncio.get_event_loop().create_task(main_csc(name, index, domain))

if __name__ == '__main__':
    print('***** Running Watcher command simulator as standalone *****')
    asyncio.get_event_loop().run_forever(main())