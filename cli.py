# user_prompt = "Enter a todo :"
#
# todo_list = []
# i = 1
#
# while (i<4):
#     todo = input(user_prompt)
#     todo_list.append(todo)
#     i = i + 1
#
# print(todo_list)

#section 4 lecture

#while loop

# todos =[]
#
# while True:
#     option = input("type add, show or exit : ")
#     user_action = option.lower()
#     match user_action:
#         case "add":
#             todo = input("Enter a todo : ")
#             todos.append(todo)
#         case "show":
#             print(todos)
#         case "exit":
#             break
# print("bye!")

#for loop

# todos =[]
#
# while True:
#     option = input("type add, show/display edit or exit : ")
#     user_action = option.strip().lower()
#     match user_action:
#         case "add":
#             todo = input("Enter a todo : ")
#             todos.append(todo)
#         case "show" | "display":
#             for i in todos:
#                 print(i.title())
#         case "edit":
#             number = int(input("enter number todo to edit : "))-1
#             print(number)
#             # number = int(number_selected)-1
#             if number < len(todos):
#                 edited_todo = input("enter edited todo : ")
#                 todos[number] = edited_todo
#                 print("edit complete")
#             else:
#                 print("enter a valid number")
#         case "exit":
#             break
#         case _:
#             print("enter a valid option")
# print("bye!")

#strings

# filenames = ["1.Raw Data.txt","2.Reports.txt","3.Presentations.txt"]
#
# for filename in filenames:
#     filename = filename.replace('.','-',1)
#     print(filename)

#enmumerate
#fstrings
#complete list
#
# todos =[]
#
# while True:
#     option = input("type add, show/display, edit, complete or exit : ")
#     user_action = option.strip().lower()
#     match user_action:
#         case "add":
#             todo = input("Enter a todo : ")
#             todos.append(todo)
#         case "show" | "display":
#             for index,item in enumerate(todos):
#                 print(f"{index+1}-{item}")
#         case "edit":
#             number = int(input("enter number todo to edit : "))-1
#             if number < len(todos):
#                 edited_todo = input("enter edited todo : ")
#                 todos[number] = edited_todo
#                 print("edit complete")
#             else:
#                 print("enter a valid number")
#         case "complete":
#             mark = int(input("enter number todo to mark as complete : "))-1
#             if mark < len(todos):
#                 todos.remove(todos[mark])
#                 print("task completed!")
#             else:
#                 print("enter a valid number")
#         case "exit":
#             break
#         case _:
#             print("enter a valid option")
# print("bye!")

#todo files

# while True:
#     option = input("type add, show/display, edit, complete or exit : ")
#     user_action = option.strip().lower()
#     match user_action:
#         case "add":
#             todo = input("Enter a todo : ") + "\n"
#
#             file = open('files/todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
#
#             todos.append(todo)
#
#             file = open('files/todos.txt', 'w')
#             todos = file.writelines(todos)
#             file.close()
#
#         case "show" | "display":
#
#             file = open('files/todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
#             #print(todos)
#             for index,item in enumerate(todos):
#                 item = item.strip('\n')
#                 print(f"{index+1}-{item}")
#
#         case "edit":
#             number = int(input("enter number todo to edit : "))-1
#             if number < len(todos):
#                 edited_todo = input("enter edited todo : ")
#                 todos[number] = edited_todo
#                 print("edit complete")
#             else:
#                 print("enter a valid number")
#         case "complete":
#             mark = int(input("enter number todo to mark as complete : "))-1
#             if mark < len(todos):
#                 todos.remove(todos[mark])
#                 print("task completed!")
#             else:
#                 print("enter a valid number")
#         case "exit":
#             break
#         case _:
#             print("enter a valid option")
# print("bye!")

#coding exercise 5

# name = input("enter a new member name : ")
# file = open('files/members.txt', 'r')
# mem_names = file.readlines()
# file.close()
#
# mem_names.append(name)
#
# file = open("files/members.txt", 'w')
# file.writelines(mem_names)
# file.close()

#coding exercise 6

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for items in filenames:
#     file = open(items,'w')
#     file.write('Hello')
#     file.close()

#coding exercise 7
# content =[]
# file = open('files/a.txt','r')
# afile = file.read()
# file.close()
# content.append(afile)
#
# file = open('files/b.txt', 'r')
# bfile = file.read()
# file.close()
# content.append(bfile)
#
# file = open('files/c.txt', 'r')
# cfile = file.read()
# file.close()
# content.append(cfile)
#
# for items in content:
#     print(items)

#zip practice
#
# female = ['phoebe','monica','Rachel','joey']
# male = ['mike','chandler','Ross']
#
# for f, m in zip(female, male):
#     print(f,m)

#absolute path practise

# file = open('/Users/aishwaryasamel/Downloads/sample.txt','w')
# file.write("hello")
# file.close()

#using with context manager better than for because if anything wrong happens,
# but with with it would still close the file

# while True:
#     option = input("type add, show/display, edit, complete or exit : ")
#     user_action = option.strip().lower()
#
#     match user_action:
#
#         case "add":
#
#             todo = input("Enter a todo : ") + "\n"
#
#             with open('files/todos.txt', 'r') as file:
#                 todos = file.readlines()
#             todos.append(todo)
#
#             with open('files/todos.txt', 'w') as file:
#                 todos = file.writelines(todos)
#
#         case "show" | "display":
#
#             with open('files/todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             for index,item in enumerate(todos):
#                 item = item.strip('\n')
#                 print(f"{index+1}-{item}")
#
#         case "edit":
#
#             with open('files/todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             number = int(input("enter number todo to edit : "))-1
#             if number < len(todos):
#                 edited_todo = input("enter edited todo : ")
#                 todos[number] = edited_todo+'\n'
#
#                 with open('files/todos.txt', 'w') as file:
#                     todos = file.writelines(todos)
#
#                 print("edit complete")
#
#             else:
#                 print("enter a valid number")
#
#         case "complete":
#
#             with open('files/todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             mark = int(input("enter number todo to mark as complete : "))-1
#             if mark < len(todos):
#                 todo_to_remove = todos[mark].strip('\n')
#                 #todos.pop(mark) can also be used
#                 todos.remove(todos[mark])
#
#                 with open('files/todos.txt', 'w') as file:
#                     todos = file.writelines(todos)
#
#                 message = f"todo number {mark+1} - {todo_to_remove} marked as complete"
#                 print(message)
#             else:
#                 print("enter a valid number")
#
#         case "exit":
#             break
#
#         #any other case
#         case _:
#             print("enter a valid option")
#
# print("bye!")

#match replaced with if and added try-except.
#docstring explined too and also concept of functions with and without arguments.

# def get_todos(filepath = 'files/todos.txt'):
#     """read a text file and return the list of to-do items
#     """
#     with open(filepath, 'r') as file_local:
#         todos_local = file_local.readlines()
#     return todos_local
#
# # print(help(get_todos))
#
#
# def write_todos(todos_arg, filepath = 'files/todos.txt'):
#     with open(filepath, 'w') as file:
#         file.writelines(todos_arg)
#
#
# while True:
#     option = input("type add, show/display, edit, complete or exit : ")
#     user_action = option.strip().lower()
#
#     if user_action == "add":
#
#         todo = input("Enter a todo : ") + "\n"
#         todos = get_todos()
#         todos.append(todo)
#         write_todos(todos)
#
#     if user_action == "show" or "display":
#
#         todos = get_todos()
#
#         for index,item in enumerate(todos):
#             item = item.strip('\n')
#             print(f"{index+1}-{item}")
#
#     if user_action == "edit":
#
#         todos = get_todos()
#         number = int(input("enter number todo to edit : "))-1
#
#         try:
#             edited_todo = input("enter edited todo : ")
#             todos[number] = edited_todo+'\n'
#
#             write_todos(todos)
#
#             print("edit complete")
#
#         except IndexError:
#             print("enter a valid number")
#             continue
#
#         # except ValueError:
#         #     print("enter number from the list")
#         #     continue
#
#         # except:
#         #     print("enter a valid number")
#         #     continue
#
#     if user_action == "complete":
#
#         todos = get_todos()
#         mark = int(input("enter number todo to mark as complete : "))-1
#
#         try:
#             todo_to_remove = todos[mark].strip('\n')
#             #todos.pop(mark) can also be used
#             todos.remove(todos[mark])
#
#             write_todos(todos)
#
#             message = f"todo number {mark+1} - {todo_to_remove} marked as complete"
#             print(message)
#
#         except IndexError:
#             print("enter a valid number")
#
#     if user_action == "exit":
#         break
#
# print("bye!")

#docstrings
# text1 = "\
# multiple lines can be written like this \n \
# but you will have to write like this. \n \
# "
# text2 = """
# instead writing like this is better."
# and easier too!
# """
#
# print(text1)
# print(text2)


#function definition outisde in a seperate file
# importance of __name__
# import functions
# #from functions import get_todos, write_todos
#
# while True:
#     option = input("type add, show/display, edit, complete or exit : ")
#     user_action = option.strip().lower()
#
#     if user_action == "add":
#
#         todo = input("Enter a todo : ") + "\n"
#         todos = functions.get_todos()
#         todos.append(todo)
#         functions.write_todos(todos)
#
#     if user_action == "show" or "display":
#
#         todos = functions.get_todos()
#
#         for index,item in enumerate(todos):
#             item = item.strip('\n')
#             print(f"{index+1}-{item}")
#
#     if user_action == "edit":
#
#         todos = functions.get_todos()
#         number = int(input("enter number todo to edit : "))-1
#
#         try:
#             edited_todo = input("enter edited todo : ")
#             todos[number] = edited_todo+'\n'
#
#             functions.write_todos(todos)
#
#             print("edit complete")
#
#         except IndexError:
#             print("enter a valid number")
#             continue
#
#         # except ValueError:
#         #     print("enter number from the list")
#         #     continue
#
#         # except:
#         #     print("enter a valid number")
#         #     continue
#
#     if user_action == "complete":
#
#         todos = functions.get_todos()
#         mark = int(input("enter number todo to mark as complete : "))-1
#
#         try:
#             todo_to_remove = todos[mark].strip('\n')
#             #todos.pop(mark) can also be used
#             todos.remove(todos[mark])
#
#             functions.write_todos(todos)
#
#             message = f"todo number {mark+1} - {todo_to_remove} marked as complete"
#             print(message)
#
#         except IndexError:
#             print("enter a valid number")
#
#     if user_action == "exit":
#         break
#
# print("bye!")

#python.org
#python datetimme format code
# import functions
#
# while True:
#     option = input("type add, show/display, edit, complete or exit : ")
#     user_action = option.strip().lower()
#
#     if user_action == "add":
#
#         todo = input("Enter a todo : ") + "\n"
#         todos = functions.get_todos()
#         todos.append(todo)
#         functions.write_todos(todos)
#
#     if user_action == "show" or "display":
#
#         todos = functions.get_todos()
#
#         for index,item in enumerate(todos):
#             item = item.strip('\n')
#             print(f"{index+1}-{item}")
#
#     if user_action == "edit":
#
#         todos = functions.get_todos()
#         number = int(input("enter number todo to edit : "))-1
#
#         try:
#             edited_todo = input("enter edited todo : ")
#             todos[number] = edited_todo+'\n'
#
#             functions.write_todos(todos)
#
#             print("edit complete")
#
#         except IndexError:
#             print("enter a valid number")
#             continue
#
#         # except ValueError:
#         #     print("enter number from the list")
#         #     continue
#
#         # except:
#         #     print("enter a valid number")
#         #     continue
#
#     if user_action == "complete":
#
#         todos = functions.get_todos()
#         mark = int(input("enter number todo to mark as complete : "))-1
#
#         try:
#             todo_to_remove = todos[mark].strip('\n')
#             #todos.pop(mark) can also be used
#             todos.remove(todos[mark])
#
#             functions.write_todos(todos)
#
#             message = f"todo number {mark+1} - {todo_to_remove} marked as complete"
#             print(message)
#
#         except IndexError:
#             print("enter a valid number")
#
#     if user_action == "exit":
#         break
#
# print("bye!")



