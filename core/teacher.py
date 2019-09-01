from interface import teacher_interface
from interface import common_interface
from lib import common

teacher_info = {
    'user': None
}

def login():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        flag, msg = common_interface.login_interface(username, password, user_type='teacher')
        if flag:
            teacher_info['user'] = username
            print(msg)
            break
        else:
            print(msg)

# 查看教授课程
@common.login_auth('teacher')
def check_course():
    flag, course_list_or_msg = teacher_interface.check_course_interface(
        teacher_info.get('user'))
    if flag:
        print(course_list_or_msg)

    else:
        print(course_list_or_msg)


# 选择教授课程
@common.login_auth('teacher')
def choose_course():
    while True:
        # 1.查看所有课程
        course_list = common_interface.get_courses_interface()

        if not course_list:
            print('没有课程')
            break

        # 2.打印所有课程,并选择
        for index, course in enumerate(course_list):
            print(index, course)

        choice = input('请输入课程编号:').strip()

        if not choice.isdigit():
            print('必须是数字')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('请选择正确编号!')
            continue

        course_name = course_list[choice]

        flag, msg = teacher_interface.choose_course_interface(
            teacher_info.get('user'), course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 查看课程下学生
@common.login_auth('teacher')
def check_student():
    while True:
        # 1.获取老师下所有课程
        flag, course_list_or_msg = teacher_interface.check_course_interface(
            teacher_info.get('user'))

        if not flag:
            print('没有课程')
            break

        for index, course in enumerate(course_list_or_msg):
            print(index, course)

        choice = input('请输入课程编号:').strip()

        if not choice.isdigit():
            continue

        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            continue

        course_name = course_list_or_msg[choice]

        # 调用查看课程下学生接口
        flag, student_list_or_msg = teacher_interface.check_student_interface(
            teacher_info.get('user'), course_name)

        if flag:
            print(student_list_or_msg)
            break

        else:
            print(student_list_or_msg)
            break


# 修改学生分数
@common.login_auth('teacher')
def change_score():
    while True:
        # 1.获取当前老师下所有的课程
        flag, course_list_or_msg = teacher_interface.check_course_interface(
            teacher_info.get('user'))

        if not flag:
            print('老师下没有课程')
            break

        for index, course in enumerate(course_list_or_msg):
            print(index, course)

        choice = input('请选择课程编号:').strip()

        if not choice.isdigit():
            continue

        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            continue

        course_name = course_list_or_msg[choice]

        flag, student_list_or_msg = teacher_interface.check_student_interface(
            teacher_info.get('user'), course_name)

        # 若有学生,则循环打印学生列表,让老师选择学生
        if not flag:
            print(student_list_or_msg)
            break

        for index, student in enumerate(student_list_or_msg):
            print(index, student)

        choice2 = input('请选择学生编号:').strip()

        if not choice2.isdigit():
            continue

        choice2 = int(choice2)

        if choice2 not in range(len(student_list_or_msg)):
            continue

        student_name = student_list_or_msg[choice2]

        # 输入修改学生的成绩
        score = input('请输入修改的成绩:').strip()

        flag, msg = teacher_interface.change_score_interface(
            teacher_info.get('user'), course_name, student_name, score
        )
        if flag:
            print(msg)
            break

func_dic = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_student,
    '5': change_score,
}

def teacher_view():
    while True:
        print('''
        1.登录
        2.查看教授课程
        3.选择教授课程
        4.查看课程学生
        5.修改学生成绩
        q.退出
        ''')

        choice = input('请选择老师功能:').strip()

        if choice == 'q':
            break

        if choice not in func_dic:
            print('选择有误!')
            continue

        func_dic.get(choice)()



