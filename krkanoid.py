import datetime
import json
import os
import urllib.request

import discord
from colorama import Fore
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from numpy import random
import host


INFO = Fore.BLUE + "[" + Fore.YELLOW + "INFO" + Fore.BLUE + "] " + Fore.WHITE
ERROR = Fore.BLUE + "[" + Fore.YELLOW + "ERROR" + Fore.BLUE + "] " + Fore.RED
WARNING = Fore.BLUE + "[" + Fore.YELLOW + "WARNING" + Fore.BLUE + "] " + Fore.YELLOW


intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix="$", intents=intents)
client.remove_command('help')
test_mute = []


@client.event
async def on_ready():
    print("""
     _  __         _                              _       _     _     ____            _   
    | |/ /  _ __  | | __   __ _   _ __     ___   (_)   __| |   | |   | __ )    ___   | |_ 
    | ' /  | '__| | |/ /  / _` | | '_ \   / _ \  | |  / _` |   | |   |  _ \   / _ \  | __|
    | . \  | |    |   <  | (_| | | | | | | (_) | | | | (_| |   | |   | |_) | | (_) | | |_ 
    |_|\_\ |_|    |_|\_\  \__,_| |_| |_|  \___/  |_|  \__,_|   | |   |____/   \___/   \__|
                                                               |_|                        


    █░░ █▀█ █▀▀ █▀█ █░█ █
    █▄▄ █▄█ █▄█ █▄█ ▀▄▀ █

    
    """)
    print(INFO + 'Bot je uspješno pokrenut!')
    await client.change_presence(activity=discord.Game(name="$help"))
    # channel = client.get_channel(832706842798850098)
    # await channel.send("")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Nešto si pogrešno napravio :rolling_eyes:.**')
        print(ERROR + f'Korisnik je nešto pogrešno napisao.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Nemaš dozvolu za tu komandu. :angry:**")
        print(ERROR + f'Korisnik nema permisiju za tu komandu.')
    if isinstance(error, CommandNotFound):
        await ctx.send("**Komanda koju si sazvao ne postoji :sweat_smile:**")
        print(ERROR + f'Korisnik je sazvao komandu koja ne postoji.')


@client.event
async def on_member_join(member):
    channel = client.get_channel(793514424844419083)
    embed = discord.Embed(
        colour=discord.Colour.purple()
    )

    embed.add_field(name="Dobrodošao", value=f':tada: {member.name} je ušao na naš Server!')
    role = discord.utils.get(member.guild.roles, name='「💥」Korisnik')
    if member.name in test_mute:
        role.append("test")
        await member.add_roles(role)
    else:
        await member.add_roles(role)

    print(INFO + f"{member.name} je ušao na Aliens Server.")
    await channel.send(embed=embed)


@client.event
async def on_member_remove(member):
    channel = client.get_channel(850335470863777855)
    embed = discord.Embed(
        colour=discord.Colour.red()
    )

    embed.add_field(name="Doviđenja", value=f':boom: {member.name} je izašao sa našeg Servera!')
    if "test" in member.roles:
        test_mute.append(member.name)

    print(INFO + f'{member.name} je izašao sa Servera.')
    await channel.send(embed=embed)


#@client.event
#async def on_message(ctx, message):
#    if "discord.gg" in message.content.lower():
#        await message.delete()
#        await message.channel.send(f"**{message.author.name}** nemoj više slati pozivnice za Servere! :angry:")
#        print(WARNING + f"{message.author.name} je poslao pozivnicu za Server.")
#    else:
#        await ctx.process_message(message)


@client.command()
async def invites(ctx):
    embed = discord.Embed(
        title="KrkanoidBot - Invites",
        colour=discord.Colour.green()
    )

    total_invites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            total_invites += i.uses

    embed.add_field(name="Invites",
                    value=f":fire: Pozvao si {total_invites} {'' if total_invites == 1 else 's'} membera na server!")
    print(INFO + f'{ctx.message.author.name} je pozvao {total_invites} korisnika na server.')
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    await ctx.send(embed=embed)


@client.command()
async def bestija(ctx):
    lines = open('./text/bestija.txt').read().splitlines()
    ran = random.choice(lines)
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )
    
    embed.add_field(name="KrkanoidBot - Beštija", value=f'_ _')
    embed.set_image(url=f'{ran}')
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "bestija".')
    await ctx.send(embed=embed)


@client.command()
async def penis(ctx, member: discord.Member):
    embed = discord.Embed(
        title="KrkanoidBot - Penis",
        colour=discord.Colour.red()
    )

    ln = open('./text/ps.txt').read().splitlines()
    velicina = random.choice(ln)

    embed.add_field(name=f"{member.name} penis: ", value=velicina, inline=False)
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "penis".')
    await ctx.send(embed=embed)


@client.command()
async def poen(ctx):
    velicina = random.randint(0,2000)
    embed = discord.Embed(
        title="KrkanoidBot - Poeni",
        colour=discord.Colour.red()
    )

    x = datetime.datetime.now()
    y = x.strftime("%H" + ":" + "%M")
    embed.add_field(name='Dobitak', value=f"||‎‎     {velicina} XP-a      ||", inline=True)
    embed.add_field(name='Rank', value=f"Početnik", inline=True)
    embed.add_field(name='Vrijeme', value=f'{y}', inline=True)
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999", icon_url=ctx.author.avatar_url)
    print(INFO + f"{ctx.message.author.name} je osvojio {velicina}XP-a.")
    await ctx.send(embed=embed)


@client.command()
async def add(ctx):
    embed = discord.Embed(
        title="KrkanoidBot - Add Bot",
        color=discord.Colour.dark_teal()
    )
    embed.add_field(name='Pozovite KrkanoidBota na vaš server',
                    value='[KrkanoidBot](https://discord.com/oauth2/authorize?client_id=813861302774399046&scope=bot&permissions=-1)',
                    inline=False)
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999", icon_url=ctx.author.avatar_url)
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "add".')
    await ctx.send(embed=embed)


@client.command()
async def porn(ctx):
    embed = discord.Embed(
        color=0xFF00E3
    )
    link = "https://nekobot.xyz/api/image?type=pgif"
    podaci = urllib.request.urlopen(link).read().decode()
    obj = json.loads(podaci)
    embed.add_field(name="KrkanoidBot - Porn", value="_ _")
    embed.set_image(url=obj['message'])
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999", icon_url=ctx.author.avatar_url)
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "porn".')
    await ctx.send(embed=embed)


@client.command()
async def howgay(ctx, member: discord.Member):
    velicina = random.randint(0,100)
    embed = discord.Embed(
        color=0xFF00F7
    )

    embed.add_field(name=f'KrkanoidBot - HowGay', value=f"{member.name} je {velicina}% gay.", inline=True)
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999", icon_url=ctx.author.avatar_url)
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "howgay".')
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="KrkanoidBot - Komande",
        colour=discord.Colour.green()
    )
    " "
    a1 = """
    $poen
    $penis @user
    $avatar @user
    $dinamo @user
    $hajduk @user
    $bestija @user
    $info @user
    """

    a2 = """
    $ban @user
    $kick @user
    $mute @user
    $unmute @user
    $clear 10
    $warn @user reason
    $ping @user
    """

    a3 = """
    $komande
    $join
    $leave
    $members
    $servers
    $invites
    $add
    """
    embed.add_field(name=f':tada: Zabava_                    _', value=a1, inline=True)
    embed.add_field(name=':fire: Staff_                          _', value=a2, inline=True)
    embed.add_field(name=':zap: Korisnici_                   _', value=a3, inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/815156505585516565/843518561149648906/line.gif')

    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999", icon_url=ctx.author.avatar_url)
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "help".')
    await ctx.send(embed=embed)


@client.command()
async def hajduk(ctx, member: discord.Member):
    embed = discord.Embed(
        title=":white_heart: Hajduk",
        colour=discord.Colour.blue()
    )

    embed.add_field(name="Torcida", value=f'{member.name} je Hajdukovac!')
    embed.set_image(
        url='https://media.discordapp.net/attachments/815156505585516565/815590237761699891/HNK_Hajduk_Split.png')
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "hajduk".')
    await ctx.send(embed=embed)


@client.command()
async def dinamo(ctx, member: discord.Member):
    embed = discord.Embed(
        title=":blue_heart: Dinamo",
        colour=discord.Colour.blue()
    )

    embed.add_field(name="Bad Blue Boys", value=f'{member.name} je Dinamovac.')
    embed.set_image(
        url='https://media.discordapp.net/attachments/793516467147767808/851535552234389534/9a811af3c03be5bfd31c14349e2640a2.png?width=670&height=670')
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "dinamo".')
    await ctx.send(embed=embed)


@client.command()
async def avatar(ctx, *, member: discord.Member = None):
    embed = discord.Embed(
        title="KrkanoidBot - Avatar",
        color=0x3BFF00
    )

    if not member:
        member = ctx.message.author
    user_avatar = member.avatar_url

    embed.add_field(name=f'{member.name} avatar', value='_ _')
    embed.set_image(url=f'{user_avatar}')
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "avatar".')
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx, member: discord.Member):
    embed = discord.Embed(
        colour=discord.Colour.green()
    )

    embed.add_field(name="Speed Test", value=f':fire: {member.name} ping je  **{round(client.latency * 1000)} ms**')
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "ping".')
    await ctx.send(embed=embed)


@client.command()
async def info(ctx, member: discord.Member):
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Informacije"
    )

    embed.add_field(name=":fire: Username", value=f'{member.name}', inline=False)
    embed.add_field(name=":boom: User ID", value=f'{member.id}', inline=False)
    embed.add_field(name=":zap: Nick", value=f'{member.nick}', inline=False)
    embed.add_field(name=":alien: Status", value=f'{member.status}', inline=False)
    embed.add_field(name=":star: Discriminator", value=f'{member.discriminator}', inline=False)
    embed.add_field(name=":ringed_planet: Joined", value=f'{member.joined_at}', inline=False)
    embed.add_field(name=":rocket: Created", value=f'{member.created_at}', inline=False)
    embed.add_field(name=":hammer: Roles", value=f'{member.top_role}', inline=False)
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "info".')
    await ctx.send(embed=embed)


@client.command()
async def members(ctx):
    embed = discord.Embed(
        title=f':alien: KrkanoidBot - Members',
        color=0xFE01E3
    )
    online_memberi = sum(member.status != discord.Status.offline and not member.bot for member in ctx.guild.members)

    embed.add_field(name=f":purple_circle:  Broj korisnika -> {ctx.guild.member_count}",
                    value=f"**:green_circle: Online korisnici -> {online_memberi}**", inline=True)
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "members".')
    await ctx.send(embed=embed)


@client.command()
async def servers(ctx):
    broj_servera = len(client.guilds)
    embed = discord.Embed(
        title="KrkanoidBot - Servers",
        color=discord.Colour.blue()
    )
    embed.add_field(name="Serveri", value='Bot je aktivan na **{0}** servera!'.format(broj_servera))
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    print(INFO + f'{ctx.message.author.name} je sazvao komandu "servers".')
    await ctx.send(embed=embed)


###############################################
#                                             #
#                 STAFF KOMANDE               #
#                                             #
###############################################


@client.command()
@commands.has_any_role("Krkanoid", "Bot", "「👽」HEAD OWNER", "「👑」Kaiyo", "「👑」Owner", "「💉」Co-Owner", "「🔧」Admin")
async def clear(ctx, amount=2):
    embed = discord.Embed(
        title=":alien: KrkanoidBot - Clear",
        colour=discord.Colour.gold()
    )
    if commands.has_permissions(manage_messages=True):
        await ctx.channel.purge(limit=amount)

        embed.add_field(name=f"Obrisno -> {amount} poruka ", value="***Poruke su izbrisane :D***", inline=True)
        embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
        print(WARNING + f"{ctx.message.author.name} je obrisao {amount} poruke.")
        await ctx.send(embed=embed)
        return
    else:
        embed.add_field(name=f":fire: Upozorenje", value="***Nemaš dozvolu za tu komandu.***", inline=True)
        embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    vrijeme_bana = "24 sata"
    embed = discord.Embed(
        title="KrkanoidBot - Ban",
        colour=discord.Colour.purple()
    )

    x = datetime.datetime.now()
    y = x.strftime("%H" + ":" + "%M")
    embed.add_field(name=f"**Banan ->** ***{member.name}***", value=f'**Vrijeme ->** ***{y}***', inline=False)
    embed.add_field(name=f'**Razlog ->** ***{reason}***', value=f"**Trajnost -> ** ***{vrijeme_bana}***", inline=False)
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    print(WARNING + f'{ctx.message.author.name} je banao {member.name} sa Servera.')
    await ctx.send(embed=embed)
    await member.ban(reason=reason)


@client.command()
async def warn(ctx, member: discord.Member, *, arg):
    f = open("upozorenja.txt", "a")
    f.write(f"{member.name} ----> " + arg + "\n")
    f.close()

    await ctx.send(f"**{member.name}** nemoj više raditi loše stvari :rage:.")
    print(WARNING + f"{member.name} radi probleme na serveru.")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    """24 sata"""
    embed = discord.Embed(
        title="KrkanoidBot - Kick",
        colour=discord.Colour.purple()
    )

    x = datetime.datetime.now()
    y = x.strftime("%H" + ":" + "%M")
    embed.add_field(name=f"**Kickan ->** ***{member.name}***", value=f'**Vrijeme ->** ***{y}***', inline=False)
    embed.add_field(name=f'**Razlog ->** ***{reason}***', value=f"**Trajnost -> ** ***Može odma ući.***", inline=False)
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    print(WARNING + f'{ctx.message.author.name} je kickao {member.name} sa Servera.')
    await ctx.send(embed=embed)
    await member.kick(reason=reason)


@client.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    muted_role = discord.utils.get(guild.roles, name="Mutavac")
    "24 sata"
    embed = discord.Embed(
        title="KrkanoidBot - Mute",
        color=0xFF3232
    )

    x = datetime.datetime.now()
    y = x.strftime("%H" + ":" + "%M")
    embed.add_field(name=f"**Mjutan ->** ***{member.name}***", value=f'**Vrijeme ->** ***{y}***', inline=False)
    embed.add_field(name=f'**Razlog ->** ***{reason}***', value=f"**Trajnost -> ** ***24h***", inline=False)
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")
    embed.set_thumbnail(url=ctx.author.avatar_url)

    if not muted_role:
        muted_role = await guild.create_role(name="Mutavac")

    for channel in guild.channels:
        await channel.set_permissions(muted_role, speak=False, send_messages=False, read_message_history=True,
                                      read_messages=False)

    print(WARNING + f'{ctx.message.author.name} je mjutao {member.name}.')
    await member.add_roles(muted_role, reason=reason)
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Mutavac")
    embed = discord.Embed(
        title="KrkanoidBot - Unmute",
        color=0x4FFE01
    )
    embed.add_field(name="Unmute", value=f':white_check_mark: {member.name} je dobio unmute!')
    embed.set_footer(text="KrkanoidBot - Made by Krkan#9999")

    await member.remove_roles(muted_role)
    print(f'[INFO] {member.name} je dobio unmute.')
    print(WARNING + f'{ctx.message.author.name} je unmjutao {member.name}.')
    await ctx.send(embed=embed)


token = os.environ['token']
host.keep_alive()
client.run(token)
