import discord
from discord.ext import commands
import random
import matchupdata
import framedata
import config

client = commands.Bot(command_prefix = '3s.')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pinging @ {round(client.latency * 1000)}ms')

@client.command()
async def help(ctx):
    embed=discord.Embed(title="lets-go-justin", url="https://github.com/ev-98/lets-go-justin", description="A Street Fighter III: 3rd Strike resource bot.")
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/logopedia/images/b/be/SFIII_Online_Edition_Logo.png/revision/latest/scale-to-width-down/1000?cb=20140206180354")
    embed.add_field(name="##Commands (prefix '3s.')", value="8ball: let the third strike announcer decide your fortune\nframes [character] [move]: display frame data\nfortune: see 8ball\nmu [character1] [character2]: display matchup odds", inline=False)
    embed.add_field(name="##Character codes", value="For any commands, you may type out the 2-letter character code instead of the full name if you prefer.\nAkuma/Gouki: AK/GO\nAlex: AL\nChun-Li: CH\nDudley: DU\n...etc", inline=False)
    embed.add_field(name="##Move notation", value="The command notation for a normal move is [button] or [input].[button]\nThe notation for special moves are [motion].[button]\nSuper arts are denoted as sa1, sa2, sa3\nAerial moves begin with 'air.'\n\nInputs:\nc(crouch), f(forward), b(back), u(up), df, db, uf, ub\nMotions:\nqcf, qcb, hcf, hcb, 360, dp, rapid, charge\nButtons:\nlp, mp, hp, 2p</br>lk, mk, hk, 2k\n\nExamples:\nc.mk(crouching medium), charge.2k(ex spinning bird kick), air.qcf.2p (ex kunai), lp+lk(throw), mp+mk(universal overhead)", inline=True)
    embed.set_footer(text="All sprites property of Capcom | Frame data provided by http://baston.esn3s.com/ ")
    await ctx.send(embed=embed)

@client.command(aliases=['8ball', 'fortune'])
async def _8ball(ctx, *, msg):
    responses=['Yeah, that makes sense!', 'Well, I got the picture!', 'Yeah, I see!', 'Yeah, I\'ve been waiting for this!', 'Alright, that\'s cool!', 'That\'s what I expected!', 'You need to practice more.', 'We await your return, warrior..', 'Excellent job!']
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def mu(ctx, c1, c2):
    arg = get_mu(c1,c2)
    await ctx.send(arg)

# @client.command()
# async def frames(ctx, *, char, move):

def get_mu(c1,c2):
    c1=c1.strip()
    c1=c1.upper()
    c2=c2.strip()
    c2=c2.upper()
    # checking arg1
    if c1=='YU'or c1=='YUN':
        i1=0
    elif c1=='CH'or c1=='CHUN-LI'or c1=='CHUNLI'or c1=='CHUN'or c1=='CHUNNERS'or c1=='CHUNNY' or c1=="CHUN_LI":
        i1=1
    elif c1=='KE'or c1=='KEN':
        i1=2
    elif c1=='MA'or c1=='MAKOTO':
        i1=3
    elif c1=='DU'or c1=='DUDLEY':
        i1=4
    elif c1=='YA'or c1=='YANG':
        i1=5
    elif c1=='GO'or c1=='GOUKI'or c1=='AK'or c1=='AKUMA':
        i1=6
    elif c1=='UR'or c1=='URIEN':
        i1=7
    elif c1=='RY'or c1=='RYU':
        i1=8
    elif c1=='OR'or c1=='ORO':
        i1=9
    elif c1=='IB'or c1=='IBUKI':
        i1=10
    elif c1=='EL'or c1=='ELENA':
        i1=11
    elif c1=='NE'or c1=='NECRO':
        i1=12
    elif c1=='AL'or c1=='ALEX':
        i1=13
    elif c1=='RE'or c1=='REMY':
        i1=14
    elif c1=='Q':
        i1=15
    elif c1=='HU'or c1=='HUGO':
        i1=16
    elif c1=='12'or c1=='TW'or c1=='TWELVE':
        i1=17
    elif c1=='SE'or c1=='SEAN':
        i1=18
    else:
        return f'No character found at `{c1}`. Please check for correct spelling and spacing.'
    
    #checking arg2
    if c2=='YU'or c2=='YUN':
        i2=0
    elif c2=='CH'or c2=='CHUN-LI'or c2=='CHUNLI'or c2=='CHUN'or c2=='CHUNNERS'or c2=='CHUNNY' or c2=="CHUN_LI":
        i2=1
    elif c2=='KE'or c2=='KEN':
        i2=2
    elif c2=='MA'or c2=='MAKOTO':
        i2=3
    elif c2=='DU'or c2=='DUDLEY':
        i2=4
    elif c2=='YA'or c2=='YANG':
        i2=5
    elif c2=='GO'or c2=='GOUKI'or c2=='AK'or c2=='AKUMA':
        i2=6
    elif c2=='UR'or c2=='URIEN':
        i2=7
    elif c2=='RY'or c2=='RYU':
        i2=8
    elif c2=='OR'or c2=='ORO':
        i2=9
    elif c2=='IB'or c2=='IBUKI':
        i2=10
    elif c2=='EL'or c2=='ELENA':
        i2=11
    elif c2=='NE'or c2=='NECRO':
        i2=12
    elif c2=='AL'or c2=='ALEX':
        i2=13
    elif c2=='RE'or c2=='REMY':
        i2=14
    elif c2=='Q':
        i2=15
    elif c2=='HU'or c2=='HUGO':
        i2=16
    elif c2=='12'or c2=='TW'or c2=='TWELVE':
        i2=17
    elif c2=='SE'or c2=='SEAN':
        i2=18
    else:
        return f'No character found at `{c2}`. Please check for correct spelling and spacing.'
   
    return matchupdata.matchups[i1][i2]

client.run(config.token)