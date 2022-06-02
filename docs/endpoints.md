# Endpoints

[Postman](https://www.postman.com/aviation-pilot-81500845/workspace/drachma/overview)


Guide for endpoints and their logic. In a change to an endpoint _UPDATE THIS FILE BEFORE COMMIT_.

## Home and Tests

#### Endpoints written in `/app/routes/home.py`

`GET /`

Home dashboard with login info for treasurer(?).

<hr />

`GET /version`


Testing endpoint. Should return current release verison of Drachma in body (ex. `{'version': '1.0.0'}`).

## Users

#### Endpoints written in `/app/routes/user.py`

`POST /user`

Request Body:
```json
{
    'name': <string>,
    'balance': <float>
}
```

Adds a User to the `users` table.

<hr />

`GET /user/<uid>`

Displays all listed transactions of the user, separated by verification status.

<hr />

`POST /user/<uid>/tx`

Request Body:

```json
{
    'price': <float>,
    'motion': <string>,
    'description': <string>
}
```

Adds a transaction to the unverified table from `uid` for the treasurer to view.

## Treasurer

#### Endpoints written in `/app/routes/treasurer.py`

`GET /tres`

Returns all transactions for the treasurer to see, totals for each verification and overall. (_TODO_ more metrics)

<hr />

`GET /tres/visualize`

Creates spending visualizations.

<hr />

`GET /tres/report`

Separate page where the treasurer report (given current information) can be saved.

<hr />

`POST /tres/tx`

Request Body:

```json
{
    'uid': <uid integer>,
    'price': <float>,
    'status': 1,
    'motion': <string>,
    'description': <string>
}
```

Adds a transaction to the verified table given a `uid`.

<hr />

`GET /tres/tx/<txid>`

Returns information about the given transaction

<hr />

`PUT /tres/tx/<txid>`

Request Body:

```json
{
    'txid': <txid integer>
    'uid': <uid integer>,
    'price': <float>,
    'status': 1,
    'motion': <string>,
    'description': <string>
}
```

Updates transaction `txid` to have the given parameters. On update of any parameters other than `status`, `tx_date` changed to datetime of update. Mainly used for status changes alone.

<hr />

`DELETE /tres/tx/<txid>`

Deletes transaction `txid` from verified or unverified table, whichever it exists on.

<hr />

## Login

_TODO_