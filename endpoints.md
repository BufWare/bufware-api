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
  "nazev": "Kofola 0,5L",
  "cena": 27.5,
  "popis": "Dobrý sladký nápoj",
  "kategorie": [1, 15, 45]
}
```

Returns:

```json
{
  "res": {
    "id": 1,
    "nazev": "Kofola 0,5L",
    "cena": 27.5,
    "popis": "Dobrý sladký nápoj",
    "skryty": false
  }
}
```

### `HTTP POST /order`

Data:

```json
{
    "produkty": [
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
    "cena": 54.95,
    "stav": 0,
    "timestamp": ...
  }
}
```

### `HTTP GET /menu`

Returns:

```json
{
    "res":[
        {
            "nazev": "Kofola",
            "cena": 0,
            "popis": "Dobrý sladký nápoj",
            "skryty": false,
            "id": 1,
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

### `HTTP POST /category`


Data

```json
{
  "nazev": "Sladké"
}
```

Returns
```json
{
  "res": {
    "id": 1,
    "nazev": "Sladké"
  }
}
```

### `HTTP POST /state`

Data:
```json
{
  "objednavka": 1,
  "stav": 2
}
```

Returns: nothing
