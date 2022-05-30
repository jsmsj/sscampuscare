import discord
from discord.ext import commands
import funcs as fn
import re
import secret

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=["ss "],intents=intents) # ,help_command=None

@bot.event
async def on_ready():
    print("ready")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency,3)}ms")

@bot.group(invoke_without_command = True)
@commands.guild_only()
async def search(ctx):
    await ctx.send(embed=fn.give_help("search"))

@search.command()
@commands.guild_only()
async def admn(ctx,text=None):
    if not text: return await ctx.send("Admission Number Not Found, Example Usage : `ss search admn 1234`")
    pattern = re.compile(r"(^s|p|S|P)?(\d+)")
    matches = pattern.finditer(text)
    mat_ls = []
    for mat in matches:
        mat_ls.append(mat)
    try:
        match = mat_ls[0]
    except:
        return await ctx.send(f"Admission Number Not Found in {text}")
    ls = []
    try:
        g1 = match.group(1)
        try:
            ls.append(int(g1))
        except:
            ls.append(g1)
    except:
        pass
    try:
        g2 = match.group(2)
        try:
            ls.append(int(g2))
        except:
            ls.append(g2)
    except:
        pass
    final = await fn.give_details_from_admn(ls)
    if final[1].description == "Admission Number Not Found":
        await ctx.send(embed=final[1])
    else:
        await ctx.send(file=final[0],embed=final[1])

@search.command()
@commands.guild_only()
async def name(ctx,text):
    await ctx.send("Under development")










bot.run(secret.token)