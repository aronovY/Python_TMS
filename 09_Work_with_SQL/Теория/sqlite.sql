SELECT id, name from students;
SELECT * from students;
SELECT DISTINCT name from students;
SELECT * from students WHERE age <= 30 AND is_alive;
SELECT * from students WHERE age <= 30 AND is_alive IS NULL;
SELECT * from students WHERE age <= 30 AND is_alive IS NOT NULL;
SELECT * from students WHERE age = 21;
SELECT * from students WHERE age <> 21;
SELECT * from students ORDER BY age;
SELECT * from students ORDER BY age DESC;
SELECT * from students ORDER BY name, age;

INSERT INTO students (name, age)
VALUES ('John', 40);

INSERT INTO students (name, age, is_alive)
VALUES ('Ann', 23, true),
       ('Crownvirus', 15, true);

UPDATE students
SET is_alive = false
WHERE is_alive AND age >= 21;

UPDATE students
SET age = age + 1
WHERE is_alive;

DELETE FROM students WHERE is_alive IS NULL;

UPDATE students SET is_alive = NOT is_alive;

SELECT name FROM students
WHERE name LIKE '%a%';

SELECT * FROM students ORDER BY id LIMIT 2;
SELECT * FROM students ORDER BY id LIMIT 2 OFFSET 1;

INSERT INTO groups (number)
VALUES (101), (102);

SELECT s.id AS student_id,
       name AS student_name,
       number AS group_number
FROM students s
JOIN groups g ON s.group_id = g.id;

SELECT students.id as s_id,
       name,
       groups.id as g_id,
       number
FROM students
LEFT JOIN groups ON students.group_id = groups.id;

-- SELECT students.id as s_id,
--        name,
--        groups.id as g_id,
--        number
-- FROM students
-- RIGHT JOIN groups ON students.group_id = groups.id;

-- SELECT students.id as s_id,
--        name,
--        groups.id as g_id,
--        number
-- FROM students
-- FULL JOIN groups ON students.group_id = groups.id;

SELECT students.id as s_id,
       name,
       groups.id as g_id,
       number
FROM students
CROSS JOIN groups;