from bip_utils import (
    Bip39SeedGenerator,
    Bip39MnemonicGenerator,
    Bip39Languages,
    Bip39WordsNum,
)
from pycongh22.bitcoin import Bitcoin
from pycongh22.coin_interface import Coin
from pycongh22.ethereum import Ethereum
from pycongh22.tezos import Tezos
# from pycongh22.bitcoin import Bitcoin


class Wallet:

    coins: list[Coin] = [Tezos(), Ethereum(), Bitcoin()]

    mnemonics = ""

    def __init__(self, mnemonics: str = ''):
        if mnemonics == "":
            mnemonics = (
                Bip39MnemonicGenerator(Bip39Languages.ENGLISH)
                .FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
                .ToStr()
            )
        seed = Bip39SeedGenerator(mnemonics).Generate()
        self.mnemonics = mnemonics
        print(mnemonics)
        for c in self.coins:
            c.seed(seed)


if __name__ == "__main__":
    wallet = Wallet('chat style uncover beauty federal dish priority best then empty lesson flag')

    for coin in wallet.coins:
        print(coin.address, coin.balance)
