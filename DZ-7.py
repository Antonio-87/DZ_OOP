class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if  (isinstance(lecturer,Lecturer) and course in lecturer.courses_attached 
            and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_rating(self):
        length = [len(value) for value in self.grades.values()]
        rating = round(sum(sum(self.grades.values(), [])) / sum(length), 1)
        return rating

    def __str__(self):
        res = (f'Имя: {self.name} \nФамилия: {self.surname}'
               f'\nСредняя оценка за лекции: '
               f'{self.__average_rating()}'
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.__average_rating() < other.__average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __average_rating(self):
        length = [len(value) for value in self.grades.values()]
        rating = round(sum(sum(self.grades.values(), [])) / sum(length), 1)
        return rating

    def __str__(self):
        res = (f'Имя: {self.name} \nФамилия: {self.surname}'
               f'\nСредняя оценка за лекции: '
               f'{self.__average_rating()}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Student!')
            return
        return self.__average_rating() < other.__average_rating()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


student_1 = Student('Ruoy', 'Eman', 'man')
student_1.courses_in_progress += ['Python', 'Git']
student_1.add_courses('Введение в программирование')
student_2 = Student('Jon', 'Evance', 'man')
student_2.courses_in_progress += ['Python', 'Git']
student_2.add_courses('Введение в программирование')

lecturer_1 = Lecturer('Advard', 'Ganuy')
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2 = Lecturer('Sara', 'Rubense')
lecturer_2.courses_attached += ['Python', 'Git']

student_1.rate_hw(lecturer_1, 'Python', 10)
student_2.rate_hw(lecturer_1, 'Git', 7)
student_1.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'Git', 10)

reviewer_1 = Reviewer('Emma', 'Rivany')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Luisa', 'Bone')
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Git', 10)

print(student_1)
print(student_2)

print(student_1 < student_2)

print(lecturer_1)
print(lecturer_2)

print(lecturer_1 < lecturer_2)

students_list = [student_1, student_2]
def average_grade_course(students_list, course):
    course_grades = 0
    i = 0
    for student in students_list:
        for key, value in student.grades.items():
            if key == course:
                course_grades += sum(value)
                i += 1
            else:
                i += 0     
    if course_grades == 0:
        return course_grades
    return round(course_grades/i, 1)


lecturers_list = [lecturer_1, lecturer_2]
def average_grade_course(lecturers_list, course):
    course_grades = 0
    i = 0
    for lecturer in lecturers_list:
        for key, value in lecturer.grades.items():
            if key == course:
                course_grades += sum(value)
                i += 1
            else:
                i += 0        
    if course_grades == 0:
        return course_grades
    return round(course_grades/i, 1)

print(average_grade_course(students_list, 'Python'))
print(average_grade_course(lecturers_list, 'Git'))

