from bip_utils import Bip32Slip10Secp256k1
from eth_account import Account
import requests
import web3


class Ethereum:

    name = "ethereum"

    @property
    def address(self) -> str:
        account = Account.from_key(self._private_key_raw)
        return account.address

    @property
    def private_key(self) -> str:
        account = Account.from_key(self._private_key_raw)
        return account.privateKey

    def seed(self, seed_bytes: str):
        ETHEREUM_PATH = "m/44'/60'/0'/0/0"
        bip32_ctx = Bip32Slip10Secp256k1.FromSeedAndPath(seed_bytes, ETHEREUM_PATH)
        self._private_key_raw = bip32_ctx.PrivateKey().Raw().ToHex()

    @property
    def balance(self) -> str:
        r = requests.get(
            f"https://api-sepolia.etherscan.io/api?module=account&action=balance&address={self.address}&tag=latest"
        )
        return int(r.json()["result"]) / 1000000000000000000

    @property
    def transactions(self) -> str:
        r = requests.get(
            f"https://api-sepolia.etherscan.io/api?module=account&action=txlist&address={self.address}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc"
        )
        return r.json()["result"]

    def send(self, to_address: str, amount: str):
        w3 = web3.Web3(web3.Web3.HTTPProvider('https://sepolia.infura.io/v3/82de4c56f4364dd899635d8ebbc349cc'))
        nonce = web3.eth.get_transaction_count(self.address)
        trx = {
            'to': web3.toChecksumAddress(to_address),
            'value': w3.to_wei(float(amount), 'ether'),
            'gasPrice': web3.to_wei(50, 'gwei'), 
            'nonce': nonce,
            'gas': 100000,
            'chainId': 11155111
        }
        signed_tx = web3.eth.account.sign_transaction(trx, self.private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash
        
