import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_category_tab

API_URL="http://localhost:8000"

st.title("Expense Managment System")

tab1,tab2 =st.tabs(["Add/Update","Analytics"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()