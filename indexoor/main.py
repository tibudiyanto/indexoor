from eth import Eth
from contract import Contract
import json

eth = Eth()
abi = json.load(open("./abis/erc721.json"))


tx_hash = "0x8a9c3242a73433b25a17f8b5aa55533845945fa4c5a520bd44ae91bb4ff3eee0"


receipt = eth.get_transaction_receipt(tx_hash)

brunks_addr = "0x0651132f094551f9d4e40de3e1e2f8b7ac149c3a"

brunks = Contract(eth.w3, brunks_addr, abi)
print(brunks.name())
print(brunks.get_erc_type())
brunks = brunks.get_instance()
print(brunks.totalSupply())

ctrl_addr = "0xDe4e5fFc4cd4C5582FC3735F96F153d59eEd2E11"

ctrl = Contract(eth.w3, ctrl_addr, abi)
print(ctrl.name())
print(ctrl.get_erc_type())
