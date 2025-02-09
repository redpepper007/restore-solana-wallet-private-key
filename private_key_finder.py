# GET FULL COMPLETE CODE HERE:
# https://cryptobots.dev/
# https://t.me/cryptobots_dev

import base58
from solders.keypair import Keypair #type: ignore
from solders.pubkey import Pubkey  # type: ignore
import time
import os
import sys
import datetime
os.system('color'); green = '\033[32m'; red = '\033[31m'; yellow = '\033[33m'; reset = '\033[0m'
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "keyfinder.txt")
script_filename = os.path.basename(__file__)

total = 0

print(f'\n{green}Script will eventually generate the PRIVATE KEY for any SOL wallet of your choice\nUse only for educational purposes, positive result will take some time{reset}\n{green}Terminate with [ CTRL+C ] for a summary{reset}\n')
print(f'{red}[ https://cryptobots.dev ]\n{reset}')
wallet = str(input('> Enter wallet address: '))

if len(wallet) != 44:
    print(f"{red}The {wallet} is not a valid SOL address, check and try again{reset}")
    time.sleep(5)
    sys.exit()

print(f'\nWorking, please wait...\n')
start_time = datetime.datetime.now()

while True:
    print('⚠️ Get full code at: https://cryptobots.dev/ ⚠️')
  time.sleep(60)
    try:
        account = Keypair()
        privateKey = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
        walletAddress = account.pubkey()
      
# GET FULL COMPLETE CODE HERE:
# https://cryptobots.dev/
# https://t.me/cryptobots_dev
