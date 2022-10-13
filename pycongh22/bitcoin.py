from bip_utils import Bip32Slip10Secp256k1
from bitcoin.wallet import CBitcoinSecret, CBech32BitcoinAddress, P2WPKHBitcoinAddress, CBitcoinAddress
from bitcoin.core.script import CScript,OP_0
from bitcoin.core import Hash160

class Bitcoin:
    
    name = 'bitcoin'  
    
    @property
    def address(self) -> str:
        account = CBitcoinSecret.from_secret_bytes(self._private_key_raw)
        script_pubkey = CScript([OP_0, Hash160(account.pub)])
        return CBech32BitcoinAddress.from_scriptPubKey(script_pubkey)
    
    @property
    def private_key(self) -> str:
        account = CBitcoinSecret.from_secret_bytes(self._private_key_raw)
        return account.hex()
    
    def seed(self, seed_bytes: str):
        BITCOIN_PATH_SEGWIT = "m/84'/0'/0'/0/0"
        bip32_ctx = Bip32Slip10Secp256k1.FromSeedAndPath(seed_bytes, BITCOIN_PATH_SEGWIT)
        self._private_key_raw = bip32_ctx.PrivateKey().Raw().ToBytes()
    
    @property
    def balance(self) -> str:
        return ""
    
    @property
    def transactions(self) -> str:
        return ""
    
    def send(self, to_address: str, amount: str):
        return ""