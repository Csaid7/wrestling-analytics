from fastapi import APIRouter, HTTPException

from app.models import Match
from app.routers.wrestlers import wrestlers

router = APIRouter()

matches = []


@router.post("/matches")
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


# return list of all matches
@router.get("/matches")
def get_matches():
    return matches
