from bip_utils import Bip32Slip10Ed25519
from pycongh22.coin_interface import Coin
from pytezos.crypto.encoding import base58_encode
from pytezos.crypto import key
from pytezos import pytezos
import requests


class Tezos(Coin):

    name = "tezos"

    @property
    def address(self) -> str:
        account = key.Key.from_encoded_key(self.private_key)
        tezos_address = account.public_key_hash()
        return tezos_address

    @property
    def private_key(self) -> str:
        return base58_encode(bytes.fromhex(self._private_key_raw), prefix=b"edsk")

    def seed(self, seed_bytes: str):
        TEZOS_PATH = "m/44'/1729'/0'/0'"
        bip32_ctx = Bip32Slip10Ed25519.FromSeedAndPath(seed_bytes, TEZOS_PATH)
        self._private_key_raw = bip32_ctx.PrivateKey().Raw().ToHex()

    @property
    def balance(self) -> str:
        r = requests.get(
            f"https://api.ghostnet.tzkt.io/v1/accounts/{self.address}/balance"
        )
        return str(int(r.text) / 1000000)

    @property
    def transactions(self) -> str:
        r = requests.get(
            f"https://api.ghostnet.tzkt.io/v1/accounts/{self.address}/operations"
        )
        return r.json()

    def send(self, to_address: str, amount: str):
        pytezos.pytezos.using(
            shell="https://ghostnet.smartpy.io", key=self.private_key.decode("utf8")
        )
        try:
            pytezos.pytezos.reveal().autofill().sign().inject()
        except:
            pass

        try:
            tx = (
                pytezos.pytezos.transaction(
                    destination=to_address, amount=round((int(amount * 1000000)))
                )
                .autofill()
                .sign()
                .inject()
            )
            return tx["hash"]
        except:
            pass
        return ""
