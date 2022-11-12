import discord
from discord.ext import commands

# -- sum configs
client = commands.Bot(
  command_prefix = '.' # you can change the prefix to your liking
  intents = discord.Intents.all()
)

# -- events 
@client.event
async def on_ready(): # when bot is online
  print('Connected to') # it will say 'Connected to (bot name here)'
  print(bot.user)

# -- commands

# - ping command example
@client.command()
async def ping(ctx):
  # bot sending the message
  await ctx.reply('Pong! {0}'.format(round(client.latency, 1)))

# - embed example
@client.command()
async def embed(ctx):
  embed = discord.Embed(
    color = 0x000000,
    title = 'Embed Title!',
    description = 'Embed Description'
)
  # adding fields 
  # Field is kinda similar to title and description, for me at least.
  embed.add_fields(name = 'Field Name', value = 'Field Value / Desc')
  # bot sending the embed
  await ctx.reply(embed = embed)

# -- running the bot
client.run('BOT_TOKEN')
# replace BOT_TOKEN with your bots token
  
