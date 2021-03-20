import discord
import random
import asyncio
from discord.ext import commands
import json
import os
import random

os.chdir("C:\\Users\\(주)서홍건축N\\Desktop\\프로그램 ㅋㅋ\\자바스크립트")
client = commands.Bot(command_prefix = '게임봇 ')

token = "ODIyNjI0Mjg0NjY5MjQ3NDg5.YFU-kQ.y6HPujIcvY7dc2J3AO2Lz0DZ6Lw"

@client.event
async def on_ready():
    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('게임봇 1.1.2 by 쌩쌩이')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invaild command used")

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)
    await ctx.send("메세지를 삭제했습니다.")

@client.command()
async def 돈정보(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]

    em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Color.red())
    em.add_field(name = "돈",value=wallet_amt)
    await ctx.send(embed = em)

@client.command()
async def 돈받기(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    await ctx.send("출석체크 완료")

    users[str(user.id)]["wallet"] += 1000

    with open("mainbank.json","w") as f:
        json.dump(users,f)

async def open_account(user):
                       
    users = await get_bank_data()
    
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
    with open("mainbank.json", "w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)
    return users

@client.command()
async def 째려봐(ctx):
    await ctx.message.channel.send("-__-")

@client.command()
async def 안녕(ctx):
    await ctx.message.channel.send("안녕하세요!")

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('삭제할 개수를 정해주세요')

@client.command()
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)
    await ctx.send(f'{member}'"님을 킥 하였습니다.")

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason=reason)
    await ctx.send(f'{member}'"님을 밴 하였습니다.")

#@client.command()
#async def 맴버수(ctx):
    #await ctx.message.channel.send(f'{str(len(member.guild.members))}')

# @client.command()
# async def 쌩쌩이프사(ctx):
#     embed = discord.Embed(title="쌩쌩이의 프사!", description="wow amazing(?)", color=0x00ff00)
#     embed.set_thumbnail(url="https://i.esdrop.com/d/Pi5RiTpMlw.png.sthumb")
#     await ctx.message.channel.send(embed=embed)

@client.command()
async def 도움말(ctx):
    embed = discord.Embed(title = "도움말", description=
    "-clear (삭제할 메시지 수)\n"
    "  적은 숫자만큼 메시지를 삭제합니다(권한 필요)\n"
    "-ping\n"
    "  핑을 확인할 수 있습니다.\n"
    "-kick @킥할 유저\n"
    "  맨션된 유저가 kick됩니다.(권한 필요)\n"
    "-ban @벤할 유저\n"
    "  맨션된 유저가 ban됩니다.(권한 필요)\n"
    "-째려봐\n"
    "  봇이 당신을 째려봅니다. (기분 나쁠수도)"
    "-돈정보\n"
    "  돈을 얼마나 가지고 있는지 확인가능합니다.\n"
    "-돈받기\n"
    "  하루에 한번 1000원을 받을 수 있습니다\n"
    "더 많은 명령어가 생길 예정입니다.."
    , color = 0x00ff00)
    await ctx.message.channel.send(embed=embed)

client.run(token)