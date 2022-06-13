from datetime import datetime
from api.models.txstatus import TxStatus

class Transaction():

    def __init__(self, uid, price, status, txid=None, tx_date=None, motion='NULL', description='NULL', description_url='NULL'):
        """
        Defines a Transaction in the `tx` table.

        Args:
            uid (integer): The User ID the Transaction is under
            price (float): The price of the Transaction
            status (integer): The verification status of the Transaction
            txid (integer, optional): The Transaction ID of a processed Transaction
            motion (string): The motion to file the Transaction under. Defaults to 'NULL'.
            description (string, optional): A description of the Transaction. Defaults to 'NULL'.   
            description_url (string, optional): When an image is attached, this parameter describes the location of said image  
        """
        self.uid = uid
        self.price = price
        
        if status == 0:
            self.status = TxStatus.UNVERIFIED
        elif status == 1:
            self.status = TxStatus.VERIFIED
            
        self.motion = motion
        self.description = description
        self.description_url = description_url
        
        # table name listed with this entry
        if self.status == TxStatus.VERIFIED:
            self.tbl = 'tx'
        else:
            self.tbl = 'tx_unverified'
            
        self.txid = txid
        
        self.tx_date = tx_date
        
        # table columns to insert into
        self.cols = [
            'uid',
            'tx_date',
            'price',
            'motion',
            'description',
            'description_url'
        ]

        if self.txid:
            self.cols.insert(0, 'txid')
        
    def __str__(self):
        return f'<Transaction: UID: {self.uid}, PRICE: {self.price}, VERIFICATION: {self.status}>'

    def serialize(self):
        """
        Turns a Transaction's data into a dictionary for passing to the frontend.

        Returns:
            dict: The values of this Transaction
        """     
        return {
            'txid': self.txid,
            'uid': self.uid,
            'tx_date': datetime.strftime(self.tx_date, '%Y-%m-%d %H:%M:%S'),
            'price': self.price,
            'motion': self.motion,
            'description': self.description
        }

    def sqlify(self):
        """
        Turns the given Entry into a formatted SQL string to be inserted or updated.

        Returns:
            string: The SQL columns insert formatted string
            string: The SQL values insert formatted string
        """        
        col_sql = ', '.join(self.cols)
        if self.txid:
            val_sql = f'{self.txid}, '
        else:
            val_sql = ''
        val_sql += f'{self.uid}, '
        if self.tx_date:
            val_sql += f"'{self.tx_date}', "
        else:
            val_sql += "datetime('now'), "
        val_sql += f'{self.price}, '
        if not self.motion == 'NULL':
            val_sql += f"'{self.motion}', "
        else:
            val_sql += f'NULL, '
        if not self.description == 'NULL':
            val_sql += f"'{self.description}'"
        else:
            val_sql += f'NULL'
        if not self.description_url == 'NULL':
            val_sql += f"'{self.description_url}'"
        else:
            val_sql += f'NULL'
        return col_sql, val_sql

    def verify(self):
        self.status = TxStatus.VERIFIED
        self.tbl = 'tx'