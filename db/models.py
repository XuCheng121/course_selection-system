# Author: Mr.Xu

from . import db_handler

# 基类
class Base:
    @classmethod
    def read_info(cls, name):
        return db_handler.read_info(cls,name)

    def save_info(self):
        return db_handler.save_info(self)


# 管理员类
class Admin(Base):

    def register(self,name,pwd):
        self.name = name
        self.pwd = pwd
        self.save_info()

    def create_school(self,name):
        school = School(name)
        school.save_info()

    def create_teacher(self,name,pwd):
        obj = Tercher(name,pwd)
        obj.save_info()

    def create_course(self,school_name, course_name):
        # 先保存课程
        course = Course(course_name)
        course.save_info()

        # 给学校添加课程
        obj = School.read_info(school_name)
        obj.add_course(course_name)


# 学校类
class School(Base):

    def __init__(self, name):
        self.name = name
        self.school_course_list = []

    def add_course(self, course):
        self.school_course_list.append(course)
        self.save_info()


# 教师类
class Tercher(Base):

    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
        self.teacher_course_list = []

    def add_course(self, course):
        self.teacher_course_list.append(course)
        self.save_info()

    def show_course_student(self,course):
        obj = Course.read_info(course)
        return obj.student_list


    def change_score(self,course_name,student_name,score):
        obj = Student.read_info(student_name)
        obj.score[course_name] = score
        obj.save_info()
        return True


# 课程类
class Course(Base):

    def __init__(self,name):
        self.name = name
        self.student_list = []

    def add_student(self,stu_name):
        # 学生选课
        self.student_list.append(stu_name)
        self.save_info()


# 学生类
class Student(Base):

    def register(self,name,pwd):
        self.name = name
        self.pwd = pwd
        self.school = None
        self.course_list = []
        self.score = {}
        self.save_info()

    def choice_school(self,school):
        self.school = school
        self.save_info()

    def show_school_course(self,school_name):
        school = School.read_info(school_name)
        return school.school_course_list


    def add_course(self,course):
        # 学生选课
        self.course_list.append(course)
        self.score[course] = 0
        self.save_info()

        # 课程包含学生
        obj = Course.read_info(course)
        obj.add_student(self.name)




