# Author: Mr.Xu

# 进入视图接口

from conf import settings
from . import admin,student,teacher

func_dict = {
    "1": admin.admin_view,
    "2": teacher.tercher_view,
    "3": student.student_view,
}

def run():
    while 1:
        print(settings.VIEW_MSG)
        index = input("请输入功能列表")
        if index == "q":
            break
        if index in func_dict:
            func_dict[index]()

