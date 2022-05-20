from enum import Enum

class TxStatus(Enum):
    UNVERIFIED = 0
    VERIFIED = 1

    def assign(self, num):
        if num == 0:
            return self.UNVERIFIED
        elif num == 1:
            return self.VERIFIED