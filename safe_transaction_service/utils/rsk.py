from enum import Enum

# FIXME: These values should be added among the other EthereumNetwork values.
class RSKNetwork(Enum):
    REGTEST = 33
    TESTNET = 31
    MAINET = 30
