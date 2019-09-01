from db import models

def register_interface(username, password):

    # 1.判断用户是否存在
    # 不合理: 不要使用
    # obj = models.Admin(username, password)
    # obj.select(username)

    # 合理: 推荐使用
    admin_obj = models.Admin.select(username)
    if admin_obj:
        return False, '用户已存在!'

    # 若存在则返回给用户, 用户已存在

    # 若不存在去保存用户数据
    # 方式一:
    # admin_obj = models.Admin(username, password)
    # admin_obj.save()

    # 方式二:
    # 保存用户数据
    models.Admin(username, password)
    return True, f'{username}---注册成功'

# def login_interface(username, password):
#     admin_obj = models.Admin.select(username)
#     if admin_obj:
#         if admin_obj.pwd == password:
#             return True, f'{username}---登录成功'
#
#         else:
#             return False, '密码错误'
#     else:
#         return False, '用户不存在!'

# 创建学校接口
def create_school_interface(admin_name, school_name, school_addr):
    # 1.判断学校是否存在
    school_obj = models.School.select(school_name)
    if school_obj:
        return False, '学校已存在!'

    # 2.若学校不存在则保存学校
    # 获取管理员对象,让管理员来创建学校
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(
        school_name, school_addr)

    return True, f'{school_name}--学校创建成功!'

# 创建老师接口
def create_teacher_interface(admin_name, teacher_name, teacher_pwd='123'):

    teacher_obj = models.Teacher.select(teacher_name)
    if teacher_obj:
        return False, '老师已存在!'

    # 通过管理员对象, 创建老师
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)

    return True, f'{teacher_name}---创建成功!'

# 创建课程接口
def create_course_interface(admin_name, school_name, course_name):
    # 1.获取学校对象中的课程列表, 判断当前课程是否存在列表中
    school_obj = models.School.select(school_name)

    if course_name in school_obj.school_course_list:
        return False, '该学校已存在此课程!'

    # 2.由管理员创建课程
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(school_name, course_name)

    return True, f'{course_name}---课程创建成功!'

