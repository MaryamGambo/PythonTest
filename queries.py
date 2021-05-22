CREATE_TABLE = "CREATE TABLE IF NOT EXISTS students_details(" \
               "'id' INTEGER," \
               "'firstName' TEXT(10) NOT NULL," \
               "'lastName' TEXT(10) NOT NULL," \
               "'age' INTEGER(2) NOT NULL," \
               "'gender' TEXT(6) NOT NULL," \
               "'email' TEXT(50) NOT NULL UNIQUE," \
               "PRIMARY KEY('id' AUTOINCREMENT)" \
               ")"

INSERT = "INSERT INTO students_details(id, firstName, lastName, age, gender, email) VALUES(NULL,?, ?, ?, ?, ?)"

FETCH_ALL = "SELECT * FROM students_details"

UPDATE = "UPDATE students_details SET firstName= ?,lastName= ?,age=?, gender=?, email=?  where id = ?"

DELETE = "DELETE FROM students_details where id = ?"