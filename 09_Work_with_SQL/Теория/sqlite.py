import sqlite3

connection = sqlite3.connect('/Users/antonlazouski/Library/Application Support/JetBrains/Toolbox/apps/PyCharm-P/ch-0/193.5233.109/PyCharm.app/Contents/bin/identifier.sqlite')
cursor = connection.cursor()

result = cursor.execute("""
SELECT * FROM students;
""")

print()
