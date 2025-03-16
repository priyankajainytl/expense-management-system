import streamlit as st
from datetime import datetime
import requests

API_URL="http://localhost:8000"

st.title("Expense Managment System")

tab1,tab2 =st.tabs(["Add/Update","Analytics"])

with tab1:
    selected_date=st.date_input("Enter Date",datetime(2024,8,1),label_visibility="collapsed")
    response=requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code==200:
        existing_expenses=response.json()
        st.write(existing_expenses)
    else:
        st.error("falied to retrieve response")
        existing_expenses=[]