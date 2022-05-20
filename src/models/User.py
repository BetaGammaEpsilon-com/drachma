class User:
    
    def __init__(self, uid, name):
        """
        Defines a User in the `users` table.

        Args:
            uid (integer): the User's ID
            name (string): the User's name
        """
        self.uid = uid
        self.name = name

    def sqlify(self):
        """
        Turns a User into a SQL insert statement.
        """
        pass