import discord
from discord.ext import commands
import os
import math
from restore import restore
import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents, case_insenitivity=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    aactivity = discord.Activity(type=discord.ActivityType.listening, name="Paddington Distrack")
    await bot.change_presence(activity=aactivity)

#Create Channel
@bot.command()
async def create(ctx, name, channel: discord.CategoryChannel=None, description=None):
  
  embed=discord.Embed(title="Channel Created", description=f"{name} was made", color=0x7a8ad8)
  embed.set_thumbnail(url="https://en.wikipedia.org/wiki/File:Homemade_marmalade,_England.jpg")
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await ctx.guild.create_text_channel(name=name, category=channel, topic=description)

#Delete Channel
@bot.command()
async def delete(ctx, channel: discord.TextChannel):
  
  embed=discord.Embed(title="Channel Created", description=f"{channel} was deleted", color=0x7a8ad8)
  embed.set_thumbnail(url="https://en.wikipedia.org/wiki/File:Homemade_marmalade,_England.jpg")
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await channel.delete()

#Move Channel Category
@bot.command()
async def mvchannel(ctx, textchannel: discord.TextChannel, channel: discord.CategoryChannel):
  
  embed=discord.Embed(title="Channel Created", description=f"{textchannel} was moved to {channel}", color=0x7a8ad8)
  embed.set_thumbnail(url="https://en.wikipedia.org/wiki/File:Homemade_marmalade,_England.jpg")
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await textchannel.edit(category = channel)
#Move Channel Position
@bot.command()
async def position(ctx, textchannel: discord.TextChannel, *, newpos):
  embed=discord.Embed(title="Channel Created", description=f"{textchannel} was moved to position {newpos}", color=0x7a8ad8)
  embed.set_thumbnail(url="https://en.wikipedia.org/wiki/File:Homemade_marmalade,_England.jpg")
  if ctx.author.guild_permissions.manage_channels:
    newpos = int(newpos)
    math.ceil(newpos)
    if ctx.author.guild_permissions.manage_channels:
            await textchannel.edit(position = newpos)
            await ctx.send(embed=embed)

#Create Voice Channel
@bot.command()
async def vc(ctx, name, channel: discord.CategoryChannel=None):
  
  embed=discord.Embed(title="Channel Created", description=f"Voice Channel {name} was made", color=0x7a8ad8)
  embed.set_thumbnail(url="https://en.wikipedia.org/wiki/File:Homemade_marmalade,_England.jpg")
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await ctx.guild.create_voice_channel(name=name, category=channel)

#Delete Voice Channel
@bot.command()
async def dvc(ctx, channel: discord.VoiceChannel):
  
  embed=discord.Embed(title="Channel Created", description=f"Voice Channel {channel} was deleted", color=0x7a8ad8)
  embed.set_thumbnail(url="https://en.wikipedia.org/wiki/File:Homemade_marmalade,_England.jpg")
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await channel.delete()

#Create Role
@bot.command()
async def role(ctx, RoleName):
  
  embed=discord.Embed(title="Channel Created", description=f"Role {RoleName} was made", color=0x7a8ad8)
  embed.set_thumbnail(url="https://en.wikipedia.org/wiki/File:Homemade_marmalade,_England.jpg")
  if ctx.author.guild_permissions.manage_roles:
    await ctx.send(embed=embed)
    await ctx.guild.create_role(name=RoleName)

#Delete Role
@bot.command()
async def derole(ctx, RoleName: discord.Role):
  
  embed=discord.Embed(title="Channel Created", description=f"Role {RoleName} was deleted", color=0x7a8ad8)
  embed.set_thumbnail(url="https://en.wikipedia.org/wiki/File:Homemade_marmalade,_England.jpg")
  if ctx.author.guild_permissions.manage_roles:
    await ctx.send(embed=embed)
    await ctx.RoleName.delete()

#Add role to someone - no embed
@bot.command(pass_context=True)
async def give(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        await user.add_roles(role)

#Remove role from someone - no embed
@bot.command(pass_context=True)
async def yoinks(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        await user.remove_roles(role)

#Purge messages
@bot.command()
@commands.has_permissions(manage_channels=True)
async def purge(ctx, limit: int):
  await ctx.channel.purge(limit=limit + 1)
    

restore()
bot.run('Your Token')
