# Author: Mr.Xu

# 管理员操作接口

from db import models


def register_interface(name,pwd):
    obj = models.Admin.read_info(name)
    if not obj:
        admin = models.Admin()
        admin.register(name,pwd)
        return True

    else:
        print("用户已经存在")
        return False


def login_interface(name,pwd):
    obj = models.Admin.read_info(name)
    if obj:
        if obj.name == name and obj.pwd == pwd:
            return True
        else:
            print("密码不正确")
            return False

    else:
        print("用户不存在")
        return False

def create_school_interface(admin_name,name):

    obj = models.School.read_info(name)
    if not obj:
        obj = models.Admin.read_info(admin_name)
        obj.create_school(name)
        return True

    else:
        print("学校已经存在")
        return False

def create_teacher_interface(admin_name,name,pwd="123"):

    obj = models.Tercher.read_info(name)
    if not obj:
        obj = models.Admin.read_info(admin_name)
        obj.create_teacher(name,pwd)
        return True

    else:
        print("该老师已存在")
        return False

def create_course_interface(admin_name,school_name,course_name):
    obj = models.School.read_info(school_name)

    if not obj:
        return False

    if course_name in obj.school_course_list:
        print("该学校课程已存在")
        return False

    else:
        obj = models.Admin.read_info(admin_name)
        obj.create_course(school_name,course_name)
        return True






