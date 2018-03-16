# -*- coding: UTF-8 -*-
from common import *
from config import *

import os, sys

if __name__ != "__main__":
    sys.exit(0)

# WWW目录不存在就退出脚本
if not isDir(wwwroot):
    msg('WWW根目录错误，程序退出', 4)
    sys.exit(0)

# 创建备份目录
if not os.path.isdir(bakDir):
    msg('备份目录不存在,创建备份目录：' + bakDir, 2)
    os.mkdir(bakDir, 0755)


def main(wwwroot, adminList, adminFile, bakDir, isDelIns):
    dirs = ''
    if os.path.exists(wwwroot):
        dirs = os.listdir(wwwroot)

    # 遍历目录
    dirc = ''
    for dirc in dirs:
        # 转换编码，中文会乱码
        dirc = setUtf8(dirc)

        # 拼接成完整的路径
        thisDir = os.path.join(wwwroot, dirc)

        # 判断是不是不用备份的网站
        if dirc in notUp:
            msg('不用备份:' + thisDir, 2)
            continue

        # 拼接子目录
        webDir = thisDir + sonDir

        # 不是目录的话过滤
        if not os.path.isdir(webDir):
            msg('非目录已跳过:' + webDir, 2)
            continue

        # 删除安装目录
        insDir = webDir + 'install'
        if isDelIns and isDir(insDir):
            msg('删除织梦安装目录:' + insDir, 1)
            remove_dir(insDir)
            pass

        for admin in adminList:
            adminDir = webDir + admin
            if not os.path.isdir(adminDir):
                continue

            for aF in adminFile:
                filename = adminDir + '/' + aF[0]
                if not isFile(filename):
                    msg('文件不存在:' + filename, 4)
                    continue


                try:
                    oldStr = aF[1]
                    newStr = aF[2]
                    signature = aF[3]
                except Exception:
                    msg('匹配规则有误,程序退出,请检查config.py的匹配规则,当前匹配规则：'+ repr(aF),4)
                    sys.exit(1)
                    pass

                upAdminFile(filename, oldStr, newStr, signature, bakDir)

    pass


# 修复admin后台目录
main(wwwroot, adminList, adminFile, bakDir, isDelIns)

# 修复会员目录
main(wwwroot, memberList, memberFile, bakDir, isDelIns)

# 修复plus目录
main(wwwroot, plusList, plusFile, bakDir, isDelIns)

# 修复include目录
main(wwwroot, includeList, includeFile, bakDir, isDelIns)

msg('程序执行完毕!', 5)
