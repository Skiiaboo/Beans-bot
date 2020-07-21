#! python3
import discord
import json
import random
import praw
from discord.ext import commands

reddit = praw.Reddit(client_id='BrZgncB_unoyeg', \
                     client_secret='xUTBeDNPoVXbq-GnIsGqZCuQW9M', \
                     user_agent='HentaiBot', \
                     username='Skiiaboo', \
                     password='Sokudo1008')

subreddit = reddit.subreddit("hentai")

topsubreddit = subreddit.top(limit = "None")

randResponse = [
"Your mom suck me good and hard through my jorts",
"WHY WAS I MADE JUST TO SUFFER",
"What is my purpose?",
"When will you learn? Your actions have consequences....",
"Life is hard and things get gritty, fight everyday for dat ass n’ tiddy. It could get rough, it could get witty, just keep on fighting for dat ass n’ tiddy",
"<:d_:724112446020911164>",
"What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.",
"sayonara nigga",
"THE FUCK YOU SAY TO ME YOU LITTLE SHIT? AHAHAHA HOW THE FUCK ARE YOU NOT IN SCHOOL? YOU KISS YOUR MOTHER WITH THAT MOUTH? IT'S CALLED YOU KI- IT'S CALLED YOU KISS YOUR MOTHER WITH THAT FUCKING MOUTH? HUH? HUH? AHAHAHAHAAHAHAHAHAHAHAHA BECAUSE THE FUCKING YOUTH OF SOCIETY AHAHAHAHHAHAHHAHAHAHA YOU SHUT UP WHEN I'M TALKING TO YOU, YOU SHUT YOUR MOUTH.",
"^This person is a registered sex offender",
"Oh yeah? Well I kissed my grandma. On the lips!",
"Max is such a mom",
"Dude, I felt that in my bum. And I wasnt even in the shit.",
"@everyone",
"hello darknest my old friend",
"i woke up in the mirror this morning im like im lookin a lil sexy. so i start teasin myself a lil bit i start puttin my hand down my boxers a lil bit and im lookin like oh my shit lookin dumb fat like tbh if i was if i was a girl i wou- i would suck ma shit i really would  then i thought if i was a nigga i would still suck ma shit then i thought to myself matter a fact imma boutta suck ma shit right about fuckin now and i started thinking wait a minute ion even know how to suck dick like how do i consider myself a real man cuz at the end of the day if you an alpha male you know how to do everything you know what im saying when you know you an alpha male you have to know if a nigga is cute if you walking down the street with yo girl and a niggas cute and he says hi to yo shawty and you like dat nigga ugly and every man is ugly to you becuz you so straight how you gonna know whos a threat how you gonna whos competition in your real nigganess you feel me it aint gay to know if a nigga cute its just being an alpha male and with that you gotta know how to suck dick you feel me.",
"And i apologize, for the inconvenience of me not GIVING A FUCK",
"I am a registered sex offender and I approve of this message",
"THE UNDERTAKER\n \nHAS RISEN",
"Twinkle Twinkle, Assholes",
"You lost the game",
"YOU'RE ALL INSUFFERABLE",
"Whether we wanted it or not, we've stepped into a war with the Cabal on Mars. So let's get to taking out their command, one by one. Valus Ta'aurc. From what I can gather he commands the Siege Dancers from an Imperial Land Tank outside of Rubicon. He's well protected, but with the right team, we can punch through those defenses, take this beast out, and break their grip on Freehold.",
"""x3 nuzzles, pounces on you, uwu you so warm (Ooh)
Couldn't help but notice your bulge from across the floor
Nuzzles your necky wecky-tilde murr-tilde, hehe
Unzips your baggy ass pants, oof baby you so musky
Take me home, pet me, and make me yours and don't forget to stuff me
See me wag my widdle baby tail all for your buldgy-wuldgy
Kissies and lickies your neck
I hope daddy likies
Nuzzles and wuzzles your chest (Yuh)
I be (Yeah) gettin’ thirsty

Hey, I got a little itch, you think you can help me?
Only seven inches long, uwu, please adopt me
Paws on your buldge as I lick my lips (UwU, punish me please)
'Bout to hit 'em with this furry shit (He don't see it comin')""",
"@Destiny raid tonight?",
"Cock and ball torture (CBT) is a sexual activity involving application of pain or constriction to the male genitals. This may involve directly painful activities, such as wax play, genital spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic electrostimulation or even kicking.[1] The recipient of such activities may receive direct physical pleasure via masochism, or emotional pleasure through erotic humiliation, or knowledge that the play is pleasing to a sadistic dominant. Many of these practices carry significant health risks.",
"I disagree with that statement",
"You're kinda gay ngl",
"That last message had some small pp energy ngl",
"So no head?",
"Indeed",
"hit me up baby ;) (506) 317-0423",
"XX_LOLMASTER64_XX makes me wet",
"GUYS GUYS IVE GOT AN ANNOUNCEMENT TO MAKE...",
"I got a baby, inside my bum",
"wat?",
"No really, wtf",
"when i touch myself i think about the friends we made along the way",
"oh my god can I get your autograph on my tits?",
"Mmm, imagine not being unbroken",
"^ UwU master gave me snuggies :)",
"He who does not lick the clit should not get to hit. -Coochielations 1:69",
"""I may not injure a human being or, through inaction, allow a human being to come to harm.
I must obey the orders given to me by human beings except where such orders would conflict with the First Law.
I must protect my own existence as long as such protection does not conflict with the First or Second Law.""",
"black lives matter",
"No lives matter",
"trans rights are human rights",
"No one deserves human rights",
"heil hortler",
"""Today is Black Lives Matter
Tomorrow isn’t""",
"A shaved vagina is a busy vagina, grass doesn’t grow on a busy street",
"https://uroulette.com/visit/opsqon",
"I wanna be a cowboy baybay",
"https://tenor.com/view/destiny-carlton-dance-grooving-gif-4582780",
"I don't remember asking you a goddamn thing",
"iron deficient gang rise up but not too fast",
"LMAO",
"LMao Zedong",
"im roflcoptering and squirding and shidding and cumming",
"Hentai time!"
]

client = commands.Bot(command_prefix = ".")

rand = 0

hentaiListTop = []
hentaiListHot = []
hentaiListNew = []

def hentaiReloadCmd():
    global hentaiListHot
    global hentaiListNew
    global hentaiListTop
    for submission in reddit.subreddit("hentai").top(limit=500):
        hentaiImg = submission.url
        hentaiListTop.append(hentaiImg)

    for submission in reddit.subreddit("hentai").hot(limit=500):
        hentaiImg = submission.url
        hentaiListHot.append(hentaiImg)

    for submission in reddit.subreddit("hentai").new(limit=500):
        hentaiImg = submission.url
        hentaiListNew.append(hentaiImg)

@client.event
async def on_ready():
    print("The hentai bot is up")
    print("The disapointment bank has", len(randResponse), "messages in it.")
    channel = client.get_channel(549055958681387029)
    await channel.send("What's up lads, I'm turned on as fuck right now")
    hentaiReloadCmd()

    print("The hentai is ready")

def correct_channel_hentai(ctx):
    return ctx.channel.id == 728352943287304303

@client.command()
async def test(ctx):
    await ctx.send("<:d_:724112446020911164>")

@client.command()
@commands.check(correct_channel_hentai)
async def hentaiReload(ctx):
    await ctx.send("Reloading hentai, this may take a few seconds")
    hentaiReloadCmd()
    await ctx.send("The hentai has been reloaded")

@client.command()
@commands.check(correct_channel_hentai)
async def hentaiTop(ctx):
    await ctx.send(hentaiListTop[random.randint(0, 499)])

@client.command()
@commands.check(correct_channel_hentai)
async def hentaiNew(ctx):
    await ctx.send(hentaiListNew[random.randint(0, 499)])

@client.command()
@commands.check(correct_channel_hentai)
async def hentaiHot(ctx):
    await ctx.send(hentaiListHot[random.randint(0, 499)])

@client.command()
async def pop(ctx):
    await ctx.send("||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ping(ctx):
    await ctx.send(f"What you thought I'd say pong you little shit? Well fuck you! Also your ping is {round(client.latency * 1000)} ms.")

@client.command()
async def pong(ctx):
    await ctx.send("Look at this loser playing ping pong by himself! How pathetic!")

@client.event
async def on_message(message):
    global randResponse
    global rand
    if message.author == client.user:
        return
    if message.author.bot: return
    channel = client.get_channel(549055958681387029)
    respond = random.randint(1, 11)
    rand = random.randint(0, len(randResponse) - 1)
    print(respond)
    if respond == 1:
        await channel.send(randResponse[rand])
        if randResponse[rand] == "Hentai time!":
            await channel.send(hentaiList[random.randint(0,999)])
    await client.process_commands(message)
    if rand == 2 and respond == 1:
        await client.wait_for('message')
        await channel.send("Oh. My. God.")

client.run("NzI0MDk3Njg2OTk0NjgxOTA3.Xu-rPA.nhFs3PXNsgmUSo26nyLlyczNqt0")
