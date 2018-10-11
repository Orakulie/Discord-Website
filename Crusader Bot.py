import discord
import asyncio
import requests
import io


c = discord.Client()

@c.event
async def on_ready():
       print("Eingelogt als")
       print(c.user.name)
       print(c.user.id)
       print("--------")
       await start()


async def start():
    await c.wait_until_ready()
    channel = discord.Object(id='442474893561298945')
    #await c.send_message(channel, "IN THE NAME OF GOD, I LIVE AGAIN!")




@c.event
async def on_message(message):
           server = discord.Server()
           await c.change_nickname(server.get_member("442461722012418050"), "Anonym")

           if message.content.lower().startswith("deus?") or message.content.lower().startswith("deus"):
                  response = requests.get("https://i.imgur.com/wV8lMiK.gif", stream=True)

                  await c.send_file(message.channel, io.BytesIO(response.raw.read()), filename='Deus_Vult.gif', content='V U L T!')
           if message.content.lower().startswith("doch"):
                  await c.send_message(message.channel, "OOH!")
           if message.content.lower().startswith("lukas"):
                  await c.send_message(message.channel, "ist ein Spast!")
           if message.content.lower().startswith("jan"):
                  await c.send_message(message.channel, "schnabuliert Kaka.")
           if message.content.lower().startswith("till"):
                  await c.send_message(message.channel, "nein.")
           if message.content.lower().startswith("christoph"):
                  await c.send_message(message.channel, "flext auf anime.")
           if message.content.lower().startswith("arian"):
                  await c.send_message(message.channel, "du meinst toshtosh")
           if message.content.lower().startswith("stirb"):
               await c.send_message(message.author,"Das werd ich mir merken, {0}".format(message.author.name))

           if message.content.lower().startswith("lonely") or message.content.lower().startswith(":sob:"):
                  try:
                         channel = message.author.voice.voice_channel
                         voice = await c.join_voice_channel(channel)
                         player = await voice.create_ytdl_player("https://www.youtube.com/watch?v=X-cfWM0BC_4")
                         player.start()
                  except:
                         await c.send_message(message.channel, "Ich bin behindert :/")

           if message.content.lower().startswith("fresse"):
                try:
                    voice_client = c.voice_client_in(message.server)
                    await voice_client.disconnect()
                except:
                    await c.send_message(message.channel, "Selber")

@c.event
async def on_member_join(member):
       channel1 = member.server.default_channel
       await c.send_message(discord.Object("442474893561298945"), "Willkommen Schlappschwanz, eksdeeeee")



c.run("NDQyNDYxNzIyMDEyNDE4MDUw.Dc_wBw.hI5i4q_6swW_aPfJHeFcV9LQgOU")
