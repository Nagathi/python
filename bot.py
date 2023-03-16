import discord
from key import token

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

client = discord.Client(intents = intents)
TOKEN = token.get("TOKEN")

bad_words = ['teste1', 'teste2', 'teste3', 'teste4']

def verify_content(msg):
    length = len(bad_words)
    for i in range(length):
        if bad_words[i] == msg.lower():
            return 'banido'
            


@client.event
async def set_cargo(message):
    await message.send("Mensagem especial deletada")

@client.event
async def set_cargo(message):
    if message.on_bulk_message_delete("xvideos"):
        await message.channel.send("Mensagem especial deletada")

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.startswith(".help"):
        await message.channel.send("Comandos: \n .myuser \n .mypic")

    if message.content.startswith(".myuser"):
        await message.channel.send(f"Seu user é: {message.author}")

    if message.content.startswith(""):
        retorno = verify_content(message.content)
        if retorno == 'banido':
            await message.channel.send(f"{message.author} foi {retorno} por linguagem inapropriada")


client.run(TOKEN)