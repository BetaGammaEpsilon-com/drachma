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
        self.uid = uid
        self.balance = balance
        
        # table name listed with this entry
        self.tbl = 'users'
        
        # table columns to insert into
        self.cols = [
            'name',
            'balance'
        ]
        
    def __str__(self):
        return f'<User: UID: {self.uid}, NAME: {self.name}, BALANCE: {self.balance}>'
    
    def serialize(self):
        """
        Turns a User's data into a dictionary for passing to the frontend.

        Returns:
            dict: The values of this User
        """        
        return {
            'uid': self.uid,
            'name': self.name,
            'balance': self.balance
        }

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

    def markdownify(self):
        """
        Turns the given Entry into a formatted Markdown string to be added to a table

        Returns:
            string: The formatted markdown string
        """

        md = f"| {self.name} | {self.balance} |"
        return md
