# Tables
## users
#### User information
| Column   | Type    | Description |
|:---:|:---:|:---| 
| uid      | integer | Primary Key |
| name     | text    | unique identifier for Users to use |
| balance  | float   | how much money the User owes/or is owed |

## tx
#### Verified Transactions

| Column |   Type   |                                               Description |
|:------:|:--------:|:---------------------------------------------------------| 
| txid   | integer  |                                               Primary Key |
| uid    | integer  |                      User that the Transaction applies to |
| txdate | datetime | Date and time of the Transaction being added to the table |
| price  |  float   |                                  Price of the Transaction |
| motion |   text   |                    Motion associated with the Transaction |
| description | text | An optional description of the motion |
| description_url | text | A URL describing where a receipt for this object is stored |

## tx_unverified
#### Unverified Transactions

| Column |   Type   |                                               Description |
|:------:|:--------:|:---------------------------------------------------------| 
| txid   | integer  |                                     Primary key for table |
| uid    | integer  |                      User that the Transaction applies to |
| txdate | datetime | Date and time of the Transaction being added to the table |
| price  |  float   |                                  Price of the Transaction |
| motion |   text   |                    Motion associated with the Transaction |
| description | text | An optional description of the motion |
| description_url | text | A URL describing where a receipt for this object is stored |

## motions
#### Motion information

| Column   | Type    | Description |
|:---:|:---:|:---| 
| motion | text | The name of the Motion |
| init_date | datetime | Timestamp when Motion was created |