# Tables
## users
| key      | type    | description |
|:---|:---:|---:| 
| uid      | integer | primary key |
| name     | text    | unique identifier for users to use |
| balance  | float   | how much money the user owes/or is owed |

## tx
#### transactions and relevant information (tx_unverified is the same but for transactions the treasurer has yet to approve)

| key    |   type   |                                               description |
|:-------|:--------:|----------------------------------------------------------:| 
| txid   | integer  |                                     Primary key for table |
| uid    | integer  |                      User that the transaction applies to |
| txdate | datetime | Date and time of the transaction being added to the table |
| price  |  float   |                                  Price of the transaction |
| motion |   text   |                    Motion associated with the Transaction |


