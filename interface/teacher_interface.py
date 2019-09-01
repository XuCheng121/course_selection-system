from db import models


# def login_interface(username, password):
#
#     # 1.判断用户名是否存在
#     teacher_obj = models.Teacher.select(username)
#     if teacher_obj:
#
#         if teacher_obj.pwd == password:
#
#             return True, '登录成功!'
#
#         else:
#             return False, '密码错误'
#
#     else:
#         return  False, '用户不存在!'


# 老师查看教授课程接口
def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)

    # 老师去获取教授课程数据
    course_list = teacher_obj.check_course()
    if course_list:
        return True, course_list

    return False, '没有课程'


# 老师选择教授课程接口
def choose_course_interface(teacher_name, course_name):
    # 1.判断课程是否在老师教授课程列表中
    teacher_obj = models.Teacher.select(teacher_name)

    # 若存在,则返回课程已存在
    if course_name in teacher_obj.teacher_course_list:
        return False, '课程已存在'

    # 若不存在,则添加
    teacher_obj.choose_course(course_name)
    return True, f'{course_name}---课程添加成功!'


# 老师查看课程下学生接口
def check_student_interface(teacher_name, course_name):

    # 1.获取老师对象
    teacher_obj = models.Teacher.select(teacher_name)

    # 2.让老师对象,去查看课程下学生
    student_list = teacher_obj.check_student(course_name)
    if student_list:
        return True, student_list

    return False, '课程下没有学生'


# 老师修改学生成绩
def change_score_interface(teacher_name, course_name, student_name, score):

    # 1.获取老师对象
    teacher_obj = models.Teacher.select(teacher_name)

    # 2.让老师去修改成绩
    teacher_obj.change_score(course_name, student_name, score)

    return True, '修改成绩成功!'