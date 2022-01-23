import json
from web3 import Web3

INTERFACE_ID_165 = "0x01ffc9a7"
INTERFACE_ID_721 = "0x80ac58cd"
INTERFACE_ID_1155 = "0xd9b67a26"

erc721_abi = json.load(open("./abis/erc721.json"))
erc1155_abi = json.load(open("./abis/erc1155.json"))


class _Contract:
    """Class to interact with random contract"""

    def __init__(self, w3: Web3, addr: str, abi: str):
        self.w3 = w3
        self.addr = addr
        self.abi = abi
        self.contract = self.w3.eth.contract(Web3.toChecksumAddress(addr), abi=abi)

    def name(self) -> str:
        return self.contract.functions.name().call()

    def get_erc_type(self) -> str:
        is_support_165 = self.contract.functions.supportsInterface(
            INTERFACE_ID_165
        ).call()

        if not is_support_165:
            return "probably 20"

        is_support_1155 = self.contract.functions.supportsInterface(
            INTERFACE_ID_1155
        ).call()

        if is_support_1155 and is_support_165:
            return "ERC1155"

        is_support_721 = self.contract.functions.supportsInterface(
            INTERFACE_ID_721
        ).call()

        if is_support_721 and is_support_165:
            return "ERC721"

        return "probably 20"


class Contract(_Contract):
    def name(self) -> str:
        return self.contract.functions.name().call()

    def get_instance(self):
        if self.get_erc_type() == "ERC721":
            return ERC721(self.w3, self.addr)

        if self.get_erc_type() == "ERC1155":
            return ERC721(self.w3, self.addr)
        raise Exception("Implement this")


class ERC721(Contract):
    def __init__(self, w3: Web3, addr, abi=erc721_abi):
        super().__init__(w3, addr, abi=abi)

    def symbol(self) -> str:
        return self.contract.functions.symbol().call()

    def totalSupply(self) -> str:
        return self.contract.functions.totalSupply().call()

    def tokenURI(self, id: int) -> str:
        return self.contract.functions.tokenURI(id).call()


class ERC1155(Contract):
    def __init__(self, w3: Web3, addr, abi=erc1155_abi):
        super().__init__(w3, addr, abi=abi)

    def symbol(self) -> str:
        return self.contract.functions.symbol().call()

    def uri(self, id: int) -> str:
        return self.contract.functions.tokenURI(id).call()
