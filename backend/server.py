from fastapi import FastAPI
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper

app = FastAPI()

# Base model for Expense
class Expense(BaseModel):
    id: int
    amount: float
    category: str
    notes: str

@app.get("/")
def hello():
   return "Hello there"

# Endpoint to get expense for a specific date
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date:date):
   expenses=db_helper.fetch_expenses_for_date(expense_date)
   return expenses

# Endpoint to 