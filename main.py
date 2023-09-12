from flask import Flask, jsonify

app = Flask(__name__)


story = """# Story

## Chapter 1: The Beginning

Once upon a time in a faraway land, there lived a brave knight named Sir Arthur. He had a mission to rescue a captured princess from the clutches of an evil dragon.

![Knight](https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg)

---

## Chapter 2: The Quest

To embark on his quest, Sir Arthur gathered his trusty sword and a suit of shining armor. He knew he would face many challenges along the way.

![Quest](https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg)

---

## Chapter 3: The Encounter

As Sir Arthur ventured deeper into the dark forest, he encountered a mysterious old wizard who offered him guidance on defeating the dragon.

![Encounter](https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg)

---

## Chapter 4: The Final Battle

After a long and perilous journey, Sir Arthur finally reached the dragon's lair. The fierce battle between knight and dragon raged on, and the fate of the princess hung in the balance.

![Battle](https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg)

---

# The End"""


@app.route('/api/stories/<story_id>', methods=['GET'])
def get_story(story_id):
    data = {
        "isImagesGenerated": False,
        "isTextGenerated": False,
        "isVoiceGenerated": False,
        "content": story,
        "voice": 'https://api7.vocalremover.org/split/listen/vocal/80866333/c2a81d'
    }

    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True, port=8080)
