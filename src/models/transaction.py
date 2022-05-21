from datetime import datetime
from src.models.txstatus import TxStatus

class Transaction():

    def __init__(self, uid, price, status, txid=None, motion='NULL', description='NULL'):
        """
        Defines a Transaction in the `tx` table.

        Args:
            uid (integer): The User ID the Transaction is under
            price (float): The price of the Transaction
            status (integer): The verification status of the Transaction
            txid (integer, optional): The Transaction ID of a processed Transaction
            motion (string, optional): The motion to file the Transaction under. Defaults to 'NULL'.
            description (string, optional): A description of the Transaction. Defaults to 'NULL'.     
        """
        self.uid = uid
        self.price = price
        
        if status == 0:
            self.status = TxStatus.UNVERIFIED
        elif status == 1:
            self.status = TxStatus.VERIFIED
            
        self.motion = motion
        self.description = description
        
        # table name listed with this entry
        if self.status == TxStatus.VERIFIED:
            self.tbl = 'tx'
        else:
            self.tbl = 'tx_unverified'
            
        if txid:
            self.txid = txid
        
        # table columns to insert into
        self.cols = [
            'uid',
            'tx_date',
            'price',
            'motion',
            'description'
        ]
        
    def __str__(self):
        return f'<Transaction: UID: {self.uid}, PRICE: {self.price}, VERIFICATION: {self.status}>'

    def sqlify(self):
        """
        Turns the given Entry into a formatted SQL string to be inserted or updated.

        Returns:
            string: The SQL columns insert formatted string
            string: The SQL values insert formatted string
        """        
        col_sql = ', '.join(self.cols)
        val_sql = f"{self.uid}, datetime('now'), {self.price}, "
        if not self.motion == 'NULL':
            val_sql += f"'{self.motion}', "
        else:
            val_sql += f'NULL, '
        if not self.description == 'NULL':
            val_sql += f"'{self.description}'"
        else:
            val_sql += f'NULL'
        return col_sql, val_sql