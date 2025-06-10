from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from graph import graph
import json
from datetime import datetime
import os

class Ticket(BaseModel):
    required_skills: List[str]
    mode: str
    client_location: str

app = FastAPI()

@app.post("/assign")
def assign_technician(ticket: Ticket):
    state = {"ticket": ticket.dict()}
    result = graph.invoke(state)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("saved_data", exist_ok=True)

    # Save claim
    with open(f"saved_data/claim_{timestamp}.json", "w") as f:
        json.dump(ticket.dict(), f, indent=2)

    # Save assigned technician
    with open(f"saved_data/assigned_{timestamp}.json", "w") as f:
        json.dump(result.get("selected", {}), f, indent=2)

    return {"assigned": result.get("selected")}
