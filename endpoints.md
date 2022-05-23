# Endpoints

### `HTTP GET /overview`

Returns:

```json
{
    "res":[
        {
            "id": 1,
            "stav": 0
        },
        ...
    ]
}
```
### `HTTP POST /order`

Data:
```json
{
    "data":[
        {
            "id":1,
            "pocet":5
        },
        ...
    ]
}
```

Returns:
```json
{
    "res": {
        "id": 1,
        "price": 54.95
    }
}
```
### `HTTP GET /menu`

URL Params:

- cat: ?int = filter category

Returns:

```json
{
    "res":[
        {
            "nazev": "Kofola",
            "cena": 0,
            "kategorie": [
                {
                    "id": 0,
                    "nazev": "sladké"
                }, ...
            ]

        }, ...
    ]
}
```
