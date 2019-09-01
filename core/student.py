from interface import student_interface
from interface import common_interface
from lib import common
student_info = {
    'user': None
}


def register():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        re_password = input('请确认密码:').strip()

        if password == re_password:
            flag, msg = student_interface.register_interface(username, password)
            if flag:
                print(msg)
                break

            else:
                print(msg)
        else:
            print('两次密码不一致!')

def login():
    while True:
        username = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        flag, msg = common_interface.login_interface(username, password, user_type='student')
        if flag:
            print(msg)
            student_info['user'] = username
            break
        else:
            print(msg)

@common.login_auth('student')
def choose_school():
    while True:
        school_list = common_interface.get_school_interface()
        for index, school in enumerate(school_list):
            print(index, school)

        choice = input('请输入选择的学校编号:').strip()

        # 如果不是数字
        if not choice.isdigit():
            print('必须是数字!')
            continue

        choice = int(choice)

        if choice not in range(len(school_list)):
            print('必须输入正确学校编号!')
            continue

        school_name = school_list[choice]

        flag, msg = student_interface.choose_school_interface(
            student_info.get('user'), school_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.login_auth('student')
def choose_course():
    while True:

        # 1.获取学生下学校所有的课程
        flag, course_list_or_msg = student_interface.get_course_interface(
            student_info.get('user'))

        if not flag:
            print(course_list_or_msg)
            break

        if not course_list_or_msg:
            print('没有课程')
            break

        for index, course in enumerate(course_list_or_msg):
            print(index, course)

        choice = input('请选择课程编号:').strip()

        if not choice.isdigit():
            print('请输入数字!')
            continue

        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            print('请选择正确编号')
            continue

        course_name = course_list_or_msg[choice]

        flag, msg = student_interface.choose_course_interface(
            student_info.get('user'), course_name)

        if flag:
            print(msg)
            break

        else:
            print(msg)

    pass

@common.login_auth('student')
def check_score():
    score_dic = student_interface.check_score_interface(student_info.get('user'))
    print(score_dic)


func_dic = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,
}

def student_view():
    while True:
        print('''
        1.注册
        2.登录
        3.选择学校
        4.选择课程
        5.查看成绩
        q.退出
        ''')

        choice = input('请选择学生功能:').strip()

        if choice == 'q':
            break

        if choice not in func_dic:
            print('选择有误!')
            continue

        func_dic.get(choice)()

