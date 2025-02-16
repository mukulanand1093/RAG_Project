
#======Request Models========

from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str
