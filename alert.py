# Copyright 2020 by KFMgang.
# All rights reserved.
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import os, sys, time
from discord_webhook import DiscordWebhook, DiscordEmbed
import psutil
from threading import Thread
from time import sleep

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def checkrunning():
    while 1:
        if checkIfProcessRunning('deadmatterServer.exe') is True:
            print('Dead Matter Server is runing')
            checkcrash()
        sleep(1)



def checkcrash():
    while 1:
        if checkIfProcessRunning('deadmatterServer.exe') is False:
            print('(Crash/restart) send Notification on Discord !')
            content ="" # add an id of a role to be identified exemple : "<@&0101010101>" 0101010101 = the id
            webhook = DiscordWebhook(url='YOUR DISCORD WEBHOOK', content=content)
            #set embed
            embed = DiscordEmbed(title='Server Status', description='**(╯°□°）╯︵ ┻━┻      The server has crashed !**', color=16711680)
            # set footer
            embed.set_footer(text='Crash')
            # set timestamp (default is now)
            embed.set_timestamp()
            webhook.add_embed(embed)
            response = webhook.execute()
            checkrunning()
        sleep(1)

Thread(target=checkrunning).start()
