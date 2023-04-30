import json
from discord_webhook import DiscordWebhook, DiscordEmbed

def SendWebhook(url,embed):
    # set webhook url
    webhook = DiscordWebhook(url=url)
    webhook.add_embed(embed)
    response = webhook.execute()

    return(response.json()['id'])

def EditWebhook(url,id,embed):
    webhook = DiscordWebhook(url=url, id=id)
    webhook.add_embed(embed)
    response = webhook.edit()