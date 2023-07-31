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
  
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await ctx.guild.create_text_channel(name=name, category=channel, topic=description)

#Delete Channel
@bot.command()
async def delete(ctx, channel: discord.TextChannel):
  
  embed=discord.Embed(title="Channel Created", description=f"{channel} was deleted", color=0x7a8ad8)
  
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await channel.delete()
    
#Create Category
@bot.command()
async def category(ctx, CategoryName):
  
  embed=discord.Embed(title="Channel Created", description=f"Category {CategoryName} was made", color=0x7a8ad8)
  
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await ctx.guild.create_category(name=CategoryName)

#Delete Category
@bot.command()
async def decategory(ctx, category: discord.CategoryChannel):
  
  embed=discord.Embed(title="Channel Created", description=f"Category {category} was deleted", color=0x7a8ad8)
  
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await category.delete()
    
#Change Description
@bot.command()
async def describe(ctx, textchannel: discord.TextChannel, *, newDesc):
  
  embed=discord.Embed(title="Channel Created", description=f"{textchannel} was updated", color=0x7a8ad8)
  
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await textchannel.edit(topic=newDesc)

#Clear Description
@bot.command()
async def cleardesc(ctx, textchannel: discord.TextChannel):
  
  embed=discord.Embed(title="Channel Created", description=f"{textchannel} was updated", color=0x7a8ad8)
  
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await textchannel.edit(topic=None)
    
#Rename Channel
@bot.command()
async def rename(ctx, channel: discord.TextChannel, newname):
  
  embed=discord.Embed(title="Channel Created", description=f"{channel} was renamed to {newname}", color=0x7a8ad8)
  
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await channel.edit(name=newname)

#Move Channel Category
@bot.command()
async def mvchannel(ctx, textchannel: discord.TextChannel, channel: discord.CategoryChannel):
  
  embed=discord.Embed(title="Channel Created", description=f"{textchannel} was moved to {channel}", color=0x7a8ad8)
  
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await textchannel.edit(category = channel)
#Move Channel Position
@bot.command()
async def position(ctx, textchannel: discord.TextChannel, *, newpos):
  embed=discord.Embed(title="Channel Created", description=f"{textchannel} was moved to position {newpos}", color=0x7a8ad8)
  
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
  
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await ctx.guild.create_voice_channel(name=name, category=channel)

#Delete Voice Channel
@bot.command()
async def dvc(ctx, channel: discord.VoiceChannel):
  
  embed=discord.Embed(title="Channel Created", description=f"Voice Channel {channel} was deleted", color=0x7a8ad8)
  
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=embed)
    await channel.delete()

#Create Role
@bot.command()
async def role(ctx, RoleName):
  
  embed=discord.Embed(title="Channel Created", description=f"Role {RoleName} was made", color=0x7a8ad8)
  
  if ctx.author.guild_permissions.manage_roles:
    await ctx.send(embed=embed)
    await ctx.guild.create_role(name=RoleName)

#Delete Role
@bot.command()
async def derole(ctx, RoleName: discord.Role):
  
  embed=discord.Embed(title="Channel Created", description=f"Role {RoleName} was deleted", color=0x7a8ad8)
  
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

#See what people are saying (Stalker???)
'''
@bot.event
async def on_message(message: discord.Message):
    if message.guild is None and not message.author.bot:
        #channel = client.get_channel('YOUR CHANNEL ID')
        content = message.content
        author = message.author.name

        await channel.send(f"{author}  ({message.author.id})\n\n{content}")

    print(
        message.author, ':', message.content, '(', message.author.id, ')'
    )

    await bot.process_commands(message)
    '''



#User Info
@bot.command()
async def info(ctx, everyone: discord.User):
    embed=discord.Embed(title=f'{everyone}',description=f"ID: {everyone.id}\nDate Account Created: {everyone.created_at}", color=0xf5c211)
    embed.set_thumbnail(url=everyone.avatar)
    await ctx.send(embed=embed)
  


restore()
bot.run('Your Token')
