import discord
from discord.ext import commands
import asyncio
import requests
import os
from bs4 import BeautifulSoup as bs
client = discord.Client()
bot = commands.Bot(command_prefix='T')

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n', data)

@bot.event
async def on_ready():
    print("로그인")
    print(bot.user.name)
    print(bot.user.id)
    print("------------------")
    await bot.change_presence(game=discord.Game(name="서버주소: RPSV.kr", type=1))
@bot.event
async def on_member_join(member):
    role = ""
    for k in member.server.roles:
        if k.name == "RPSV":
            role = k
            break
    await bot.add_roles(member, role)
    embed = discord.Embed(title="RPSV 관리자", description="알피서버 사전예약 이벤트중! 지금 당장 신청하자\n\n1.5.2 최강자를 가려라 약한사람은 필요없다 -RP-\n\n1주차 최강자전 보상 : 서버아이템 ( 미정 )\n2주차 최강자전 보상 : 서버아이템 ( 미정 )+ 문화상품권 2만원\n3주차 최강자전 보상 : 서버아이템 ( 미정 )\n4주차 최강자전 보상 : 문화상품권 5만원+서버아이템 ( 미정 )", color=0x00ff00)
    await bot.send_message(bot.get_channel("557527899993800716"), embed=embed)
@bot.event
async def on_message(message):
    if message.content.startswith("공지띄우기1"):
        await bot.delete_message(message)
        embed = discord.Embed(title="RPSV 관리자",
                              description="알피서버 사전예약 이벤트중! 지금 당장 신청하자\n\n1.5.2 최강자를 가려라 약한사람은 필요없다 -RP-\n\n1주차 최강자전 보상 : 서버아이템 ( 미정 )\n2주차 최강자전 보상 : 서버아이템 ( 미정 )\n3주차 최강자전 보상 : 서버아이템 ( 미정 )\n4주차 최강자전 보상 : 문화상품권 5만원",
                              color=0x00ff00)
        await bot.send_message(message.channel, embed=embed)

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
