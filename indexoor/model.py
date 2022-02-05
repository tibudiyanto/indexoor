from hexbytes import HexBytes
from typing import List, Optional


from pydantic import BaseModel, validator, root_validator


class HexBytesType(HexBytes):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, HexBytes):
            raise TypeError("has to be HexBytes")
        return v


"""
Pydantic Models belows are used to type guard data returned from 
web3 library and also used to serialize data into postgres.
"""


class Block(BaseModel):
    hash: HexBytesType
    number: int
    nonce: HexBytesType
    parent_hash: HexBytesType
    base_fee_per_gas: int
    difficulty: int
    gas_limit: int
    gas_used: int
    receipts_root: HexBytesType
    size: int
    timestamp: int
    transactions: List[HexBytesType]

    def __init__(
        self, parentHash, baseFeePerGas, gasLimit, gasUsed, receiptsRoot, **data
    ):
        super().__init__(
            **data,
            parent_hash=parentHash,
            base_fee_per_gas=baseFeePerGas,
            gas_limit=gasLimit,
            gas_used=gasUsed,
            receipts_root=receiptsRoot,
        )


class Transaction(BaseModel):
    block_hash: HexBytesType
    block_number: int
    chain_id: str
    # Sender address
    sender: HexBytesType
    gas: int
    gas_price: int
    hash: HexBytesType
    input: str
    nonce: int
    # destination address, null if contract creation
    to: Optional[HexBytesType]
    transaction_index: int
    type: str
    value: int

    def __init__(
        self, blockHash, blockNumber, chainId, gasPrice, transactionIndex, **data
    ):
        super().__init__(
            **data,
            block_hash=blockHash,
            block_number=blockNumber,
            chain_id=chainId,
            gas_price=gasPrice,
            transaction_index=transactionIndex,
            sender=data["from"],
        )

    @validator("sender", pre=True)
    def check_sender(cls, v):
        return HexBytes(v)


class Log(BaseModel):
    block_hash: HexBytesType
    block_number: int
    tx_hash: HexBytesType
    contract_address: HexBytesType
    transaction_index: int
    topics: List[HexBytesType]
    log_index: int
    data: Optional[str]

    def __init__(
        self,
        address,
        blockHash,
        blockNumber,
        transactionHash,
        transactionIndex,
        logIndex,
        **data
    ):
        super().__init__(
            **data,
            contract_address=address,
            block_hash=blockHash,
            block_number=blockNumber,
            tx_hash=transactionHash,
            transaction_index=transactionIndex,
            log_index=logIndex,
        )

    @validator("contract_address", pre=True)
    def check_contract(cls, v):
        return HexBytes(v)
