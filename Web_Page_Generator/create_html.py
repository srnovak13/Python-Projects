import webbrowser

f= open("summer_sale.html","w")

message= """<html>
<body>
<h1>Stay tuned for our amazing summer sale!</h1>
</body>
</html>"""

f.write(message)
f.close()

filename='C:\\Users\\srnov\\Git Depositories\\Python Projects\\Python-Projects\\summer_sale.html'

webbrowser.open_new_tab(filename)

