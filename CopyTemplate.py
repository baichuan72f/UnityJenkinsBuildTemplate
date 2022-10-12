import os
import shutil
def CopyTemplate(arg):
    source_path = os.path.abspath("D:/Project/BuildTemplate/Template/Editor")
    target_path = arg['WORKSPACE'] + '/Assets/Editor/Build'
    # print(arg)
    print(arg['WORKSPACE'])
    if not os.path.exists(target_path):
        # 如果目标路径不存在原文件夹的话就创建
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(target_path)
    # 复制Template
    shutil.copytree(source_path, target_path)
    print('copy dir finished!')
    # 写入参数
    f = open(target_path + "/arg.txt", "w")
    env = str(arg)
    f.write(env)
    f.close()
    print('write arg finished!')
