```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# run flask
python3 main.py
```

## ENDPOINTS

# GET `/api/stories/id

`http://127.0.0.1:8080/api/stories/cd9cbb86-9535-4a82-a554-5d7b794e7b4e`

## OUTPUT
```json
{
"content": "# Story\n\n## Chapter 1: The Beginning\n\nOnce upon a time in a faraway land, there lived a brave knight named Sir Arthur. He had a mission to rescue a captured princess from the clutches of an evil dragon.\n\n![Knight](https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg)\n\n---\n\n## Chapter 2: The Quest\n\nTo embark on his quest, Sir Arthur gathered his trusty sword and a suit of shining armor. He knew he would face many challenges along the way.\n\n![Quest](https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg)\n\n---\n\n## Chapter 3: The Encounter\n\nAs Sir Arthur ventured deeper into the dark forest, he encountered a mysterious old wizard who offered him guidance on defeating the dragon.\n\n![Encounter](https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg)\n\n---\n\n## Chapter 4: The Final Battle\n\nAfter a long and perilous journey, Sir Arthur finally reached the dragon's lair. The fierce battle between knight and dragon raged on, and the fate of the princess hung in the balance.\n\n![Battle](https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg)\n\n---\n\n# The End",
"isImagesGenerated": false,
"isTextGenerated": false,
"isVoiceGenerated": false,
"voice": "https://api7.vocalremover.org/split/listen/vocal/80866333/c2a81d"
}
```

---

# POST /api/stories<generate>

`http://127.0.0.1:8080/api/stories/generate`

## INPUT: DTO:

```json
{
  "storyStyle": "Drama",
  "imagesStyle": "Cinematic",
  "duration": "5",
  "actress": "DiCaprio"
}
```

## OUTPUT:

```json
{
    "id": "562828d7-79d6-42fa-a6d0-a3f40b655f92"
}
```
