import json
from typing import Optional
from flask import Flask
from pydantic import BaseModel

from eth import Eth
from contract import Contract

eth = Eth()
abi = json.load(open("./abis/erc721.json"))


class ERC721(BaseModel):
    name: str
    symbol: str
    totalSupply: str
    tokenURI: Optional[str]


app = Flask(__name__)


@app.get("/assets/<string:addr>")
def get_contract_info(addr: str):
    contract = Contract(eth.w3, addr.lower(), abi).get_instance()
    return contract.get_contract_info().dict()


@app.get("/assets/<string:addr>/<int:token_id>")
def get_token_info(addr, token_id):

    contract = Contract(eth.w3, addr.lower(), abi).get_instance()
    return contract.get_token_information(token_id).dict()
