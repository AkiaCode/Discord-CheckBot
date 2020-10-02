import discord, json, os
from discord.ext import commands 

if str(json.load(open('./data/setup.json', 'r'))["token"]) == "none":
    print("[setup-bot] 새로운 봇의 토큰을 입력해주세요")
elif str(json.load(open('./data/setup.json', 'r'))["prefix"]) == "none":
    print("[setup-bot] 새로운 봇에 적용할 접두사를 입력해주세요")
else:

    locas = []
    for locale in os.listdir('./locale'):
        locas.append(locale[:-3])

    if not str(json.load(open('./data/setup.json', 'r'))["locale"]) in str(locas):
        print("[setup-bot] 올바르지 않은 언어 파일입니다. 직접 추가하거나 다른 파일을 이용해주세요")
    else:

        client = commands.Bot(command_prefix = "{}".format(json.load(open('./data/setup.json'))["prefix"]))

        @client.event 
        async def on_ready():

            for filename in os.listdir('./src'):
                if filename.endswith('.py'):
                    client.load_extension(f'src.{filename[:-3]}')

            print("[setup-bot] 성공적으로 클라이언트에 접속되었습니다. 이제 명령어를 사용하실 수 있습니다!")
                
        client.run(json.load(open('./data/setup.json', 'r'))["token"])
