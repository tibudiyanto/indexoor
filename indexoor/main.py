from eth import Eth
from contract import Contract
import json

eth = Eth()
abi = json.load(open("./abis/erc721.json"))


tx_hash = "0x8a9c3242a73433b25a17f8b5aa55533845945fa4c5a520bd44ae91bb4ff3eee0"
tx_hash = "0x9d3eb421007c5c8a065444d3e24527b43d5c923e1d8e80d76f70784160d23d6b"


transaction = eth.get_transaction(tx_hash)
receipt = eth.get_transaction_receipt(tx_hash)
block = eth.get_block("latest")

tx_schema = {key: str(type(value)) for key, value in transaction.items()}
receipt_schema = {key: str(type(value)) for key, value in receipt.items()}
block_schema = {key: str(type(value)) for key, value in block.items()}

json.dump(dict(tx_schema), open("./tx.json", "w"), indent=2)
json.dump(dict(receipt_schema), open("./receipt.json", "w"), indent=2)
json.dump(dict(block_schema), open("./block.json", "w"), indent=2)

# brunks_addr = "0x0651132f094551f9d4e40de3e1e2f8b7ac149c3a"

# brunks = Contract(eth.w3, brunks_addr, abi)
# print(brunks.name())
# print(brunks.get_erc_type())
# brunks = brunks.get_instance()
# print(brunks.totalSupply())

# ctrl_addr = "0xDe4e5fFc4cd4C5582FC3735F96F153d59eEd2E11"

# ctrl = Contract(eth.w3, ctrl_addr, abi)
# print(ctrl.name())
# print(ctrl.get_erc_type())
