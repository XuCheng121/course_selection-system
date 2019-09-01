# Author: Mr.Xu

# 视图菜单信息
VIEW_MSG = '''
    请选择登录角色：
    1、管理员视图
    2、老师视图
    3、学生视图
    q、退出
'''

# admin菜单
ADMIN_MENU = '''
    1、注册
    2、登录
    3、创建学校
    4、创建老师
    5、创建课程
    q、退出
'''

# student菜单
STUDENT_MENU = '''
    1、注册
    2、登录
    3、选择校区
    4、选择课程
    5、查看成绩
    q、退出
'''

# teacher菜单
TEATHER_MENU = '''
    1、登录
    2、查看教授课程
    3、选择教授课程
    4、查看课程下学生
    5、修改学生成绩
    q、退出
'''

import os

# 配置环境变量
HOME_PATH = os.path.dirname(os.path.dirname(__file__))
DB_DIR_PATH = os.path.join(HOME_PATH, "db")