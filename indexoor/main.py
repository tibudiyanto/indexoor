from eth import Eth

eth = Eth()


tx_hash = "0x8a9c3242a73433b25a17f8b5aa55533845945fa4c5a520bd44ae91bb4ff3eee0"


receipt = eth.get_transaction_receipt(tx_hash)
