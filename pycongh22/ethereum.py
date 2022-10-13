
from bip_utils import Bip32Slip10Secp256k1
from eth_account import Account
import requests

class Ethereum:
    
    name = 'ethereum'  
    
    @property
    def address(self) -> str:
        account = Account.from_key(self._private_key)
        return account.address
    
    @property
    def private_key(self) -> str:
        account = Account.from_key(self._private_key)
        return account.privateKey
    
    def seed(self, seed_bytes: str):
        ETHEREUM_PATH = "m/44'/60'/0'/0/0"
        bip32_ctx = Bip32Slip10Secp256k1.FromSeedAndPath(seed_bytes, ETHEREUM_PATH)
        self._private_key = bip32_ctx.PrivateKey().Raw().ToHex()
    
    @property
    def balance(self) -> str:
        r = requests.get(f'https://api-sepolia.etherscan.io/api?module=account&action=balance&address={self.address}&tag=latest')
        return int(r.json()['result'])/1000000000000000000
    
    @property
    def transactions(self) -> str:
        r = requests.get(f'https://api-sepolia.etherscan.io/api?module=account&action=txlist&address={self.address}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc')
        return r.json()['result']
    
    def send(self, to_address: str, amount: str):
        return ""