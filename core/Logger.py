import time

class style:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def reset():
    print(f"                                                ", end="\r")

def sleep(seconds):
    while seconds > 0:
        print(f"{style.OKBLUE}Sleep {style.OKCYAN}{seconds}s", end="\r")
        time.sleep(1)
        seconds -= 1
        reset()
    reset()

def info(text):
    print(f"{style.OKBLUE}{text}", end="\r")
    time.sleep(1)
    reset()

def success(text):
    print(f"{style.OKGREEN}{text}", end="\r")
    time.sleep(1)
    reset()

def error(text):
    print(f"{style.FAIL}{text}", end="\r")
    time.sleep(1)
    reset()

def printHeader():
    print(f'''{style.OKBLUE}                                                                                        
  __  __ ___ _  _ ___ ___ ___    _   ___ _____                
 |  \/  |_ _| \| | __/ __| _ \  /_\ | __|_   _|               
 | |\/| || || .` | _| (__|   / / _ \| _|  | |                 
 |_|  |_|___|_|\_|___\___|_|_\/_/ \_\_|   |_|                 
      ___ ___ _____   _____ ___   ___ _____ _ _____ _   _ ___ 
     / __| __| _ \ \ / / __| _ \ / __|_   _/_\_   _| | | / __|
     \__ \ _||   /\ V /| _||   / \__ \ | |/ _ \| | | |_| \__ \\
     |___/___|_|_\ \_/ |___|_|_\ |___/ |_/_/ \_\_|  \___/|___/

    ''')

def print_config(config):
    for key, value in config.items():
        print(f"{style.HEADER}{key.ljust(15, ' ')} : {style.OKCYAN}{value}")
