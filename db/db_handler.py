# Author: Mr.Xu

# 数据处理操作

import os
import pickle
from conf import settings

# 读取信息接口
def read_info(cls,name):
    dir_path = os.path.join(settings.DB_DIR_PATH, cls.__name__)
    file_path = os.path.join(dir_path, name)

    if os.path.exists(file_path):
        with open(file_path,"rb") as f:
            return pickle.load(f)
    return False


# 保存信息接口
def save_info(obj):
    dir_path = os.path.join(settings.DB_DIR_PATH, obj.__class__.__name__)

    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    file_path = os.path.join(dir_path, obj.name)
    with open(file_path, "wb") as f:
        pickle.dump(obj,f)
    return True
