# Author: Mr.Xu

from conf import settings
from lib import common
from interface import student_interface,common_interface

# 用户信息
user_dic = {
    "user" : None
}

def register():
    print("register...")

    user = input("请输入账户")
    pwd = input("请输入密码")
    pwd_true = input("请确认密码")

    if pwd != pwd_true:
        print("两次密码不一致")
        return

    flag = student_interface.register_interface(user,pwd)
    if flag:
        print("注册成功")


def login():
    print("login...")

    user = input("请输入账户")
    pwd = input("请输入密码")

    flag = student_interface.login_interface(user, pwd)
    if flag:
        user_dic["user"] = user
        print("登陆成功")


@common.login_auth("student")
def choice_school():
    print("choice_school...")

    school_list = common_interface.get_school_list()
    if not school_list:
        print("没有学校")
        return

    for i, school in enumerate(school_list):
        print(f"学校编号:{i} {school}")

    index = input("请输入选择的学校编号")

    if index.isdigit() and int(index) in range(len(school_list)):
        index = int(index)

        school_name = school_list[index]
        flag = student_interface.choice_school_interface(user_dic["user"],school_name)
        if flag:
            print(f"选择学校成功 {school_name}")

    else:
        print("输入错误")


@common.login_auth("student")
def choice_course():
    print("choice_course...")

    course_list = student_interface.get_course_list(user_dic["user"])
    if course_list:
        for i, course in enumerate(course_list):
            print(f"学校编号{i} {course}")

        index = input("请输入选择的学校编号")

        if index.isdigit() and int(index) in range(len(course_list)):
            index = int(index)

            course_name = course_list[index]

            flag = student_interface.choice_course_interface(user_dic["user"], course_name)
            if flag:
                print(f"成功选择课程: {course_name}")
        else:
            print("输入错误")


@common.login_auth("student")
def show_score():
    print("show_score...")

    score = student_interface.show_score_interface(user_dic["user"])
    if score:
        print(score)
    

# 学生视图
def student_view():
    func_dict = {
        "1": register,
        "2": login,
        "3": choice_school,
        "4": choice_course,
        "5": show_score,
    }
    while 1:
        print(settings.STUDENT_MENU)
        index = input("请输入功能列表")
        if index == "q":
            break
        if index in func_dict:
            func_dict[index]()