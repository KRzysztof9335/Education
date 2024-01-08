FastApi is a framework for building web API.

# 1. Basics

The very basic example is located [basics_1.py](fastapi/basics_1.py)
To run application do:
```
uvicorn basics_1:app --reload
```

NOTE: Use '--reload' only for development

There are few basic steps:
1. Import FastAPi
1. Create FastApi instance
1. Create a path operation (like @app.get("/"))
1. Define path operation function (like async def root())
1. Return the content


## Path operations

  - GET
  - POST
  - PUT or PATCH
  - DELETE
  - OPTIONS
  - TRACE


**Idempotence** is a property of API operations that ensures repeating the same operation multiple time will have an effect of executing operations once.

**PUT vs PATCH** - use PUT when you want to replace entire object otherwise use PATCH. PUT is idempotent PATCH does not have to be.


# 2. Path parameters with types

To use arguments or variables just modify route in the following way:
```
@app.get("/items/{item_id}")
async def root(item_id: int):
    return {}
```

There is also nice endpoints representation under:
```
http://127.0.0.1:8000/docs#/
```

When creating path operation function, the order they appear in file matter. Like in example:
```
@app.get("/users/me")
...
@app.get("/users/{user_id}")
...
```

# 3. Query parameters

The query is set of key-value parameters that go after '?' and they are separated by '&'.

```
http://127.0.0.1:8000/items/?skip=0&limit=5
```
If parameter is not present in routing function then it is simply ignored without any errors/warnings.

### Multiple path and query parameters

In path they might be many path and query parameters. FastApi will handle them correctly. No specific order is required.


# 4. Request body

What if you want to send some data from user?

request body - data sent from client to server
response body - data sent from server to client

To send data use requests/curl/aiohttp whatever like:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/items/12' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "description": "string",
  "tax": 0
}'
```

You can still combine path and query parameters.
If parameter coming to function is recognized as Pydantic model, it will be mapped as request body.



