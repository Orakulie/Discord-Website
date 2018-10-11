import discord 
import asyncio
import requests
import io
import datetime
import os
import youtube_dl
import time

c = discord.Client()

@c.event
async def on_ready():
       print("Eingelogt als")
       print(c.user.name)
       print(c.user.id)
       print("--------")
       c.accept_invite("https://discord.gg/5pkNpaY")
       await start()


async def start():
    await c.wait_until_ready()
    channel = discord.Object(id='442474893561298945')
    



@c.event
async def on_message(message):
    text_f = open("Chat.txt","a")
    text_f.write("<div style='background-color:Steelblue;padding: 0px;'>{0}:</div> {1}[{2}]\n".format(message.author.name, message.content,datetime.datetime.now().strftime('%H:%M')))
    text_f.close()
   if message.content.lower().startswith("song"):
        try:
            yturl = message.content[5:]
            channel = message.author.voice.voice_channel
            voice = await c.join_voice_channel(channel)
            player = await voice.create_ytdl_player(yturl)
            player.start()
        except:
            try:
                voice_client = c.voice_client_in(message.server)
                await voice_client.disconnect()
                yturl = message.content[5:]
                channel = message.author.voice.voice_channel
                voice = await c.join_voice_channel(channel)
                player = await voice.create_ytdl_player(yturl)
                player.start()
            except:
                await c.send_message(message.channel, "Ich bin behindert :/")

    if message.content.lower().startswith("psch"):
        try:
            voice_client = c.voice_client_in(message.server)
            await voice_client.disconnect()
        except:
            await c.send_message(message.channel, "Selber")

@c.event
async def on_member_join(member):
       channel1 = member.server.default_channel
       await c.send_message(discord.Object("442474893561298945"), "Hello there!")

async def Nachrichten():
    await c.wait_until_ready()
    
    while not c.is_closed:
        await asyncio.sleep(5)
        try:
            text_f = open("Send.txt","r")
            text = text_f.readline()
            text_f.close()
            await c.send_message(discord.Object("442474893561298945"), "Das Internet sagt: {0}".format(text))
            os.remove("Send.txt")
        except:
            pass
c.loop.create_task(Nachrichten())

c.run("NDQyNDYxNzIyMDEyNDE4MDUw.Dc_wBw.hI5i4q_6swW_aPfJHeFcV9LQgOU")
