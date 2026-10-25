from pydantic import BaseModel


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
