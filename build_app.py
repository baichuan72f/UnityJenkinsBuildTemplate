import os
import subprocess
import time


# 设置你本地的Unity安装目录
unity_exe = r"C:\Program Files\Unity\Hub\Editor\2021.3.4f1\Editor\Unity.exe"
# unity工程目录，当前脚本放在unity工程根目录中
# project_path = sys.argv[1]
# 日志
log_file = os.getcwd() + '/unity_log.log'

static_func = 'BuildTools.BuildApk'

# 杀掉unity进程


def kill_unity():
    os.system('taskkill /IM Unity.exe /F')


def clear_log():
    if os.path.exists(log_file):
        os.remove(log_file)

# 调用unity中我们封装的静态函数


def call_unity_static_func(func, arg):
    kill_unity()
    time.sleep(1)
    clear_log()
    time.sleep(1)
    cmd ='call ' + os.path.abspath('build_app.bat') + ' %s %s %s' % (arg[1], arg[2], arg[3])
    print('run cmd:  ' + cmd)
    os.system(cmd)
    # subprocess.Popen(cmd)


# 实时监测unity的log, 参数target_log是我们要监测的目标log, 如果检测到了, 则跳出while循环
def monitor_unity_log(target_log):
    pos = 0
    while True:
        if os.path.exists(log_file):
            break
        else:
            time.sleep(0.1)
    while True:
        fd = open(log_file, 'r', encoding='utf-8')
        if 0 != pos:
            fd.seek(pos, 0)
        while True:
            line = fd.readline()
            pos = pos + len(line)
            if target_log in line:
                print(u'监测到unity输出了目标log: ' + target_log)
                fd.close()
                return
            if line.strip():
                print(line)
            else:
                break
        fd.close()


def build(arg):
    call_unity_static_func(static_func,arg)
    monitor_unity_log('Build App Done!')
    print('done')


if __name__ == '__main__':
    arr=['C:\ProgramData\Jenkins\.jenkins\workspace\Example01','C:\ProgramData\Jenkins\.jenkins\workspace\Example01','hhh','1.0.0']
    build(arr)
