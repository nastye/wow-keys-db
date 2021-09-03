import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.author != self.user:
            new_channel = await message.channel.category.create_text_channel(str(message.author))
            await new_channel.send(content='Message from {0.author}: {0.content}'.format(message))
            await message.delete()


def main():
    client = MyClient()
    client.run('NDY4MDk0NjQ5NTg5MDM5MTA1.W0t5HQ.TW9UCe71UGxR2OVb8ZyrLXChUFE')
