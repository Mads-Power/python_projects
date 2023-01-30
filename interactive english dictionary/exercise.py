import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "",
    host = "",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("enter word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'line'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(results[1])
else:
    print("no word found")