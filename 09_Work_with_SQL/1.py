import psycopg2


def task_2(cursor):
    cursor.execute('''
            CREATE TABLE shops
            (
                "id" SERIAL NOT NULL,
                "name" VARCHAR(30) NOT NULL ,
                "address" VARCHAR(100) DEFAULT NULL,
                "staff_amount" INTEGER NOT NULL,
                PRIMARY KEY(id)
            );
            CREATE TABLE departments
            (
                "id" SERIAL PRIMARY KEY,
                "sphere" VARCHAR(30) NOT NULL,
                "staff_amount" INTEGER NOT NULL ,
                "shop" INTEGER REFERENCES Shops(id)
            );
            CREATE TABLE items
            (
                "id" SERIAL PRIMARY KEY,
                "name" VARCHAR(30) NOT NULL,
                "descriptions" TEXT DEFAULT NULL,
                "price" INTEGER,
                "department" INTEGER REFERENCES Departments(id)
            )
''')


def task_3(cursor):
    cursor.execute('''
    INSERT INTO shops (name, address, "staff amount")
    VALUES ('Auchan', null, 250), ('IKEA', 'Vilnius, Lithuania.', 500);
    INSERT INTO departments (sphere, staff_amount, shop)
    VALUES ('Furniture', 250, 1), ('Furniture', 300, 2), ('Dishes', 200, 1);
    INSERT INTO items (name, descriptions, price, department)
    VALUES ('Table', 'Cheap wooden table', 300, 1), ('Table', null, 750, 2),
        ('Bed', 'Amazing wooden bed', 1200, 2), ('Cup', null, 10, 3),
        ('Plate', 'Glass plate', 20, 3)
''')


def task_4(cursor):
    cursor.execute('''
                    SELECT *
                    FROM items
                    WHERE descriptions IS NOT NULL
                    ''')
    lst1 = [row for row in cursor]

    cursor.execute('''
                    SELECT DISTINCT sphere
                    FROM departments
                    WHERE departments.staff_amount > 200
                    ''')
    lst2 = [row for row in cursor]

    cursor.execute('''
                    SELECT address
                    FROM shops
                    WHERE shops.name ILIKE 'i%';
                    ''')
    lst3 = [row for row in cursor]

    cursor.execute('''
                    SELECT DISTINCT name
                    FROM items
                    JOIN departments d on items.department = d.id
                    WHERE d.sphere = 'Furniture';
                    ''')
    lst4 = [row for row in cursor]

    cursor.execute('''
                    SELECT name
                    FROM items
                    WHERE descriptions IS NOT NULL;
                    ''')
    lst5 = [row for row in cursor]

    cursor.execute('''
                    SELECT *
                    FROM items
                    ORDER BY name LIMIT 2 OFFSET 2;
                    ''')
    lst6 = [row for row in cursor]

    cursor.execute('''
                    SELECT name, sphere
                    FROM items
                    JOIN departments d on items.department = d.id;
                    ''')
    lst7 = [row for row in cursor]

    print(f'1: {lst1}\n'
          f'2: {lst2}\n'
          f'3: {lst3}\n'
          f'4: {lst4}\n'
          f'5: {lst5}\n'
          f'6: {lst6}\n'
          f'7: {lst7}')


with psycopg2.connect(dbname='my_db_psql', user='user', password='', host='localhost') as conn:
    with conn.cursor() as cur:
        # task_2(cur)
        # task_3(cur)
        task_4(cur)
