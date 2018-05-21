# 织梦漏洞修复工具

运行环境：python2.6

使用模块：os, sys,shutil, time,chardet

使用说明： 更改config.py里面的配置，根据实际修改：wwwroot、notUp、sonDir、adminList、bakDir、isDelIns等等参数。
默认删除织梦安装目录install。设置data/common.inc.php文件属性设置为644（Linux/Unix）或只读（NT）。更改默认的DEDE目录为随机目录


##### 文件目录:

    config.py
        |
        |__配置文件

    dede.py
        |
        |__主文件

    common.py
        |
        |__公共函数库

    bak
        |
        |__备份源文件的目录
    log
        |
        |__日志目录
    res
        |
        |__结果保存目录



#### 更新：

    **时间** ：2018年5月21日16:41:35
    **内容** ：
        1、新增设置data/common.inc.php文件属性设置为644
        2、新增更改默认的DEDE目录
        3、修复部分识别码不能识别



欢迎使用，交流请发邮件935291958@qq.com，如果想请我喝杯咖啡，请扫码以下二维码，3Q。

![a](https://github.com/a935291958/upDede/blob/master/yz.jpg?raw=true)


