import asyncio
from lsst.ts import salobj


async def main_csc(name, index, domain):
    """Runs the WeatherStation simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print(
        "\nWeatherStation      | **** Starting WeatherStation command simulator loop *****"
    )
    print(
        "WeatherStation      | - Creating remote (CSC, index): (",
        name,
        ", ",
        index,
        ")",
    )
    r = salobj.Remote(domain=domain, name=name, index=index)
    await r.start_task
    evt = await r.evt_summaryState.aget()
    state = salobj.State(evt.summaryState)
    if state == salobj.State.STANDBY:
        await r.cmd_start.start(timeout=30)
        await r.cmd_enable.start(timeout=30)
    await r.evt_heartbeat.next(flush=True)


async def main(csc_list, domain):
    """Runs the WeatherStation simulator

    Parameters
    ----------
    csc_list: `[()]`
        The list of CSCs to run as a tuple with the CSC name and index
    """
    print(
        "\nWeatherStation      | **** Starting WeatherStation command simulator loop *****"
    )
    for csc in csc_list:
        name = csc[0]
        index = csc[1]
        asyncio.get_event_loop().create_task(main_csc(name, index, domain))
