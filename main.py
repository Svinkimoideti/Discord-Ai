
import discord

from discord.ext import commands

from model import AI

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event

async def on_ready():
  
    print(f'Все работает')

@bot.command()
async def image(ctx):
    if len(ctx.message.attachments) > 0:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./images/{file_name}')
            await ctx.send('Я украл и сохранил твою картинку))')
            class_name = AI(f'./images/{file_name}')
            await ctx.send (class_name)
    else:
        await ctx.send('А где фото?((')

bot.run("")
