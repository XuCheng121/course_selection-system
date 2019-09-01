from db import models

def register_interface(username, password):
    # 1.判断学生是否存在
    student_obj = models.Student.select(username)

    if student_obj:
        return False, '学生已存在'

    models.Student(username, password)

    return True, f'{username}---学生创建成功!'


# def login_interface(username, password):
#
#     # 1.获取学生对象,判断学生是否存在
#     student_obj = models.Student.select(username)
#     if student_obj:
#         # 判断密码是否一致
#         if student_obj.pwd == password:
#             return True, '登录成功!'
#         else:
#             return  False, '密码错误!'
#
#     else:
#         return False , '用户不存在!'


# 学生选择学校接口
def choose_school_interface(student_name, school_name):

    # 1.判断学生是否拥有学校
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        return False, '学生已选择学校'

    # 2.让学生对象选择学校
    student_obj.choose_school(school_name)
    return True, '选择学校成功!'


# 获取学校下所有课程接口
def get_course_interface(student_name):
    student_obj = models.Student.select(student_name)

    if student_obj.school:
        school_name = student_obj.school
        school_obj = models.School.select(school_name)
        return True, school_obj.school_course_list

    else:
        return False, '请先选择学校!'

# 学生选择课程接口
def choose_course_interface(student_name, course_name):

    # 1.判断该课程是否存在学生课程列表中
    student_obj = models.Student.select(student_name)

    if course_name in student_obj.student_course_list:
        return False, '该课程已经选择过了!'

    student_obj.choose_course(course_name)

    return True, f'{course_name}---课程选择成功!'


# 学生查看成绩接口
def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    score_dic = student_obj.check_score()
    return score_dic
