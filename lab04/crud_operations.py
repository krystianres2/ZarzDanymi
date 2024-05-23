from basicmodel import app, db, Student

app.app_context().push()

# all_students = Student.query.all()

# print(f'All students:\n{all_students}')

# new_student = Student('Łukasz', 3)
# db.session.add(new_student)
# db.session.commit()

# all_students = Student.query.all()
# print(f'All students:\n{all_students}')

# all_students = Student.query.all()
# print(f'All students:\n{all_students}')

student_first = db.session.get(Student, 1)

print(f'Student 1; print "only" Name:\n{student_first.name}')

print(f'Student 1; print ALL data:\n{student_first}')
all_students = Student.query.all()
print(f'All students:\n{all_students}')

student_lukasz = Student.query.filter_by(name='Łukasz')

print(f'Student (Lukasz):\n{student_lukasz.all()}')

# Update

first_student = db.session.get(Student,1)
first_student.name = 'Natalia'
first_student.semester = 7
db.session.add(first_student)
db.session.commit()

all_students = Student.query.all()
print(f'All students:\n{all_students}')

# Delete

second_student = db.session.get(Student,2)
db.session.delete(second_student)
db.session.commit()

all_students = Student.query.all()
print(f'All students:\n{all_students}')