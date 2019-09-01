# Author: Mr.Xu

# 通用操作接口

import os
from conf import settings

def get_school_list():
    path = os.path.join(settings.DB_DIR_PATH,"School")

    if os.path.exists(path):
        return os.listdir(path)

def get_course_list():
    path = os.path.join(settings.DB_DIR_PATH, "Course")

    if os.path.exists(path):
        return os.listdir(path)