# Author: Mr.Xu

from conf import settings
from lib import common
from interface import teacher_interface,common_interface

# 用户信息
user_dic = {
    "user" : None
}

def login():
    print("login...")

    user = input("请输入账户")
    pwd = input("请输入密码")

    flag = teacher_interface.login_interface(user, pwd)
    if flag:
        user_dic["user"] = user
        print("登陆成功")


@common.login_auth("teacher")
def show_course():
    print("login...")

    course_list = teacher_interface.show_course_interface(user_dic["user"])
    if course_list:
        print(f"教授课程 {course_list}")


@common.login_auth("teacher")
def choice_course():
    print("choice_course...")

    course_list = common_interface.get_course_list()
    if not course_list:
        print("没有课程")

    for i, course in enumerate(course_list):
        print(f"课程编号:{i} {course}")

    index = input("请输入选择的课程编号")

    if index.isdigit() and int(index) in range(len(course_list)):
        index = int(index)

        course_name = course_list[index]
        flag = teacher_interface.choice_course_interface(user_dic["user"], course_name)
        if flag:
            print(f"选择课程成功 {course_name}")
        else:
            print("输入错误")


@common.login_auth("teacher")
def show_course_student():
    print("show_course_student...")

    course_list = teacher_interface.show_course_interface(user_dic["user"])
    if not course_list:
        print("没有课程")

    for i, course in enumerate(course_list):
        print(f"课程编号:{i} {course}")

    index = input("请输入选择的课程编号")

    if index.isdigit() and int(index) in range(len(course_list)):
        index = int(index)

        course_name = course_list[index]
        student_list = teacher_interface.show_course_student_interface(user_dic["user"], course_name)
        if student_list:
            print(f"当前课程下的学生： {student_list}")


@common.login_auth("teacher")
def change_score():
    print("change_score...")

    course_list = teacher_interface.show_course_interface(user_dic["user"])
    if not course_list:
        print("没有课程")

    for i, course in enumerate(course_list):
        print(f"课程编号:{i} {course}")

    index = input("请输入选择的课程编号")

    if index.isdigit() and int(index) in range(len(course_list)):
        index = int(index)

        course_name = course_list[index]
        student_list = teacher_interface.show_course_student_interface(user_dic["user"], course_name)
        if student_list:
            for i, student in enumerate(student_list):
                print(f"课程编号:{i} {student}")

            index = input("请输入选择的学生编号")
            score = input("请输入修改的分数")

            if index.isdigit() and int(index) in range(len(student_list)):
                index = int(index)

                student_name = student_list[index]
                flag = teacher_interface.change_score_interface(user_dic["user"],course_name, student_name,score)
                if flag:
                    print("修改成功")

# 教师视图
def tercher_view():
    func_dict = {
        "1": login,
        "2": show_course,
        "3": choice_course,
        "4": show_course_student,
        "5": change_score,
    }
    while 1:
        print(settings.TEATHER_MENU)
        index = input("请输入功能列表")
        if index == "q":
            break
        if index in func_dict:
            func_dict[index]()