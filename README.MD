# indexoor

Just a way for me to learn more about eth chain data and also maybe try to index it (?)

# Goals

- [x] look up block info
- [x] look up transaction
- [x] look up transaction receipt
- [x] look up block
- [x] deduce a contract is an ERC721
- [x] deduce a contract is an ERC1155
- [x] create a starlette API
- [x] Create web service endpoint to:
  - [x] Fetch an NFT contract info /assets/<contract_addr>
  - [x] Fetch metadata of an tokenID /assets/<contract_addr>/<token_id>
- Index the chain from genesis for all NFT contract

# Dev Notes

## Blocks

| field         | dataType |
| ------------- | -------- |
| baseFeePerGas | int      |
| difficulty    | int      |
| extraData     | HexBytes |
| gasLimit      | int      |
| gasUsed       | int      |
| hash          | HexBytes |
| logsBlook     | HexBytes |
| miner         | str      |
| mixHash       | HexBytes |
| nonce         | HexBytes |
| number        | int      |
| parentHash    | HexBytes |
| receiptsRoot  | HexBytes |
| size          | int      |
| stateRoot     | HexBytes |
| timestamp     | int      |

## Contract

| field       | type |
| ----------- | ---- |
| name        | str  |
| type        | str  |
| addr        | str  |
| symbol      | str  |
| totalSupply | int  |
| tokenURI    | str  |
