import responses_1
import discord

#token has been removed for privacy reasons
TOKEN = ''

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print('Discord bot loaded :)')


# z
@client.event
async def on_member_join(member):
    channel = client.get_channel(1098748363781967915)
    await channel.send(f'Welcome to the server {member.mention}.')


@client.event
async def on_message(message: str) -> str:
    if message.author == client.user:
        return

    elif message.author != client.user:
        user_message = message.content
        await message.channel.send(responses_1.handle_response(user_message))


client.run(TOKEN)