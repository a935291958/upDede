# -*- coding: UTF-8 -*-

#测试目录：
#  /home/wwwroot/
#           |--  a.com
#                   |-- config
#                   |-- bin
#                   |-- web  #网站存放代码的目录
#           |--  b.com
#                   |-- config
#                   |-- bin
#                   |-- web  #网站存放代码的目录




# 网站根目录
#wwwroot = 'D:/'
wwwroot = '/home/wwwroot/'

# 不要修复的网站根目录，注意区分大小写
# notUp = ['Program Files (x86)','abc']
notUp = ['abc', 'index', 'user']

# 根目录下面的二级目录
# sonDir = '/'  #没有的话这样写
sonDir = '/web/'

# 需要修复管理员的目录
adminList = ['dede', 'gzch1200']

#修改漏洞文件前先备份原来的文件的备份目录
bakDir = './bak/'

#是否删除织梦安装目录install
isDelIns = True




########################以下为要修复的文件########################

# 管理员目录要修复的文件 [文件名,需要替换的字符串,新的字符串,特征码]
adminFile = [
    [
        'media_add.php',
        '$fullfilename = $cfg_basedir.$filename;',
        'if (preg_match(\'#\.(php|pl|cgi|asp|aspx|jsp|php5|php4|php3|shtm|shtml)[^a-zA-Z0-9]+$#i\', trim($filename))) { ShowMsg("你指定的文件名被系统禁止！",\'javascript:;\'); exit(); } $fullfilename = $cfg_basedir.$filename;',
        'php|pl|cgi|asp|aspx|jsp|php5|php4|php3|shtm|shtml',
    ]
]

# 需要修复会员的目录
memberList = ['member']

# member目录要修复的文件
memberFile = [
    [
        'album_add.php',
        '//保存到主表',
        '//保存到主表\r\n $mtypesid = intval($mtypesid);',
        '$mtypesid = intval($mtypesid)'
    ],
    [
        'pm.php',
        '$row = $dsql->GetOne("SELECT * FROM `#@__member_pms` WHERE id=\'$id\' AND (fromid=\'{$cfg_ml->M_ID}\' OR toid=\'{$cfg_ml->M_ID}\')");',
        '$id = intval($id);\n    $row = $dsql->GetOne("SELECT * FROM `#@__member_pms` WHERE id=\'$id\' AND (fromid=\'{$cfg_ml->M_ID}\' OR toid=\'{$cfg_ml->M_ID}\')");',
        '$id = intval($id);'
    ],
    [
        'article_add.php',
        'if (empty($dede_fieldshash) || $dede_fieldshash != md5($dede_addonfields.$cfg_cookie_encode))',
        'if (empty($dede_fieldshash) || ( $dede_fieldshash != md5($dede_addonfields . $cfg_cookie_encode) && $dede_fieldshash != md5($dede_addonfields . \'anythingelse\' . $cfg_cookie_encode)) )',
        '$dede_fieldshash != md5($dede_addonfields . \'anythingelse\' . $cfg_cookie_encode'
    ],
    [
        'inc/inc_archives_functions.php',
        'echo "<input type=\\"hidden\\" name=\\"dede_fieldshash\\" value=\\"".md5($dede_addonfields.$cfg_cookie_encode)."\\" />";',
        'echo "<input type=\\"hidden\\" name=\\"dede_fieldshash\\" value=\\"".md5($dede_addonfields."bearshop.cc".$cfg_cookie_encode)."\\" />";',
        'md5($dede_addonfields."bearshop.cc".$cfg_cookie_encode)'
    ],
    [
        'mtypes.php',
        '$name = HtmlReplace($name);',
        '$name = HtmlReplace($name);\n        /* 对$id进行规范化处理 */\n        $id = intval($id);',
        '$id = intval($id);'
    ],
    [
        'soft_add.php',
        '$urls .= "{dede:link islocal=\'1\' text=\'{$servermsg1}\'} $softurl1 {/dede:link}\\r\\n";',
        'if (preg_match("#}(.*?){/dede:link}{dede:#sim", $servermsg1) != 1) {\n            $urls .= "{dede:link islocal=\'1\' text=\'{$servermsg1}\'} $softurl1 {/dede:link}\\r\\n";\n        }',
        'preg_match("#}(.*?){/dede:link}{dede:#sim", $servermsg1'
    ],
    [
        'inc/archives_check_edit.php',
        '$litpic =$oldlitpic;',
        '$litpic =$oldlitpic; if (strpos( $litpic, \'..\') !== false || strpos( $litpic, $cfg_user_dir."/{$userid}/" ) === false) exit(\'not allowed path!\');',
        '!== false || strpos( $litpic, $cfg_user_dir."/{$userid}/"'
    ]
]

# 需要修复会员的目录
plusList = ['plus']

# plus目录要修复的文件
plusFile = [
    [
        'guestbook/edit.inc.php',
        'else if($job==\'editok\')',
        'else if($job==\'editok\'){ $remsg = trim($remsg); /* 验证$g_isadmin */',
        '$remsg = trim($remsg);'
    ],
    [
        'guestbook/edit.inc.php',
        '$msg = HtmlReplace($msg, -1);',
        '$msg = HtmlReplace($msg, -1);\r\n /* 对$msg进行有效过滤 */ \r\n $msg = addslashes($msg);',
        '$msg = addslashes($msg);'
    ]
]
#include
includeList = ['include']

includeFile = [
    [
        'uploadsafe.inc.php',
        'if(empty(${$_key.\'_size\'}))\n    {\n        ${$_key.\'_size\'} = @filesize($$_key);\n    }',
        '$imtypes=array("image/pjpeg","image/jpeg","image/gif","image/png","image/xpng","image/wbmp","image/bmp");if(in_array(strtolower(trim(${$_key.\'_type\'})),$imtypes)){$image_dd=@getimagesize($$_key);if($image_dd==false){continue;}if(!is_array($image_dd)){exit(\'Upload filetype not allow !\');}}',
        '{$image_dd=@getimagesize($$_key);if($image_dd==false){continue;}if(!is_array($image_dd'
    ],
    [
        'uploadsafe.inc.php',
        '$image_dd = @getimagesize($$_key);',
        '$image_dd = @getimagesize($$_key); if($image_dd == false){ continue; }',
        '$image_dd = @getimagesize($$_key); if($image_dd == false){ continue; }'
    ],
    [
        'payment/alipay.php',
        '$order_sn = trim($_GET[\'out_trade_no\']);',
        '$order_sn = trim(addslashes($_GET[\'out_trade_no\']));',
        'trim(addslashes($_GET[\'out_trade_no\']))'
    ],
    [
        'dedesql.class.php',
        'if(isset($GLOBALS[\'arrs1\']))',
        '$arrs1 = array(); \n$arrs2 = array();\nif(isset($GLOBALS[\'arrs1\']))',
        '$arrs1 = array'
    ],
    [
        'common.inc.php',
        'if( strlen($svar)>0 && preg_match(\'#^(cfg_|GLOBALS|_GET|_POST|_COOKIE)#\',$svar) )',
        'if( strlen($svar)>0 && preg_match(\'#^(cfg_|GLOBALS|_GET|_POST|_COOKIE|_SESSION)#\',$svar) )',
        '#^(cfg_|GLOBALS|_GET|_POST|_COOKIE|_SESSION)#)'
    ]
]