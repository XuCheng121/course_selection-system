from db import db_handler

class Base:
    # 对象的保存数据方法
    def save(self):
        db_handler.db_save(self)

    # 对象的查询方法
    @classmethod
    def select(cls, username):
        obj = db_handler.db_select(cls, username)
        return obj

# 管理员类
class Admin(Base):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.save()

    # 管理员创建学校方法
    def create_school(self, school_name, school_addr):
        # 实例化学校类,创建学校
        School(school_name, school_addr)

    # 管理员创建老师方法
    def create_teacher(self, teacher_name, teacher_pwd):
        # 实例化Teacher保存老师对象
        Teacher(teacher_name, teacher_pwd)

    # 管理员创建课程方法
    def create_course(self, school_name, course_name):
        # 1.给学校添加课程
        # 获取学校对象的课程列表
        school_obj = School.select(school_name)

        # 实例化课程类创建课程
        Course(course_name)

        # 把课程绑定给学校
        school_obj.add_course(course_name)


# 学生类
class Student(Base):
    def __init__(self, student_name, student_pwd):
        self.name = student_name
        self.pwd = student_pwd
        self.school = None
        self.student_course_list = []
        # 学生的所有分数
        self.score = {}  # score[course_name] = score
        self.save()

    # 学生选择学校
    def choose_school(self, school_name):
        self.school = school_name
        self.save()

    # 学生选择课程
    def choose_course(self, course_name):
        self.student_course_list.append(course_name)
        # 1.学生选择课程并初始化该课程分数
        self.score[course_name] = 0
        self.save()

        # 2.让课程也选择学生
        course_obj = Course.select(course_name)
        course_obj.add_student(self.name)

    # 学生查看成绩
    def check_score(self):
        return self.score


# 课程类
class Course(Base):
    def __init__(self, course_name):
        self.name = course_name
        self.student_list = []
        self.save()

    def add_student(self, student_name):
        self.student_list.append(student_name)
        self.save()


# 老师类
class Teacher(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.name = teacher_name
        self.pwd = teacher_pwd
        # 一个老师可以有多个课程
        self.teacher_course_list = []
        self.save()

    # 老师查看教授课程方法
    def check_course(self):
        return self.teacher_course_list

    # 老师选择教授课程方法
    def choose_course(self, course_name):
        self.teacher_course_list.append(course_name)
        self.save()

    # 老师查看课程下学生方法
    def check_student(self, course_name):
        # 1.获取课程对象
        course_obj = Course.select(course_name)
        return course_obj.student_list

    # 老师修改成绩方法
    def change_score(self, course_name, student_name, score):
        student_obj = Student.select(student_name)
        student_obj.score[course_name] = score
        student_obj.save()


# 学校类
class School(Base):
    def __init__(self, school_name, school_addr):
        self.name = school_name
        self.addr = school_addr
        # 一所学校可以有多个课程
        self.school_course_list = []
        self.save()

    def add_course(self, course_name):
        self.school_course_list.append(course_name)
        self.save()


