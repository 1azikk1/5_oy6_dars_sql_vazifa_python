from database import db
from collections import namedtuple


def run():
    while True:
        break


if __name__ == '__main__':
    # TABLE LARNI YARATIB OLAMIZ

    db.create_table_students()
    db.create_table_courses()
    db.create_table_enrollments()
    db.create_table_teachers()
    db.create_table_course_assignments()

    # TABLE GA MA'LUMOTLARNI QO'SHAMIZ

    # STUDENTS
    # db.insert_students(18, 'toxir@gmail.com')
    # db.insert_students(19, 'sobir@gmail.com')
    # db.insert_students(20, 'jalil@gmail.com')
    # db.insert_students(21, 'bakir@gmail.com')
    # db.insert_students(22, 'ali@gmail.com')
    # db.insert_students(23, 'vali@gmail.com')
    # db.insert_students(24, 'jasur@gmail.com')

    # COURSES
    # db.insert_courses('Python', 1)
    # db.insert_courses('JavaScript', 3)
    # db.insert_courses('C++', 5)

    # ENROLLMENTS
    # db.insert_enrollments(1, 1)
    # db.insert_enrollments(5, 3)
    # db.insert_enrollments(7, 2)

    # TEACHERS
    # db.insert_teachers(4)
    # db.insert_teachers(12)

    # COURSE ASSIGNMENTS
    # db.insert_course_assignments(1, 1)
    # db.insert_course_assignments(2, 3)

    # STUDENT JADVALI NOMINI O'ZGARTIRAMIZ

    # db.change_table_students('students', 'talabalar')
    # db.change_column_talabalar('talabalar', 'age', 'talabaning_yoshi')

    # TALABALAR JADVALIDAGI 2 TA TALABANING YOSHINI O'ZGARTIRAMIZ
    # db.update_students_info('talabalar', 'talabaning_yoshi', 30, 1)
    # db.update_students_info('talabalar', 'talabaning_yoshi', 35, 7)

    # # 2 TA TALABANI O'CHIRIB TASHLAYMIZ
    # db.delete_students('talabalar', 2)
    # db.delete_students('talabalar', 1)

    # JADVALLARNI KO'RAMIZ

    # FAQAT TALABALAR JADVALINI CHIQARISH UCHUN

    # Student = namedtuple("talabalar", ['id', 'age', 'email'])
    #
    # for student in db.select_all_data('talabalar'):
    #     talaba = Student(*student)
    #     print(talaba.id, talaba.age, talaba.email)

    # QOLGAN JADVALLARNI CHIQARISH UCHUN
    # for data in db.select_all_data('enrollments'):
    #     print(data)
    run()

