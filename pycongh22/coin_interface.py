class Coin:

    name = "coin"

    @property
    def address(self) -> str:
        return ""

    @property
    def private_key(self) -> str:
        return self._private_key_raw

    def seed(self, seed_bytes: str):
        self._private_key_raw = seed_bytes

    @property
    def balance(self) -> str:
        return ""

    @property
    def transactions(self) -> str:
        return ""

    def send(self, to_address: str, amount: str):
        return ""
