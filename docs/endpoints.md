# Endpoints

<!-- TODO -->
[Postman](#)

Guide for endpoints and their logic. In a change to an endpoint _UPDATE THIS FILE BEFORE COMMIT_.

## Home and Tests
`GET /`

Home dashboard with login info for treasurer(?).

<hr />

`GET /version`

Testing endpoint. Should return current release verison of Drachma in body (ex. `{'version': '1.0.0'}`).

## Users

`GET /user/<uid>` OR
`GET /user/<name>` -> `REDIRECT` to `/user/<uid>`

Displays all listed transactions of the user, separated by verification status.

<hr />

`POST /<uid>/tx`

Request Body:

```
{
    'uid': <uid>,
    'price': <float>,
    'status': 0,
    'motion': <string>,
    'description': <string>
}
```

Adds a transaction to the unverified table from `uid` for the treasurer to view.

## Treasurer

`GET /tres`

Displays all transactions for the treasurer to see. Homepage for all Drachma capabilities. Spending visualizations and metrics displayed here.

<hr />

`GET /tres/report`

Separate page where the treasurer report (given current information) can be saved.

<hr />

`POST /tres/tx`

Request Body:

```
{
    'uid': <uid>,
    'price': <float>,
    'status': 1,
    'motion': <string>,
    'description': <string>
}
```

Adds a transaction to the verified table given a `uid`.

<hr />

`PUT /tres/<txid>`

Request Body:

```
{
    'txid': <txid>
    'uid': <uid>,
    'price': <float>,
    'status': 1,
    'motion': <string>,
    'description': <string>
}
```

Updates transaction `txid` to have the given parameters. On update of any parameters other than `status`, `tx_date` changed to datetime of update. Mainly used for status changes alone.

<hr />

`DELETE /tres/<txid>`

Deletes transaction `txid` from verified or unverified table, whichever it exists on.

<hr />

## Login

_TODO_