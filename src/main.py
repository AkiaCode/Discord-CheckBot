import discord, time, json, datetime 

from discord.ext import commands 

class MainClient(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.locale = json.load(open(f'./locale/{locale}.json', 'r', encoding="UTF-8"))

    @commands.command(aliases=["출첵", "attendancecheck"])
    async def check(self, ctx, menu=None):

        if menu == None:

            times = f"{datetime.datetime.today().year}-{datetime.datetime.today().month}-{datetime.datetime.today().day}"

            ply = json.load(open('./data/ply.json', 'r'))
            try:
                if ply[f"{times}"][f"{ctx.author.id}"]:
                    await ctx.send(str(self.locale["OkayCheck"]).replace("$", f"{ctx.author.mention}"))
                else:
                    ply = dict(ply)
                    ply[f"{times}"] += {f"{ctx.author.id}": f"{time.time()}"}
                    json.dump(ply, open('./data/ply.json', 'w'), ensure_ascii=False, indent="\t")
                    await ctx.send(str(self.locale["NotCheck"]).replace("$", f"{ctx.author.mention}"))
            except:
                ply = dict(ply)
                ply[f"{times}"] = {f"{ctx.author.id}": f"{time.time()}"}
                json.dump(ply, open('./data/ply.json', 'w'), ensure_ascii=False, indent="\t")
                await ctx.send(str(self.locale["NotCheck"]).replace("$", f"{ctx.author.mention}"))

        elif menu == "목록" or menu == "list":

            ply = json.load(open('./data/ply.json', 'r'))
            plylist = ""
            plyround = 0

            for plys in ply:
                for yer in ply[f"{plys}"]:
                    if str(yer) == str(ctx.author.id):

                        plyround += 1

                        if plylist == "":
                            plylist = "{}. 출석한 날: {}".format(plyround, plys)
                        else:
                            plylist += "\n{}. 출석한 날: {}".format(plyround, plys)

            if plylist == "":
                plylist = str(self.locale["NotList"])

            await ctx.send("```\n{}```".format(plylist))

def setup(client):
    client.add_cog(MainClient(client))
