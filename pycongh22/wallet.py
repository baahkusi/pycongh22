from bip_utils import Bip39SeedGenerator, Bip39MnemonicGenerator, Bip39Languages, Bip39WordsNum
from pycongh22.bitcoin import Bitcoin
from pycongh22.coin_interface import Coin
from pycongh22.ethereum import Ethereum
from pycongh22.tezos import Tezos


class Wallet:
    
    coins: list[Coin] = [
        Tezos,
        Bitcoin,
        Ethereum
    ]
    
    mnemonics = ''
    
    def __init__(self, mnemonics: str):
        for c in self.coins:
            c.seed(self._getseed(mnemonics))
    
    def _getseed(self, mnemonics: str):
        if mnemonics is None or mnemonics == '':
            random_mnemonics = Bip39MnemonicGenerator(Bip39Languages.ENGLISH).FromWordsNumber(Bip39WordsNum.WORDS_NUM_12).ToStr()
            seed_bytes = Bip39SeedGenerator(random_mnemonics).Generate()
        else:
            seed_bytes = Bip39SeedGenerator(mnemonics).Generate()
        return seed_bytes
