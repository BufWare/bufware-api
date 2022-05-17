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
