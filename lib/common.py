

def login_auth(role):
    def auth(func):
        from core import admin, student, teacher
        def inner(*args, **kwargs):

            if role == 'admin':
                if admin.admin_info.get('user'):
                    res = func(*args, **kwargs)
                    return res

                else:
                    admin.login()

            elif role == 'student':
                if student.student_info.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()

            elif role == 'teacher':
                if teacher.teacher_info.get('user'):
                    res = func(*args, **kwargs)
                    return res

                else:
                    teacher.login()

            else:
                print('权限不足!')


        return inner
    return auth