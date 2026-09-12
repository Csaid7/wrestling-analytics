from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

# initialize instance of FastAPI class
app = FastAPI()
# Wrestler class definition
class Wrestler(BaseModel):
    name: str
    weight_class: int
    id: int

class Match(BaseModel):
     wrestler_id : int
     opponnent_id : int
     wreslter_score : int
     opponnent_score : int
     takedowns : int
     escapes: int
     reversals : int
     near_fall_point : int
     id : int
matches = []
@app.post("/matches")
def create_match(match: Match):
    wrestler = None 
    for w in wrestlers:
        if w.id == match.wrestler_id:
            wrestler = w
    opponent = None
    for opp in wrestlers:
        if opp.id == match.opponnent_id:
            opponent = opp
    if wrestler.weight_class != opponent.weight_class:
        raise HTTPException(status_code= 400, detail = "Wrestlers must be in the same weight Class")     
    match.id = len(matches) + 1 
    matches.append(match)
    return match 

@app.get("/")
def wrestler():
    return { "status": "ok"}

wrestlers = [] 
# store a wreslter in a list 
@app.post("/wrestlers")
def store_Wrestler(wrestler : Wrestler):
    wrestler.id = len(wrestlers) + 1
    wrestlers.append(wrestler)
    return wrestler
# return list of all wrestlers
@app.get("/wrestlers")
def get_wrestlers():
    return wrestlers
# return list of all matches
@app.get("/matches")
def get_matches():
    return matches



