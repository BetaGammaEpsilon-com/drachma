class User():
    
    def __init__(self, name, uid=None, balance=0.0):
        """
        Defines a User in the `users` table.

        Args:
            name (string): the User's name
            uid (integer, optional): The User ID of a processed User
            balance (integer, optional): The initial balance of the User. Defaults to 0.0.
        """
        self.name = name
        self.balance = balance
        
        if uid:
            self.uid = uid
        
        # table name listed with this entry
        self.tbl = 'users'
        
        # table columns to insert into
        self.cols = [
            'name',
            'balance'
        ]
        
    def __str__(self):
        return f'<User: NAME: {self.name}, BALANCE: {self.balance}>'

    def sqlify(self):
        """
        Turns the given Entry into a formatted SQL string to be inserted or updated.

        Returns:
            string: The SQL columns insert formatted string
            string: The SQL values insert formatted string
        """      
        col_sql = ', '.join(self.cols)
        val_sql = f"'{self.name}', {self.balance}"
        return col_sql, val_sql