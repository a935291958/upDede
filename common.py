# -*- coding: UTF-8 -*-
import os, re, shutil, time, random

import chardet

# 创建日志目录
if not os.path.isdir('./log'):
    os.mkdir('./log')


# 写入日志
def msg(str, type):
    if not str or not type:
        print '日志相关异常'
        return False

    msg = ''
    pMsg = ''

    # 打开日志文件
    f = './log/' + time.strftime("%Y-%m-%d", time.localtime()) + '.log'
    fLog = open(f, 'a')

    # 拼接提示信息
    msg = time.strftime("%H:%M:%S", time.localtime()) + '] ' + str

    if (type == 1):
        msg = '[INFO] [' + msg
        pMsg = '\033[0;32;40m ' + msg

    elif type == 2:
        msg = '[WARNING] [' + msg
        pMsg = '\033[0;33;40m ' + msg

    elif type == 3:
        msg = '[ALERT] [' + msg
        pMsg = '\033[0;35;40m ' + msg

    elif type == 4:
        msg = '[ERROR] [' + msg
        pMsg = '\033[0;31;40m ' + msg

    elif type == 5:
        msg = '[SUCCESS] [' + msg
        pMsg = '\033[0;37;40m ' + msg
    else:
        print  'type参数错误!'
        fLog.close()
        return False

    print pMsg

    fLog.write(msg + '\n')
    fLog.close()

    pass


# 判断是不是文件
def isFile(filename):
    return os.path.isfile(filename)


# 判断是不是目录
def isDir(dir):
    return os.path.isdir(dir)


# 递归删除目录，非空的也可以删除
def remove_dir(dir):
    dir = dir.replace('\\', '/')
    if (os.path.isdir(dir)):
        for p in os.listdir(dir):
            remove_dir(os.path.join(dir, p))
        if (os.path.exists(dir)):
            os.rmdir(dir)
    else:
        if (os.path.exists(dir)):
            os.remove(dir)
    pass


# 获取文件编码
def getDetect(filename):
    if not isFile(filename):
        return False
    f = open(filename, 'r')
    fileData = f.read()
    f.close()
    return chardet.detect(fileData)


# 设置文本为utf-8
def setUtf8(str):
    return str.decode('gbk').encode('utf-8')


# 设置文本为gbk
def setGbk(str):
    return str.decode('utf-8').encode('gbk')


# 设置文件编码
def setCode(old, new):
    return str.decode(old).encode(new)


# 生成随机字符串，输入需要几位数
def salt(num):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(num):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt



# 更新DEDE管理员目录下面的文件
def upAdminFile(fileName, oldStr, newStr, signature, bakDir):
    if (not fileName) or (not oldStr) or (not newStr):
        msg('参数不完整!', 4)
        return
    # 判断是不是文件
    if not os.path.isfile(fileName):
        msg('文件不存在:' + fileName, 4)
        return

    msg('开始修复文件:' + fileName, 1)
    fo = open(fileName, 'r+')

    # 获取编码
    coding = getDetect(fileName)['encoding']

    # 逐行读取文件，
    fileData = ''
    for f in fo.readlines():
        fileData += f

    if coding != 'utf-8':
        signature = setGbk(signature)
        newStr = setGbk(newStr)
        oldStr = setGbk(oldStr)

    if fileData.find(signature) > 0:
        msg('特征码已存在，即可能已修复:' + setUtf8(signature), 3)
        fo.close()
        return True

    # 重新设置文件指针
    fo.seek(0, 0)

    # 替换后的
    newFileData = fileData.replace(oldStr, newStr, 1)
    if (newFileData == fileData):
        msg('未能匹配到需要替换的字符串:' + oldStr, 3)

        # 使用正则匹配
        # newFileData = re.match(oldStr,fileData)

        # print oldStr
        # print newFileData

        return False

    # 修改文件前先备份文件,此操作会覆盖备份文件夹里面的文件
    oldFileBaseName = os.path.basename(fileName)

    # 获取父目录,把路径中的斜杠换成下划线
    father_path = (os.path.abspath(os.path.dirname(fileName))).replace('\\', '_').replace('/', '_').replace(':', '_')

    # 在备份文件夹创建子目录
    bakAllDir = bakDir + father_path
    if not isDir(bakAllDir):
        os.mkdir(bakAllDir)

    # print father_path

    # 拼接成完整的备份文件路径+名
    bakFile = bakAllDir + '/' + oldFileBaseName
    msg('备份源文件： ' + fileName + ' => ' + bakFile, 1)

    # 如果备份目录下面的备份文件已存在，则追加时间戳
    if isFile(bakFile):
        bakFile += repr(int(time.time()))

    # 复制源文件到备份目录下面
    shutil.copyfile(fileName, bakFile)

    # 匹配成功后写入文件
    fo.write(newFileData)

    # 关闭文件
    fo.close()

    pass
