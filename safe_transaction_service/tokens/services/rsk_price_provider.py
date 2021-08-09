from safe_transaction_service.utils.rsk import RSKNetwork
from eth_typing.evm import ChecksumAddress
from gnosis.eth.ethereum_client import EthereumNetwork
from gnosis.eth.oracles.oracles import PriceOracle, UsdPricePoolOracle
from safe_transaction_service.tokens.clients.coingecko_client import CoingeckoClient


class RSKPriceProvider(PriceOracle, UsdPricePoolOracle):
    TRIF_ADDRESS = '0x19f64674d8a5b4e652319f5e239efd3bc969a1fe'
    RIF_ADDRESS = '0x2acc95758f8b5f583470ba265eb685a8f45fc9d5'

    def __init__(self, ethereum_network: int):
        self.ethereum_network = ethereum_network
        self.coingecko_client = CoingeckoClient()

    def get_rbtc_usd_price(self) -> float:
        return self.coingecko_client.get_rbtc_usd_price()
    
    def _is_rif_or_trif(self, token_address):
        token_address_lower = token_address.lower()
        return (self.ethereum_network == RSKNetwork.TESTNET.value and token_address_lower == self.TRIF_ADDRESS) \
            or (self.ethereum_network == RSKNetwork.MAINET.value and token_address_lower == self.RIF_ADDRESS)

    def get_price(self, token_address):
        if self._is_rif_or_trif(token_address):
            return self.coingecko_client.get_rif_btc_price()
        # FIXME: Add suport for other tokens
        return 0.
    
    def get_pool_usd_token_price(self, pool_token_address: ChecksumAddress) -> float:
        if self._is_rif_or_trif(pool_token_address):
            return self.coingecko_client.get_rif_usd_price()
        return 0.
