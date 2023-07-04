import deta
from fastapi import FastAPI

from util.secrets import DATA_KEY

app = FastAPI()


@app.get("/highscores")
async def get_high_scores():
    d = deta.Deta(DATA_KEY)
    db = d.Base('FastAPI_data')
    return db.fetch().items


@app.put("/addscore")
async def add_score_to_list(initials: str, score: int):
    """ Add a new score with initials to a list of high scores,
    sort the list in descending order, and keep only the top 10
    scores in the database.
    Inputs:
    - initials: a string representing the initials of the player who achieved the score.
    - score: an integer representing the score achieved by the player. """
    d = deta.Deta(DATA_KEY)
    db = d.Base('FastAPI_data')
    if len(initials) > 0 and score >= 0:
        items = db.fetch().items
        high_scores = []
        if items:
            for item in items.pop()['score_list']:
                high_scores.append((item[1], item[0]))
        high_scores.append((score, initials[:3].upper()))
        high_scores.sort(reverse=True)
        db.put({"score_list": [(item[1], item[0]) for item in high_scores[:10]]},
               "score_list")
    return db.fetch().items


@app.put("/clear")
async def clear_high_score_list():
    d = deta.Deta(DATA_KEY)
    db = d.Base('FastAPI_data')
    for item in db.fetch().items:
        db.delete(item['key'])
    return db.fetch().items
