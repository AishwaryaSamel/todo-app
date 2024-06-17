# bonus 1
# text = input("Enter a title: ")
# print("length of the string is : " ,len(text))

# bonus 2.1
# password = "Enter password : "
#
# while password != "abc":
#     password = input(password)
#
# print("Correct")

# coding ex 3
# Create a program that prompts the user to input their name once.
# Then, the program repeatedly prints out the name with the first letter capitalized.

# name = input("Enter your name : ")
# while True:
#     print(name.capitalize())

# coding ex 4
# Create a program that prompts the user to input their name repeatedly.
# Then, the program repeatedly prints out the name with the first letter capitalized.

# while True:
#     name = input("Enter your name : ")
#     print(name.capitalize())

# section 2 bug fix ex 3

# countries = []
#
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
#     print(countries)

# bonus 5
# waiting_list = ["sen","ben","john"]
# waiting_list.sort()
# for index, item in enumerate(waiting_list):
#     print(f"{index + 1}.{item.capitalize()}")

# bonus 6
# contents = ['1. How you doin?','2. we were on a break!','3. my eyes,my eyes...']
# filenames = ['joey.txt','rachel.txt','phoebe.txt']
#
# for content, filename in zip(contents, filenames):
#     file = open(f"files/{filename}",'w')
#     file.write(content)
#     file.close()

# bonus 7
# filenames = ["1.doc","1.report","1.presentation"]
# filenames = [filename.replace('.','-')+'.txt' for filename in filenames]
# print(filenames)

# bonus 8

# date = input("Enter today's date (yyyy-mm-dd): ")
# filename = f"journal/{date}.txt"
# mood = input("How do you rate your mood today from 1 to 10: ")
# content = input("Let your thoughts flow: ")
#
# with open(filename,'w') as file:
#     file.write(mood + 2 * "\n")
#     file.write(content)
#
# print("noted!")

# bonus 9 using if-elif-else
# password = input("Enter a password : ")
# message = "try again"
# dflag = False
# uflag = False
# lflag = False
# lenflag = False
#
# if len(password) >= 8:
#     lenflag = True
#
# for i in password:
#     if i.isdigit():
#         dflag = True
#
#     if i.islower():
#         lflag = True
#
#     if i.isupper():
#         uflag = True
#
# if lenflag and dflag and lflag and uflag:
#     message = "password correct"
# else:
#     message = "incorrect password"
#
# print(message)


# bonus 9 using lists
# password = input("Enter a password : ")
# message = "try again"
# result = []
# len_pass = False
# digit = False
# uppercase = False
# lowercase = False
#
# if len(password) >= 8:
#     len_pass = True
# result.append(len_pass)
#
# for i in password:
#     if i.isdigit():
#         digit = True
# result.append(digit)
#
# for i in password:
#     if i.islower():
#         lowercase = True
# result.append(lowercase)
#
# for i in password:
#     if i.isupper():
#         uppercase = True
# result.append(uppercase)
#
# print(result)
# if all(result):
#     message = "Strong password"
# else:
#     message = "Weak password"
#
# print(message)


# bonus 9 using dictionary
# password = input("Enter a password : ")
# message = "try again"
# result = {}
# len_pass = False
# digit = False
# uppercase = False
# lowercase = False
#
# if len(password) >= 8:
#     len_pass = True
# result['len_pass'] = len_pass
#
# for i in password:
#     if i.isdigit():
#         digit = True
# result['digit'] = digit
#
# for i in password:
#     if i.islower():
#         lowercase = True
# result['lowercase'] = lowercase
#
# for i in password:
#     if i.isupper():
#         uppercase = True
# result['uppercase'] = uppercase
#
# print(result)
# if all(result.values()):
#     message = "Strong password"
# else:
#     message = "Weak password"
#
# print(message)

# bonus 11*****
# def get_avg():
#     with open("files/data.txt", 'r') as file:
#         data = file.readlines()
#
#     data_sliced = data[1:]
#     values = [float(i) for i in data_sliced]
#     avg_local = sum(values) / len(data_sliced)
#     return avg_local
#
#
# average = get_avg()
# print(average)

#bonus 12
# feet_inches = input("Enter feet and inches: ")
#
# def convert(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#
#     meters = feet * 0.3048 + inches * 0.0254
#     # return f"{feet} feet and {inches} inches is {meters} meters"
#     return meters
#
# result = convert(feet_inches)
#
# if result < 1:
#     print("Kid is too small")
# else:
#     print("kid can use the slide")

#bonus 13 decoupling function
# feet_inches = input("Enter feet and inches: ")
#
# def parse(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#     return {"feet":feet,"inches":inches}
#
# def convert(feet, inches):
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
# parsed = parse(feet_inches)
# result = convert(parsed['feet'],parsed['inches'])
# print(f"{parsed['feet']} feet and {parsed['inches']} inches is {result} meters")
#
# if result < 1:
#     print("Kid is too small")
# else:
#     print("kid can use the slide")

#bonus 14

# feet_inches = input("Enter feet and inches: ")
#
# parsed = parse(feet_inches)
# result = convert(parsed['feet'], parsed['inches'])
# print(f"{parsed['feet']} feet and {parsed['inches']} inches is {result} meters")
#
# if result < 1:
#     print("Kid is too small")
# else:
#     print("kid can use the slide")

#bonus 15
#
# import json
#
# with open("questions.json","r") as file:
#     content = file.read()
#
# data = json.loads(content)
#
# score = 0
# for question in data:
#     print(question["question_text"])
#     for index, alternative in enumerate(question["alternatives"]):
#         print(index+1, "-", alternative)
#     user_choice = int(input("Enter your answer: "))
#     question["user_choice"] = user_choice
#
# for index,question in enumerate(data):
#     if question["user_choice"] == question["correct_answer"]:
#         score += 1
#         result = "Correct Answer"
#     else:
#         result = "Wrong Answer"
#
#     message = f"{index+1} {result} - Your answer : {question['user_choice']}, " \
#               f"Correct answer : {question['correct_answer']}"
#
#     print(message)
#
# print("Score : ", score, "/", len(data))
#
# # print(type(data))
# # print(data)

#section 16, bug fix exercise
# from parsers import parse
# import random
#
# # Ask the user to enter a lower and an upper bound divided by a comma
# user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10): ")
#
# # Parse the user string by calling the parse function
# parsed = parse(user_input)
#
# # Pick a random int between the two numbers
# rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])
#
# print(rand)

#section 16, coding exercise
# import random
#
# lower_bound = int(input("Enter the lower bound: "))
# upper_bound = int(input("Enter the upper bound: "))
#
# print(random.randint(lower_bound, upper_bound))

# #bonus 16
# import FreeSimpleGUI as sg
#
# src_label = sg.Text("Select files to compress:")
# src_input = sg.InputText(tooltip="source")
# src_choose_btn = sg.FileBrowse("Choose")
#
# dest_label = sg.Text("Select destination folder:")
# dest_input = sg.InputText(tooltip="destination")
# dest_choose_btn = sg.FolderBrowse("Choose")
#
# compress_btn = sg.Button("Compress")
#
# window = sg.Window('File Zipper',layout = [[src_label,src_input,src_choose_btn],
#     [dest_label,dest_input,dest_choose_btn],
#     [compress_btn]])
#
# window.read()
# window.close()

#section 17, coding exercise
# import FreeSimpleGUI as sg
#
# feet_label = sg.Text("Enter feet:")
# feet_input =  sg.Input()
#
# inch_label = sg.Text("Enter inches:")
# inch_input = sg.Input()
#
# convert_btn = sg.Button("Convert")
#
# window = sg.Window('Convertor', layout = [[feet_label,feet_input],[inch_label,inch_input],[convert_btn]])
# window.read()
# window.close()

#bonus 17
# from zip_creator import make_archive
# import FreeSimpleGUI as sg
#
# src_label = sg.Text("Select files to compress:")
# src_input = sg.InputText(tooltip="source")
# src_choose_btn = sg.FilesBrowse("Choose", key="files")
#
# dest_label = sg.Text("Select destination folder:")
# dest_input = sg.InputText(tooltip="destination")
# dest_choose_btn = sg.FolderBrowse("Choose", key="folder")
#
# compress_btn = sg.Button("Compress")
# message_label = sg.Text(key="message",text_color="white")
#
# window = sg.Window('File Zipper',layout = [[src_label,src_input,src_choose_btn],
#     [dest_label,dest_input,dest_choose_btn],
#     [compress_btn, message_label]])
#
# while True:
#     event, values = window.read()
#     # print(1, event)
#     # print(2, values)
#     filepaths = values["files"].split(";")
#     folder = values["folder"]
#     make_archive(filepaths,folder)
#     window['message'].update(value ="Compress successful!")
#     # print(3,filepaths)
#     # print(4,folder)
#
# window.close()

#section 18, coding exercise 55
# import FreeSimpleGUI as sg
# from converters import convert
#
# feet_label = sg.Text("Enter feet:")
# feet_input =  sg.Input(key="feet")
#
# inch_label = sg.Text("Enter inches:")
# inch_input = sg.Input(key="inches")
#
# convert_btn = sg.Button("Convert")
# message_label = sg.Text(key="message", text_color="white")
#
# window = sg.Window('Convertor', layout = [[feet_label,feet_input],
#                                           [inch_label,inch_input],
#                                           [convert_btn,message_label]])
#
# while True:
#     events, values = window.read()
#     meters = convert(float(values['feet']),float(values['inches']))
#     window["message"].update(value=f"{meters} m")
#     # print(events)
#     # print(values)
#     # print(meters)
#
# window.close()

#bonus 18
#
# import FreeSimpleGUI as sg
# from zip_extractor import extract_archive
#
# archive_label = sg.Text("Select archive",key="archive_label")
# archive_text = sg.Input(key="archive_text")
# file_choose = sg.FileBrowse("Choose",key="file")
#
# dest_label = sg.Text("Select destination",key="dest_label")
# dest_text = sg.Input(key="dest_text")
# folder_choose = sg.FolderBrowse("Choose", key="folder")
#
# extract_button = sg.Button("Extract")
# output_label = sg.Text(key="message",text_color="white")
#
# window = sg.Window('ARCHIVE EXTRACTOR',layout=[[archive_label,archive_text,file_choose],
#                                                [dest_label,dest_text,folder_choose],
#                                                [extract_button,output_label]])
#
# while True:
#     events,values = window.read()
#     print(1, events)
#     print(2, values)
#
#     archive_path = values['file']
#     dest_folder = values['folder']
#     extract_archive(archive_path,dest_folder)
#     window['message'].update(value="Extraction successful!")
#
#     print(3, archive_path)
#     print(4, dest_folder)
#
#
# window.close()

#section 19, coding exercise
# import FreeSimpleGUI as sg
# from converters import convert
#
# sg.theme("Black")
# feet_label = sg.Text("Enter feet:")
# feet_input =  sg.Input(key="feet")
#
# inch_label = sg.Text("Enter inches:")
# inch_input = sg.Input(key="inches")
#
# convert_btn = sg.Button("Convert")
# exit_btn = sg.Button("Exit")
# message_label = sg.Text(key="message", text_color="white")
#
# window = sg.Window('Convertor', layout = [[feet_label,feet_input],
#                                           [inch_label,inch_input],
#                                           [convert_btn,exit_btn,message_label]])
#
# while True:
#     event, values = window.read()
#     match event:
#         case "Exit":
#             break
#         case sg.WIN_CLOSED:
#             break
#
#     meters = convert(float(values['feet']),float(values['inches']))
#     window["message"].update(value=f"{meters} m")
#     # print(event)
#     # print(values)
#     # print(meters)
#
# window.close()

