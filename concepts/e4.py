import webbrowser
#open web browser and search for a term on the browser

term = input("enter a search term: ")
webbrowser.open("https://google.com/search?q="+term)