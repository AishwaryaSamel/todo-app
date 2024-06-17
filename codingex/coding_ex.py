import time
from function import functions
import FreeSimpleGUI as sg

# pip/ pip3 install FreeSimpleGUI on terminal will also install it
#or else go to pycharm -> preferences -> project name -> interpreter -> + -> FreeSimpleGUI -> install package

sg.theme("GreenMono")
date_label = sg.Text('',key="date_label")
todo_label = sg.Text("Type in a to-do")

input_box = sg.InputText(tooltip = "Enter a todo", key = "todo")
add_button = sg.Button(key="Add",size=10, image_source="add.png",mouseover_colors="blue", tooltip="add todo")

list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events = True, size =[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(key="Complete",size=10, image_source="complete.png", tooltip="mark as complete")
exit_button = sg.Button("Exit")
message_label = sg.Text(key="message", text_color="white")

layout = [[date_label],[todo_label],[input_box,add_button],[list_box,edit_button],[complete_button,exit_button,message_label]]
window = sg.Window('My To-Do App', layout=layout, font = ("Helvetica",20))

while True:
    #below line will give per second timer
    # event, values = window.read(timeout=1000)
    event, values = window.read()
    window['date_label'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    print(event)
    print(values)
    print(values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                # window["message"].update(value="Please select an item first")
                # print("Please select an item first")
                sg.popup("Please select an item first", font=("Helvetica",20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                # window["message"].update(value="Please select an item first")
                # print("Please select an item first")
                sg.popup("Please select an item first", font=("Helvetica",20))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case  sg.WIN_CLOSED:
            break
            # exit()
#exit completely stops the program so bye wont be printed. but break will just go out of the loop
# print("Bye")
window.close()