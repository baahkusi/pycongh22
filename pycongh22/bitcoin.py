from bip_utils import Bip32Slip10Secp256k1

class Bitcoin:
    
    name = 'bitcoin'  
    
    @property
    def address(self) -> str:
        return ""
    
    @property
    def private_key(self) -> str:
        account = CBitcoinSecret.from_secret_bytes(self._private_key)
        return account.hex()
    
    def seed(self, seed_bytes: str):
        BITCOIN_PATH_SEGWIT = "m/84'/0'/0'/0/0"
        bip32_ctx = Bip32Slip10Secp256k1.FromSeedAndPath(seed_bytes, BITCOIN_PATH_SEGWIT)
        self._private_key = bip32_ctx.PrivateKey().Raw().ToBytes()
    
    @property
    def balance(self) -> str:
        return ""
    
    @property
    def transactions(self) -> str:
        return ""
    
    def send(self, to_address: str, amount: str):
        return ""