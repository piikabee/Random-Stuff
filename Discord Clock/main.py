import discord
import asyncio
import datetime

client = discord.Client()

distoken = "https://discord.com/developers/applications/733414028361072670/bot"

# These must all be Voice Channels
timechannel = 725417791355617341

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    while True:
        now = datetime.datetime.now()
        await client.get_channel(timechannel).edit(name=f"{now.hour}:{now.minute} (2:17 AM)") # The channel gets changed here
        await asyncio.sleep(60)


client.run(distoken)
