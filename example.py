"""Example usage of ais-api."""
import asyncio
import aiohttp
from ais-api.ws import AisWebService

API_KEY = 'dom-demo'
AIS_WS_URL = 'http://ais-dom.local:8122'


async def say_it_example():
    """Say text example."""
    async with aiohttp.ClientSession() as session:
        ais_ws = AisWebService(LOOP, session, API_KEY, AIS_WS_URL)
        ais_answer = await ais_ws.say_it("Hello world")
        print("AIS answer:", ais_answer)


async def send_command_example():
    """Send command example."""
    async with aiohttp.ClientSession() as session:
        ais_ws = AisWebService(LOOP, session, API_KEY, AIS_WS_URL)
        command = "playAudio"
        value = "http://n-15-1.dcs.redcdn.pl/sc/o2/Eurozet/live/audio.livx?audio=5"
        ais_answer = await ais_ws.command(command, value)
        print("AIS answer:", ais_answer)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(say_it_example())
LOOP.run_until_complete(send_command_example())
