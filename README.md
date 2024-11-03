# Access SQLite DB using Python

So, we are using 4 different methods.
1. `cursor()` : returns a "Cursor" object which uses this connection with db.
2. `commit()` : Explicitly commit any pending transaction to db.
3. `rollback()` : cause a transaction to be rolled back to the starting point.
4. `close()` : close the connection to the database permanently.

