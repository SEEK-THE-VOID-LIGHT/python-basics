import discord

bot = commands.Bot(command_prefix="!")


# There are two ways to get a command:

LOGIN_TOKEN = 0000000   #your token

@bot.event
async def on_message(message):
    #the first
    if message.author == bot.user:
        return
    
    if message.content.lower() == "hello":
        print("hello")
        await message.channel.send(f"Hello {message.author.mention}")
    
    await bot.process_commands(message)


#the second... Make a new def for each command
@bot.command(description='more commands')
async def command_list(ctx):
    pass
    #here you could list possible command


@bot.event
async def on_ready():
    print('Login initiation done as')
    print(bot.user.name)
    print(bot.user.id)
    activity = discord.Game(name="!help", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)


bot.run(LOGIN_TOKEN)