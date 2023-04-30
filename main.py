import json
import time
import codecs

from core.ServerStatus import *
from core.Webhook import *
from core.Logger import *
from core.Table import *

# print header text
printHeader()

# import config.json
try:
    info("Try import config")
    with codecs.open('config.json', 'r', 'utf-8') as file:
        config = json.load(file)
    info("Success import config")
except:
    error("Fail import config")

print_config(config)
print("\n")

while True:
    info("Try Get Server Data")
    serverAddress, serverPort, serverisOnline, serverPlayersOnline, serverPlayersMax, serverVersion, serverMotd, currentDateTime = getStatus(f"{config['SERVER_ADDRESS']}:{config['SERVER_PORT']}")
    success("Success Get Server Data")

    embed = {
            "type": "rich",
            "title": f"{config['SERVER_NAME']} Server Status",
            "description": "",
            "color": 0x00FFFF,
            "timestamp": f"{currentDateTime}",
            "thumbnail": {
                "url": "https://api.mcsrvstat.us/icon/play.gaprok.me:19133"
            },
            "footer": {
                "text": f"{config['FOOTER']} | Last Update"
            },
            "fields": [
            {
                "name": ":globe_with_meridians:  Server Address",
                "value": f"```{serverAddress}```",
                "inline": True
            },
            {
                "name": ":satellite:  Port",
                "value": f"```{serverPort}```",
                "inline": True
            },
            {
                "name": ":scroll:  MOTD",
                "value": f"```{serverMotd}```"
            },
            {
                "name": ":gear:  Version",
                "value": f"```{serverVersion}```",
                "inline": True
            },
            {
                "name": ":signal_strength:  Status",
                "value": f"```{serverisOnline}```",
                "inline": True
            },
            {
                "name": ":busts_in_silhouette:  Player Count",
                "value": f"```{serverPlayersOnline} | {serverPlayersMax} Players```",
            }
        ]
    }

    if config['MESSAGE_ID'] == "":
        info("MESSAGE_ID not found, trying send first message")
        response = SendWebhook(config['WEBHOOK_URL'],embed)
        config['MESSAGE_ID'] = response

        # write the message id on config file
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        
        success("Success send first message and update MESSAGE_ID")

    else:
        info("Trying update the message")
        EditWebhook(config['WEBHOOK_URL'],config['MESSAGE_ID'],embed)
        success("Success update the message")
    
    sleep(config['SLEEP'])