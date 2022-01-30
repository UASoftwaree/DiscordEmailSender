import os
import smtplib
import discord
from discord.ext import commands
import json

user = "" # Your Email
password = "" # Your Email Password
token = "" # Discord Bot Token
targetEmail = {"", ""} # Target / Targets Email Here


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user, password)

bot = commands.Bot(command_prefix="!")

@bot.command()
async def fb(ctx, * ,message=None):

  server.sendmail(user,
    targetEmail,
    message
  )

  await ctx.send("Email Sent")

bot.run(token)