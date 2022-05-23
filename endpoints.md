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

### `HTTP POST /product`

Data:

```json
{
  "data": {
    "nazev": "Kofola 0,5L",
    "cena": 27.5,
    "kategorie": [1, 15, 45]
  }
}
```

Returns:

```json
{
  "res": {
    "id": 1,
    "nazev": "Kofola 0,5L",
    "cena": 27.5
  }
}
```

### `HTTP POST /order`

Data:

```json
{
    "data": [
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
    "cena": 54.95
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
