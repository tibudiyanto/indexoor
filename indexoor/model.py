from typing import List 


from pydantic import BaseModel



class Block(BaseModel):
    hash: bytes
    number: int
    nonce: bytes
    parentHash: bytes
    baseFeePerGas: int
    difficulty: int
    gasLimit: int
    gasUsed: int
    # logsBloom: bytes
    # miner: str
    # mixHash: bytes
    receiptsRoot: bytes
    # sha3Uncles: bytes
    size: int
    # stateRoot: bytes
    timestamp: int
    # totalDifficulty: int
    transactions: List[bytes]


class Transaction(BaseModel):
    # accessList: List[str]
    blockHash: bytes
    blockNumber: int
    chainId: str
    # Sender address
    from: bytes
    gas: int
    gasPrice: int
    hash: bytes
    input: str
    # maxFeePerGas: int
    # maxPriorityFeePerGas: int
    nonce: int
    # wtf is this
    # r: bytes
    # s: bytes
    # destination address, null if contract creation
    to: bytes
    transactionIndex: int
    type: str
    # v: int
    value: int

class Log(BaseModel):
    blockHash: bytes
    blockNumber: int
    transactionHash: bytes
    contractAddress: bytes
    transactionIndex: int
    # cumulativeGasUsed: int
    # effectiveGasPrice: int
    topics: List[bytes]
    logIndex: int
    data: bytes

