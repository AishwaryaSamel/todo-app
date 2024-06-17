#we are using streamlit library. easy to create webpps, intuitive, easy to integrate with graphs. so easy to make graphs and data.
import streamlit as st
from function import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my todo app")
st.write("This app is designed to increase one's productivity.")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new todo...", on_change=add_todo, key="new_todo")

# st.session_state





