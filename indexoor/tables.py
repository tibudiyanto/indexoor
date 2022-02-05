from db import DB

from sqlalchemy import Table, Column 
from sqlalchemy.dialects.postgresql import (
    BYTEA,
    INTEGER,
    JSONB,
    BIGINT,
    TIMESTAMP,
    TEXT,
)

blocks = Table(
    "blocks",
    DB.metadata,
    Column("hash", BYTEA, primary_key=True),
    Column("number", BIGINT),
    Column("nonce", BYTEA),
    Column("parent_hash", BYTEA),
    Column("base_fee_per_gas", BIGINT),
    Column("difficulty", INTEGER),
    Column("gas_limit", INTEGER),
    Column("gas_used", INTEGER),
    Column("receipt_root", BYTEA),
    Column("size", INTEGER),
    Column("timestamp", TIMESTAMP),
)

transactions = Table(
    "transactions",
    DB.metadata,
    Column("hash", BYTEA, primary_key=True),
    # foreign key
    Column("block_hash", BYTEA),
    # foreign key
    Column("block_number", BIGINT),
    Column("chain_id", TEXT),
    Column("from", BYTEA),
    Column("to", BYTEA),
    Column("tx_index", INTEGER),
    Column("gas", BIGINT),
    Column("gas_price", BIGINT),
    Column("input", BYTEA),
    Column("nonce", INTEGER),
    Column("type", TEXT),
    Column("value", INTEGER),
)

logs = Table(
    "logs",
    DB.metadata,
    Column("block_hash", BYTEA),
    Column("block_number", BIGINT),
    # foreign Key
    Column("tx_hash", BYTEA, ),
    Column("contract_address", BYTEA),
    Column("tx_index", INTEGER),
    Column("topics", JSONB),
    Column("log_index", INTEGER),
    Column("data", BYTEA),
)
