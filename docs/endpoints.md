# Endpoints

[Postman](https://www.postman.com/aviation-pilot-81500845/workspace/drachma/overview)


Guide for endpoints and their logic. In a change to an endpoint **UPDATE THIS FILE BEFORE COMMIT**. _Italicized_ routes have not been implemented at all yet.

## Home and Tests

#### Endpoints written in `/app/routes/home.py`

<hr />

`GET /`

Home dashboard with login info for treasurer(?).

<hr />

`GET /version`


Testing endpoint. Should return current release verison of Drachma in body (ex. `{'version': '1.0.0'}`).

## Users

#### Endpoints written in `/app/routes/user.py`

<hr />

_`GET /user`_

Gets a list of all Users.

`POST /user`

Adds a User to the `users` table.

Sample Request Body:
```json
{
    "name": "string", // (str) The User's unique name
    "balance": 0.0    // (float) the User's balance
}
```

Sample Responses:

On succesful User Creation `STATUS CODE: 200`
```json
{ "message": "New user created successfully." }
```

On invalid request `STATUS CODE: 400`
```json
{ "error": "BAD REQUEST: Error in creating new user -- request must include `name` and `balance` fields." }
```

On insertion error `STATUS CODE: 403`
```json
{ "error": "BAD REQUEST: `name` parameter must be unique." }
```

<hr />

`GET /user/<uid>`

Displays all listed transactions of the user, separated by verification status.

<hr />

`POST /user/<uid>/tx`

Request Body:

```json
{
    "price": 0.0,     // (float) price of the Transaction
    "motion": "",     // (str, optional) the motion this Transaction is under
    "description": "" // (str, optional) a description of this Transaction
}
```

Adds a transaction to the unverified table from `uid` for the treasurer to view.

## Treasurer

#### Endpoints written in `/app/routes/treasurer.py`

<hr />

`GET /tres`

Returns all transactions for the treasurer to see, totals for each verification and overall. (_TODO_ more metrics)

<hr />

_`GET /tres/visualize`_

Creates spending visualizations.

<hr />

`GET /tres/report`

Separate page where the treasurer report (given current information) can be saved.

<hr />

`POST /tres/tx`

Sample Request Body:

```json
{
    "uid": 0,         // (int) UID of the User
    "price": 0.0,     // (float) price of the Transaction
    "motion": "",     // (str, optional) the motion this Transaction is under
    "description": "" // (str, optional) a description of this Transaction
}
```

Adds a transaction to the verified table given a `uid`.

<hr />

_`GET /tres/tx/<txid>`_

Returns information about the given transaction

_`PUT /tres/tx/<txid>`_

Sample Request Body:

```json
{
    "uid": 0,         // (int) UID of the User
    "price": 0.0,     // (float) price of the Transaction
    "status": 1,      // (int) verification status: 1 is verified, 0 is unverified (new Treasurer transactions are automatically verified)
    "motion": "",     // (str, optional) the motion this Transaction is under
    "description": "" // (str, optional) a description of this Transaction
}
```

Updates transaction `txid` to have the given parameters. On update of any parameters other than `status`, `tx_date` changed to datetime of update. Mainly used for status changes alone.

_`DELETE /tres/tx/<txid>`_

Deletes transaction `txid` from verified or unverified table, whichever it exists on.

<hr />

`GET /tres/motion`

Returns all available motions.

`POST /tres/motion`

Adds a motion.

Sample Request Body:
```json
{
    "motion": "eboard"
}
```

`DELETE /tres/motion`

Deletes a motion.

Sample Request Body:
```json
{
    "motion": "eboard"
}
```

<hr />

## Login

<hr />

_TODO_