# Author: Mr.Xu

# 学生操作接口

from db import models


def register_interface(name,pwd):
    obj = models.Student.read_info(name)
    if not obj:
        student = models.Student()
        student.register(name,pwd)
        return True

    else:
        print("用户已经存在")
        return False


def login_interface(name,pwd):
    obj = models.Student.read_info(name)
    if obj:
        if obj.name == name and obj.pwd == pwd:
            return True
        else:
            print("密码不正确")
            return False

    else:
        print("用户不存在")
        return False

def choice_school_interface(student_name, school_name):
    obj = models.Student.read_info(student_name)
    if obj.school:
        print("学生已经选择学校")
        return False

    else:
        obj.choice_school(school_name)
        return True

def get_course_list(student_name):
    obj = models.Student.read_info(student_name)
    if obj.school:
        course_list = obj.show_school_course(obj.school)
        if course_list:
            return course_list
        else:
            print("没有课程")
            return False

    else:
        print("没有选择学校")
        return False

def choice_course_interface(student_name, course_name):
    obj = models.Student.read_info(student_name)
    if course_name in obj.course_list:
        print("该课程已经选择过了")
        return False

    else:
        obj.add_course(course_name)
        return True

def show_score_interface(student_name):
    obj = models.Student.read_info(student_name)
    if obj.score:
        return obj.score

    else:
        print("还没有选课")
        return False