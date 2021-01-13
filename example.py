"""Example usage of ais-api."""
import asyncio
import aiohttp
from aisapi.ws import AisWebService

AIS_WS_URL = "http://ais-dom.local:8122"


async def get_gate_info_example():
    """Get gate info example."""
    async with aiohttp.ClientSession() as session:
        ais_ws = AisWebService(LOOP, session, AIS_WS_URL)
        ais_answer = await ais_ws.get_gate_info()
        print("AIS answer:", ais_answer)


async def say_it_example():
    """Say text example."""
    async with aiohttp.ClientSession() as session:
        ais_ws = AisWebService(LOOP, session, AIS_WS_URL)
        ais_answer = await ais_ws.say_it("Hello world")
        print("AIS answer:", ais_answer)


async def send_command_example():
    """Send command example."""
    async with aiohttp.ClientSession() as session:
        ais_ws = AisWebService(LOOP, session, AIS_WS_URL)
        command = "playAudio"
        value = "http://n-15-1.dcs.redcdn.pl/sc/o2/Eurozet/live/audio.livx?audio=5"
        ais_answer = await ais_ws.command(command, value)
        print("AIS answer:", ais_answer)


async def get_audio_status_example():
    """Get audio status example."""
    async with aiohttp.ClientSession() as session:
        ais_ws = AisWebService(LOOP, session, AIS_WS_URL)
        ais_answer = await ais_ws.get_audio_status()
        print("AIS answer:", ais_answer)


async def get_audio_type_example():
    """Get media example."""
    async with aiohttp.ClientSession() as session:
        ais_ws = AisWebService(LOOP, session, AIS_WS_URL)
        # media_content_id = "ais_radio"
        # media_content_id = "ais_podcast"
        media_content_id = "ais_audio_books"
        # media_content_id = "ais_tunein"
        ais_answer = await ais_ws.get_audio_type(media_content_id)
        print("AIS answer:", ais_answer)


async def get_audio_name_example():
    """Get media example."""
    async with aiohttp.ClientSession() as session:
        ais_ws = AisWebService(LOOP, session, AIS_WS_URL)
        media_content_id = "ais_radio/Publiczne"
        ais_answer = await ais_ws.get_audio_name(media_content_id)
        print("AIS answer:", ais_answer)


async def send_command_example2():
    """Send command example."""
    async with aiohttp.ClientSession() as session:
        ais_ws = AisWebService(LOOP, session, AIS_WS_URL)
        command = "stopAudio"
        value = True
        ais_answer = await ais_ws.command(command, value)
        print("AIS answer:", ais_answer)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(get_gate_info_example())
LOOP.run_until_complete(say_it_example())
LOOP.run_until_complete(send_command_example())
LOOP.run_until_complete(get_audio_status_example())
LOOP.run_until_complete(get_audio_type_example())
LOOP.run_until_complete(get_audio_name_example())
LOOP.run_until_complete(send_command_example2())
