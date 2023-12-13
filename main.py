import os
import json
import telebot
import time
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
VALIDATOR_ADDRESS = os.getenv("VALIDATOR_ADDRESS")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)


def is_in_active_set():
    '''
    Check if a validator address is a Block Producer.
    '''

    abi = None

    # Get the contract ABI
    with open("./abi/ValidatorSet.json", "r") as f:
        abi = json.loads(f.read())

    contract = None

    w = None

    # Get the contract address in the right format
    contract_address = Web3.to_checksum_address("0x617c5d73662282ea7ffd231e020eca6d2b0d552f")

    # Instantiate a Web3 object
    w = Web3(Web3.HTTPProvider("https://ronin.lgns.net/rpc"))

    # Create an object to interface with the validator set contract
    contract = w.eth.contract(abi=abi, address=contract_address)

    # Get the validator address in the right format
    val_address = Web3.to_checksum_address(VALIDATOR_ADDRESS)

    # Check in the RPC is reachable
    if not w.is_connected():
        print("RPC is unreachable")

    # Call the isBlockProducer function and get the result
    result = contract.functions.isBlockProducer(val_address).call()

    return result


if __name__ == "__main__":
    print("Starting script...")

    bot.send_message(CHAT_ID, "Started monitoring Ronin Active Set!")

    while True:
        if not is_in_active_set():
            bot.send_message(CHAT_ID, "The validator is not in the active set")

        print("Sleeping for 2 second")
        time.sleep(2)
