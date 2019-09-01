# Author: Mr.Xu

import os
import sys
from core import src

# 将文件的绝对父目录路径添加到环境变量
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# 主程
if __name__ == '__main__':
    src.run()