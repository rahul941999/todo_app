import streamlit as st
import functions


todos = functions.read()
st.title("My Todo App")
st.subheader("This is the Subheader")
st.write("This is the write Block.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo :", placeholder="Add a new todo..",
              label_visibility="hidden")
print("hello")
