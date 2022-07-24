import psycopg2

data = {
	'id': 3,
	'completed': False
}

data2 = {
	'id': 4,
	'completed': True
}

sql = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

connection = psycopg2.connect('dbname=test')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
	CREATE TABLE table2(
		id INTEGER PRIMARY KEY,
		completed BOOLEAN NOT NULL DEFAULT False
	);
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);', {
	'id': 2,
	'completed': False
})

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);', data)

cursor.execute(sql, data2)

cursor.execute('SELECT * from table2')

result = cursor.fetchall()
print('fetchall', result)

result2 = cursor.fetchone()
print('fetchone', result2)

connection.commit()

connection.close()
cursor.close()
