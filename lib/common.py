# Author: Mr.Xu

# 登陆装饰器
def login_auth(role):
    from core import admin,student,teacher
    def auth(func):
        def inner(*args, **kwargs):
            if role == "admin":
                if admin.user_dic.get("user"):
                    res = func(*args, **kwargs)
                    return res
                admin.login()
            elif role == "student":
                if student.user_dic.get("user"):
                    res = func(*args, **kwargs)
                    return res
                student.login()

            elif role == "teacher":
                if teacher.user_dic.get("user"):
                    res = func(*args, **kwargs)
                    return res
                teacher.login()
        return inner
    return auth
