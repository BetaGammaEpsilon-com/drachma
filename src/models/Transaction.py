from datetime import datetime
from src.models import TxStatus

class Transaction:

    def __init__(
        self, 
        txid,
        uid,
        price,
        status,
        motion=None,
        description=None  
        ):
        """
        Defines a Transaction in the `tx` table.

        Args:
            txid (integer): The Transaction ID
            uid (integer): The User ID the Transaction is under
            price (float): The price of the Transaction
            status (integer): The verification status of the Transaction
            motion (string, optional): The motion to file the Transaction under. Defaults to None.
            description (string, optional): A description of the Transaction. Defaults to None.     
        """
        self.txid = txid
        self.uid = uid
        self.tx_date = datetime.now()
        self.price = price
        self.status = TxStatus.assign(status)
        self.motion = motion
        self.description = description

    def sqlify(self):
        """
        Turns a Transaction into a SQL insert statement.
        """
        pass