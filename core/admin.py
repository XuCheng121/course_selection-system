# Author: Mr.Xu

from conf import settings
from lib import common
from interface import admin_interface,common_interface

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

    flag = admin_interface.register_interface(user,pwd)
    if flag:
        print("注册成功")


def login():
    print("login...")

    user = input("请输入账户")
    pwd = input("请输入密码")

    flag = admin_interface.login_interface(user, pwd)
    if flag:
        user_dic["user"] = user
        print("登陆成功")


@common.login_auth("admin")
def create_school():
    print("create_school...")

    schoool_name = input("请输入学校名")

    flag = admin_interface.create_school_interface(user_dic["user"],schoool_name)
    if flag:
        print(f"创建学校成功{schoool_name}")


@common.login_auth("admin")
def create_teacher():
    print("create_teacher...")

    name = input("请输入老师名")

    flag = admin_interface.create_teacher_interface(user_dic["user"], name)
    if flag:
        print(f"创建老师成功{name}")


@common.login_auth("admin")
def create_course():
    print("create_course...")

    school_list = common_interface.get_school_list()
    if not school_list:
        print("没有学校")
        return

    for i,school in enumerate(school_list):
        print(f"学校编号:{i} {school}")

    index = input("请输入选择的学校编号")

    if index.isdigit() and int(index) in range(len(school_list)):
        index = int(index)

        school_name = school_list[index]
        course_name = input("请输入课程名称")

        flag = admin_interface.create_course_interface(user_dic["user"], school_name, course_name)
        if flag:
            print(f"成功创建了课程: {course_name}, 学校: {school_list}")


# 管理员视图
def admin_view():
    func_dict = {
        "1": register,
        "2": login,
        "3": create_school,
        "4": create_teacher,
        "5": create_course,
    }
    while 1:
        print(settings.ADMIN_MENU)
        index = input("请输入功能列表")
        if index == "q":
            break
        if index in func_dict:
            func_dict[index]()