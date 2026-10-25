from fastapi import APIRouter

from app.models import Wrestler

router = APIRouter()

wrestlers = []


# store a wreslter in a list
@router.post("/wrestlers")
def store_Wrestler(wrestler : Wrestler):
    wrestler.id = len(wrestlers) + 1
    wrestlers.append(wrestler)
    return wrestler


# return list of all wrestlers
@router.get("/wrestlers")
def get_wrestlers():
    return wrestlers
