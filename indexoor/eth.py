import os

from web3 import Web3

INFURA_URL = os.environ.get("INFURA_URL")


class Eth:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(INFURA_URL))

    def get_block(self, block_number: int):
        block_data = self.w3.eth.get_block(block_number)
        return block_data

    def get_transaction(self, transaction: str):
        tx_detail = self.w3.eth.get_transaction(transaction)
        return tx_detail

    def get_transaction_receipt(self, transaction: str):
        receipt = self.w3.eth.get_transaction_receipt(transaction)
        return receipt
