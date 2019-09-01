# Author: Mr.Xu

# 教师操作接口

from db import models

def login_interface(name,pwd):
    obj = models.Tercher.read_info(name)
    if obj:
        if obj.name == name and obj.pwd == pwd:
            return True
        else:
            print("密码不正确")
            return False

    else:
        print("用户不存在")
        return False

def show_course_interface(name):
    obj = models.Tercher.read_info(name)
    if obj.teacher_course_list:
        return obj.teacher_course_list
    else:
        print("没有选择课程")
        return False


def choice_course_interface(name, course_name):
    obj = models.Tercher.read_info(name)
    if course_name in obj.teacher_course_list:
        print("已经选择过该课程")
        return False

    else:
        obj.add_course(course_name)
        return True


def show_course_student_interface(name,course_name):
    obj = models.Tercher.read_info(name)

    student_list = obj.show_course_student(course_name)
    if student_list:
        return student_list

    else:
        print("该课程没有学生")
        return True


def change_score_interface(name, course_name, student_name, score):
    obj = models.Tercher.read_info(name)

    obj.change_score(course_name,student_name,score)

    return True