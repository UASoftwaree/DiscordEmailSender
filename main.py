import os
import smtplib
import discord
from discord.ext import commands
import json

user = os.environ['user'] # Email
password = os.environ['password'] # Password
token = os.environ['token'] # Discord Token
email = "" # Target Email Here


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user, password)
bot = commands.Bot(command_prefix="!")



@bot.command()
async def say(ctx, message=None):
  await ctx.send(message)

@bot.command()
async def feedback(ctx, * ,message=None):

  server.sendmail(user,
    email,
    message
  )

  await ctx.send("Email Sent")

bot.run(token)