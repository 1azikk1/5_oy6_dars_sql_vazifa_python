import psycopg2


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='courses',
            user='postgres',
            host='localhost',
            password='1'
        )

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result

    def create_table_students(self):
        sql = '''CREATE TABLE IF NOT EXISTS students(
            student_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            age INTEGER CHECK(age > 0),
            email VARCHAR(50) UNIQUE NOT NULL
        );
        '''
        self.manager(sql, commit=True)

    def create_table_courses(self):
        sql = '''CREATE TABLE IF NOT EXISTS courses(
            course_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            course_code VARCHAR(50) UNIQUE NOT NULL,
            credits INTEGER CHECK(credits >= 1 and credits <=5)       
        );'''
        self.manager(sql, commit=True)

    def create_table_enrollments(self):
        sql = '''CREATE TABLE IF NOT EXISTS enrollments(
            enrollment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            student_id INTEGER REFERENCES students(student_id) ON DELETE SET NULL,
            course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE
        );'''
        self.manager(sql, commit=True)

    def create_table_teachers(self):
        sql = '''CREATE TABLE IF NOT EXISTS teachers(
            teacher_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            experience_years INTEGER CHECK(experience_years >=0)            
        );'''
        self.manager(sql, commit=True)

    def create_table_course_assignments(self):
        sql = '''CREATE TABLE IF NOT EXISTS course_assignments(
            assignment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            teacher_id INTEGER DEFAULT 2 REFERENCES teachers(teacher_id) ON DELETE SET DEFAULT,
            course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE
        );'''
        self.manager(sql, commit=True)

    def insert_students(self, age, email):
        sql = '''INSERT INTO students(age, email) VALUES
        (%s, %s) ON CONFLICT DO NOTHING
        '''
        self.manager(sql,  age, email, commit=True)

    def insert_courses(self, course_code, credits):
        sql = '''INSERT INTO courses(course_code, credits) VALUES (%s, %s) ON CONFLICT DO NOTHING'''
        self.manager(sql, course_code, credits, commit=True)

    def insert_enrollments(self, student_id, course_id):
        sql = '''INSERT INTO enrollments(student_id, course_id) VALUES (%s, %s)
            ON CONFLICT DO NOTHING
        '''
        self.manager(sql, student_id, course_id, commit=True)

    def insert_teachers(self, experience_years):
        sql = '''INSERT INTO teachers(experience_years) VALUES (%s) ON CONFLICT DO NOTHING'''
        self.manager(sql, experience_years, commit=True)

    def insert_course_assignments(self, teacher_id, course_id):
        sql = '''INSERT INTO course_assignments(teacher_id, course_id) VALUES (%s, %s)
            ON CONFLICT DO NOTHING
        '''
        self.manager(sql, teacher_id, course_id, commit=True)

    def change_table_students(self, table_name, new_table_name):
        sql = f'''ALTER TABLE {table_name} RENAME TO {new_table_name}'''
        self.manager(sql, commit=True)

    def change_column_talabalar(self, table_name, column_name, new_column_name):
        sql = f'''ALTER TABLE {table_name} RENAME COLUMN {column_name} TO {new_column_name}'''
        self.manager(sql, commit=True)

    def update_students_info(self, table_name, column_name, new_age, student_id):
        sql = f'''UPDATE {table_name} SET {column_name} = %s WHERE student_id = %s'''
        self.manager(sql, new_age, student_id, commit=True)

    def delete_students(self, table_name, student_id):
        sql = F'''DELETE FROM {table_name} WHERE student_id = %s'''
        self.manager(sql, student_id, commit=True)

    def select_all_data(self, table_name):
        sql = f'''SELECT * FROM {table_name}'''
        return self.manager(sql, table_name, fetchall=True)


db = DataBase()
