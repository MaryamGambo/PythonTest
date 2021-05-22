import sqlite3
import queries

try:
    with sqlite3.connect("students.sqlite3") as conn:
        cur = conn.cursor()

        # to create a table
        cur.execute(queries.CREATE_TABLE)


    class Connectivity:
        def start(self):
            while True:
                self.options()

                prompt = input("Do you want to continue [Y/N] ?").lower()
                quit(0) if prompt == 'n' else ''

        def options(self):
            print('1) Display all students')
            print('2) Insert student record')
            print('3) Update student record')
            print('4) Delete student record')

            option = int(input('Select an option [1/2/3/4] =>'))
            if option == 1:
                self.display_record()
            elif option == 2:
                self.insert_record()
            elif option == 3:
                self.update_record()
            elif option == 4:
                self.delete_record()
            else:
                print('Invalid option')
            return

        def display_record(self):
            # selecting all records from table
            students = cur.execute(queries.FETCH_ALL)  # fetch all records from db
            for i in students:
                print(i)

            return

        def insert_record(self):
            # inserting records into table
            first_name = input('Enter your first name:')
            last_name = input('Enter your last name:')
            age = int(input('Enter your age:'))
            gender = input('Enter your gender:')
            email = input('Enter your email address:').lower()
            cur.execute(queries.INSERT, (first_name, last_name, age, gender, email))

            conn.commit()

            print('Student record successfully added')
            return

        def delete_record(self):
            # deleting a record from table
            student_id = input('Enter your student id:')
            cur.execute(queries.DELETE, student_id)
            conn.commit()

            print('Student record deleted successfully')
            return

        def update_record(self):
            # updating a record in the table
            student_id = int(input('Enter your student id:'))
            first_name = input('Enter first name:')
            last_name = input('Enter last name:')
            age = input('Enter age:')
            gender = input('Enter gender:')
            email = input('Enter email address:')

            cur.execute(queries.UPDATE, (first_name, last_name, age, gender, email, student_id))

            conn.commit()

            print('Student record updated successfully')
            return


except sqlite3.Connection as e:
    print('Error while connecting to sqlite database')




