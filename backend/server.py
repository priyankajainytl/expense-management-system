from fastapi import FastAPI
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper
app = FastAPI()


class Expense(BaseModel):
    id: int
    amount: float
    category: str
    notes: str

@app.get("/")
def hello():
   return "Hello there"

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date:date):
   expenses=db_helper.fetch_expenses_for_date(expense_date)
   return expenses

@app.get("/expenses/v1/{expense_date}")
def get_expenses(expense_date:date):
   expenses=db_helper.fetch_expenses_for_date(expense_date)
   return expenses

#async def app(scope, receive, send):
 #   assert scope['type'] == 'http'

  #  await send({
   #     'type': 'http.response.start',
    #    'status': 200,
     #   'headers': [
      #      [b'content-type', b'text/plain'],
       # ],
    #})
    #await send({
     #   'type': 'http.response.body',
      #  'body': b'Hello, world!',
  #  })'