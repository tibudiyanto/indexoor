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
    contract = Contract(eth.w3, addr, abi).get_instance()
    payload = ERC721(
        name=contract.name(),
        symbol=contract.symbol(),
        totalSupply=contract.totalSupply(),
    )

    return payload.dict()


@app.get("/assets/<string:addr>/<int:token_id>")
def get_token_info(addr, token_id):
    contract = Contract(eth.w3, addr, abi).get_instance()
    payload = ERC721(
        name=contract.name(),
        symbol=contract.symbol(),
        totalSupply=contract.totalSupply(),
        tokenURI=contract.tokenURI(token_id),
    )
    return payload.dict()
