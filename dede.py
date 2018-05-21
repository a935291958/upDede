# -*- coding: UTF-8 -*-
from common import *
from config import *

import os, sys, platform, stat, random

if __name__ != "__main__":
    sys.exit(1)

# WWW目录不存在就退出脚本
if not isDir(wwwroot):
    msg('WWW根目录错误，程序退出', 4)
    sys.exit(1)

# 创建备份目录
if not os.path.isdir(bakDir):
    msg('备份目录不存在,创建备份目录：' + bakDir, 2)
    os.mkdir(bakDir, 0755)

# 创建保存结果的目录
if not os.path.isdir(resDir):
    msg('结果目录不存在,创建备份目录：' + resDir, 2)
    os.mkdir(resDir, 0755)


def main(adminList, adminFile):
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

        # 设置data/common.inc.php文件属性设置为644（Linux/Unix）
        dataFile = webDir + 'data/common.inc.php'
        if isSetCommon and isFile(dataFile):
            msg('更改文件目标权限：' + dataFile, 1)
            thisSys = platform.system()
            if ('Windows' == thisSys):
                msg('当前为Windows', 1)
                os.chmod(dataFile, stat.S_IREAD)
            elif ('Linux' == thisSys):
                msg('当前为Linux', 1)
                # 更改权限
                os.chmod(dataFile, 0644)
                # 更改所有者为root
                os.chown(dataFile, 0, 0)
                pass
            pass

        # 更改织梦后台目录
        dedeDir = webDir + 'dede'
        newDedeDir = ''
        if upDedeDir[0] and isDir(dedeDir):

            # 1的的话生成随机目录
            if upDedeDir[1] == 1:
                saltDir = salt(upDedeDir[2])
                newDedeDir = webDir + saltDir
            # 2的话生成指定的目录
            elif upDedeDir[1] == 2:
                newDedeDir = webDir + upDedeDir[2]
                pass

            if newDedeDir and not isDir(newDedeDir):
                os.rename(dedeDir, newDedeDir)

                # 写入结果
                f = resDir + time.strftime("%Y-%m-%d", time.localtime()) + '.log'
                fRes = open(f, 'a')
                fRes.write(dedeDir + ',' + newDedeDir + '\n')
                fRes.close()
                msg('更改织梦后台目录成功  源目录=>' + dedeDir + '  目标目录=>' + newDedeDir, 1)
            else:
                msg('更改织梦后台目录失败  源目录=>' + dedeDir + '  目标目录=>' + newDedeDir, 4)
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
main(adminList, adminFile)

# 修复会员目录
main(memberList, memberFile)

# 修复plus目录
main(plusList, plusFile)

# 修复include目录
main(includeList, includeFile)

msg('程序执行完毕!', 5)
