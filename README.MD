# indexoor

Just a way for me to learn more about eth chain data and also maybe try to index it (?)

# Goals

- [x] See block info
- [x] See transaction 
- [ ] See transaction receipt
- [ ] See block

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
| sh3Uncles     | HexBytes |
| size          | int      |
| stateRoot     | HexBytes |
| timestamp     | int      |

- each blocks has different numbers of transaction
