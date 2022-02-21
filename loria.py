import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="!")

async def on_ready():
    print(f'目前登入身份：{bot.user}')

@bot.command()
async def 電話簿(ctx):
    await ctx.send('瑪蒂亞塔分機：123\n儡寂娜塔分機：456\n伊姆塔分機：789\n貝魯蘭塔分機：333\n艾斯朋塔分機：666') 

#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#    if message.content == '':
#        await message.channel.send('')    
 


bot.run("OTM2MjEwMTc4MzcyNjk4MTcy.YfJ3rA.05HHOlFV0xCZaCfxx1QaadQu9QE") 