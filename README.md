```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# run flask
python3 main.py
```

## ENDPOINTS

# GET /api/stories/<id>

`http://127.0.0.1:8080/api/stories/cd9cbb86-9535-4a82-a554-5d7b794e7b4e`

---

# POST /api/stories<generate>

`http://127.0.0.1:8080/api/stories/generate`

## DTO:

```json
{
  "storyStyle": "Drama",
  "imagesStyle": "Cinematic",
  "duration": "5",
  "actress": "DiCaprio"
}
```
