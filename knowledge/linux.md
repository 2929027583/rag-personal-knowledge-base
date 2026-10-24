#  一.目录结构
## 进入根目录
查看根目录下的文件

cd /

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1783517631308-97e1d901-e930-4029-ba90-d86a2a962dfe.png" width="948.6666666666666" alt="" title="" crop="0,0,1,1" id="ua473133f" class="ne-image">

## 目录结果详解
### bin目录
bin:binariesdes的缩写，是用来存放二进制的可执行文件

查看bin目录下的文件

cd bin/

ls

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1783518537445-54e69b59-1ab8-42b0-be61-158b6c0a947c.png" width="1360" alt="" title="" crop="0,0,1,1" id="ubefd9e3d" class="ne-image">

sbin:（super user  binaries ）存放的二进制可执行文件，只有root（超级管理员）才能访问

先回到根目录

cd ../回到上一级

cd sbin/切换到sbin目录

ls 查看文件

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1783518673735-bd36a104-e864-4dcf-aa0a-eef755477f21.png" width="1566.6666666666667" alt="" title="" crop="0,0,1,1" id="u2e5d4b26" class="ne-image">

### 其他目录
dev:(device）用来存放设备文件 

home:存放用户文件的根目录

mnt :(mount)超级管理员安装临时文件系统的安装点

tmp:(temporary)临时文件存放点

usr:(unix shared resources)存放共享系统资源

boot:存放用于系统引导使用的文件

etc:存放系统配置文件

root:系统管理员的用户主目录

lib：共享库，相当于Windows的dil文件

src:(service):存放服务启动之后需要提取的数据

proc：系统内存映射，虚拟目录，进入目录可以看到系统信息

obt：额外安装软件的时候存放目录

var: 存储不断增多的这种文件，比如日志文件

run: 系统运行所需文件

media:U盘，光盘临时放的文件

# 二.系统管理
## 1.linux用户
### 1.1概述
linux系统是一个多用户多任务的操作系统，任何一个要使用系统资源的用户，都必须首先向系统管理申请一个账号，然后以这个账号的身份进入系统，root用户是系统默认创建的管理员账号

### 1.2添加用户
```plain
useradd [选项] 用户名
```

```plain
useradd jh
```

```plain
passwd jh
draken123
```

添加成功

添加一个新的会话

用户名：jh

密码：draken123

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1783824586830-533fcd57-7e04-4b38-8c9c-24ed2573e471.png" width="654.6666666666666" alt="" title="" crop="0,0,1,1" id="ufb5c19e3" class="ne-image">

### 1.3删除用户
```plain
语法
userdel [选项] 用户名
删除用户同时将目录删除
userdel -r 用户名
```

### 1.4查询用户
```plain
语法
id 用户名
```

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1783827234323-f88b963c-0d94-4d6f-bbf0-adb2b18a0fc7.png" width="415.1111111111111" alt="" title="" crop="0,0,1,1" id="u849aec11" class="ne-image">

### 1.5切换用户（重点）
```plain
语法
su 用户名
切换到zs用户
su zs
```

注意：高权限的用户切换到低权限的用户不需要输入密码，但是低权限的用户切换到高权限寻密码

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1783827444066-653a8232-3ea4-464c-9139-fe98d0b502a3.png" width="345.77777777777777" alt="" title="" crop="0,0,1,1" id="ud239f8ba" class="ne-image">

## 2.linux组管理
### 2.1概述
linux的组类似于角色，系统可以对有共性的多个用户进行统一的管理，每一个用户都至少属于一个组，创建用户是如果不指定组，会默认创建一个跟用户名相同的组，并且把新创建的用户分配到组中，root用户默认属于root组

### 2.2添加组
```plain
语法
groupadd 组名
添加sy-group
groupadd sy-group
```

### 2.3删除组
```plain
语法
groupdel 组名
删除sy-group
groupdel sy-group
```

### 2.4新添加用户属于某一组
```plain
语法
useradd -g 组名 用户名
添加ww用户属于sy-group
useradd -g sy-group ww
```

查看信息

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1783840742319-8b0e3139-0e1b-4f94-88e4-2edfe52d9557.png" width="537.7777777777778" alt="" title="" crop="0,0,1,1" id="u4a6807fd" class="ne-image">

### 2.5将用户从指定组删除
```plain
语法
-a表示add
-d表示delete
gpasswd -a/-d 用户名 组名
将ww从sy-group删除
gpasswd -a ww sy-group
查看所有组的信息
cat /etc/group
```

## 3.VI与VIM
### 3.1概述
vi编辑器：是linux和unix上最基本的文本编辑器，工作在字符模式下，由于不需要图形界面，vi是效率很高的文本编辑器

vim编辑器：vi的增强版，比vi更容易使用，vi的命令几乎全部都可以在vim上使用

### 3.2vi和vim三种常见模式
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1783844076480-ba69c115-1233-4f87-b991-8bc4755ba01c.png" width="584.4444444444445" alt="" title="" crop="0,0,1,1" id="u0d7c6f0f" class="ne-image">

+ 一般模式：以vi/vim命令打开一个档案就直接进入一般模式了（这是默认的模式）
+ 编辑模式：通常使用i来进入编辑模式
+ 命令模式：在这个模式当中，可以提供你相关指令，完成读取，存盘，替换，离开vim，显示行号等

### 3.3常用操作
+ 一般模式下
    - 拷贝当前行yy
    - 粘贴下一行p
    - 删除当前行dd
    - 跳转到文档最末行G
    - 最首行gg
    - 光标移动到具体行数（行数）shift +G
    - u是撤销
    - 快速移动
        * end快速跳转到行末
        * home移动到头部
+ 命令行模式下 ：/查找的单词  
    - n切换下一个查找的单词
    - N切换上一个查找的单词
    - 设置行号set nu
    - 取消行号set nonu
    - q是退出文档
    - 保存文档wq
    - ！表示强制执行

# 三.linux实操指令
## 一.帮助指令
### 1.man指令
```shell
man [命令或配置文件] //功能描述：获得帮助手册上的信息
查看ls命令的帮助信息
man ls 
name ：命令名称
SYNOPSIS ：如何使用命令
DESCRIPTION ：描述命令
SEE ALSO ：相关手册
```

### 2.help命令
```shell
help [命令] //功能描述：获得命令内置的帮助信息
查看cd命令的帮助信息
help cd
注意：不用特意去记什么命令用什么帮助指令，随便用，会给提示的
```

## 二.文件目录相关指令
### 1.pwd 显示当前工作路径
语法

`pwd`

查看当前工作目录

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1785249921763-ec8baea7-ee78-4da4-9105-b7e4292b4df5.png" width="352.53333333333336" alt="" title="" crop="0,0,1,1" id="ub1d94018" class="ne-image">

### 2.ls列出目录内容
```shell
ls [选项] [目录或是文件]
ls -a 列出全部文件，包括隐藏文件
ls -i 列出文件名称和iNode编号
ls -al 列出所有文件详细信息
```

ls -al

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1785252103723-d5a29d2b-4b4c-4aad-b881-6e86470b3775.png" width="602.1333333333333" alt="" title="" crop="0,0,1,1" id="uca8d4193" class="ne-image">

### 3.cd切换目录
```shell
cd [参数] 
功能描述：切换到指定目录
```

案例

+ 切换到根目录
    - cd /
+ 切换到目录home目录
    - cd /home
+ ./代表当前目录
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1785253304659-a3ccc1b1-f082-4f3e-bb46-e4ca82a37973.png" width="360" alt="" title="" crop="0,0,1,1" id="u6b5a7170" class="ne-image">
+ ../代表上一层目录
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1785253300215-781b9bb5-23c4-4159-9523-ded914df2891.png" width="360" alt="" title="" crop="0,0,1,1" id="u351ec552" class="ne-image">
+ cd ~切换到用户家目录
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1785253254002-51dad86a-a841-407d-a989-84ed3f5dc731.png" width="432.53333333333336" alt="" title="" crop="0,0,1,1" id="ued5fd874" class="ne-image">
+ 注意：可以用tab键位补全路径

### 4.mkdir创建目录
+ 语法
    - mkdir 目录（可以是多级目录）
+ 在ww目录下创建test和app目录
    - mkdir test
    - mkdir /home/ww/app

### 5.rmdir
+ 语法
    - rmdir 目录名称
+ 删除ww下的test目录
    - rmdir /home/ww/test

### 6.touch创建空文件
+ 语法
    - touch 文件名称列表
+ 在ww目录下创建db.properties文件
    - touch db.properties
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1785338818322-ce9fdfe0-cdef-4ff6-a80e-24c9569b4861.png" width="542.9333333333333" alt="" title="" crop="0,0,1,1" id="ue0ede9b7" class="ne-image">

### 7.cp拷贝文件，目录
+ 语法
    - cp [选项] source dest  //source 源文件 dest 目标文件
    - cp -r source dest 递归拷贝
+ 拷贝a.txt文件到zs目录下
    - cp a.txt  /home/zs
    - cp a.txt ../zs
+ cp -r source dest 
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1785339844183-41df5cb5-5275-4cd3-82b6-1b89ee0475fd.png" width="538.1333333333333" alt="" title="" crop="0,0,1,1" id="u3dffa6c2" class="ne-image">
    - 覆盖不提示\cp -r source dest

### 8.rm删除目录，文件
+ 语法
    - rm [选项] 要删除的文件或目录
    - 常用选项：
        * -r ：递归删除整个文件夹
        * -f ：强制删除不提示
+ 删除sy目录下ww目录及其目录下文件
    - rm -rf  ww
+ rm -rf 慎用（有把握才使用）

### 9.mv移动目录，文件或者重命名
+ 重命名语法
    - mv oldNameFile newNameFile
+ 重命名sy下a.txt文件叫test.txt
    - mv a.txt test.txt
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1785340428880-8590224e-bd6e-4e25-a9fa-e38f3c570d11.png" width="544.5333333333333" alt="" title="" crop="0,0,1,1" id="u309c9aa5" class="ne-image">
+ 移动sy目录下的test.txt文件到ww文件夹下
    - mv test.txt /home/ww/
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1785340716793-86274c69-3d3a-404b-9011-0996cf3e4904.png" width="536.5333333333333" alt="" title="" crop="0,0,1,1" id="u4ab4c700" class="ne-image">

### 10.cat查看文件内容
+ 语法
    - cat [选项] 要查看的文件名
    - 常用选项
        * -n ：显示行号
+ 查看目录opt下的test.txt文件
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1785754442846-4cae2bba-1723-4ed5-8280-e66cd5995152.png" width="485.3333333333333" alt="" title="" crop="0,0,1,1" id="u6c141fe1" class="ne-image">

### 11.more把文件内容分屏查看
+ 语法
    - more 要查看的文件名
    - 功能说明·：more是一个基于vi编辑器的文本过滤器，它以全屏幕的方式按页显示文本文件的内容
    - 空格键向下翻页
    - enter向下翻行
    - q 退出
    - = 查看行数
+ 查看test.txt文件
    - more test.txt

### 12.less 用于大文件显示    
+ 根据内容需要显示，所以支持大文件的查找效率更高
+ 语法
    - less 文件
    - 空格向下翻页
    - enter向下翻行
    - q 退出
    - /内容  向下查找内容 n向下查找 N向下查找
    - ？内容 向上查找内容 n向上查找 N向下查找

### 13.head 显示文件头部内容
+ 语法：
    - head 文件（默认查看10行文件）
    - head -n 5 文件（查看5行文件）
    - -n 代表行数

### 14.echo输出内容到控制台
+ 语法
    - echo [选项] [输出内容]
    - 功能介绍：输出常量和变量内容到控制台
+ 控制台打印hello world 
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786169296715-36a325fc-3e6f-403b-9240-e9c124cf8fe3.png" width="518.9333333333333" alt="" title="" crop="0,0,1,1" id="u37a9cd69" class="ne-image">

### 15.重定向输出>和>>
+ 语法
    - 查看指令>目标文件
    - 将前一个查看指令的结果覆盖写入到目标文件中，如果文件不存在，则新建
    - 查看指令>>目标文件
    - 将前一个查看指令的结果追加·写入到目标文件中，如果文件不存在，则新建
+ 操作
    - ls -al > pwd.txt
    - ls -al >> pwd.txt

### 16.history 查看执行过的历史命令
+ 语法
    - history

## 三.查看日志常用
### 1.head 显示文件头部内容
+ 语法：
    - head 文件（默认查看文件头部10行内容）
    - head -n 5 文件（查看文件头部5行内容）
    - -n 代表行数

### 2.tail 显示文件尾部内容
+ 语法：
    - tail 文件（默认查看文件尾部10行内容）
    - tail -n 5 文件（查看文件尾部5行内容）
    - -n 代表行数
    - 常用-f追加新内容，监听文件的内容变化

## 四.时间日期指令
### 1.date 指令
+ 语法
    - date [选项] [format]
+ 显示当前时间
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786177374271-71fe75c6-ee68-4cbb-ba44-41ebe0617eea.png" width="488.53333333333336" alt="" title="" crop="0,0,1,1" id="u4194d0b6" class="ne-image">
+ 显示年月日
    - date  +"%y"
    - date  +"%m"
    - date  +"%d"

### 2.cal查看日历
+ 语法
    - cal

## 五.搜索查找指令
### 1.find查找文件或目录
+ 概述：find指令将从指定目录向下递归地遍历其各个子目录，将满足条件的文件或者目录显示在终端
+ 语法
    - **find [搜索范围] [选项]**
    - -name按照指定名称查找
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786248309351-d080a5b4-5f7d-4bc8-918c-ec01a7d6b7e3.png" width="526.9333333333333" alt="" title="" crop="0,0,1,1" id="u6ffbf91a" class="ne-image">
    - **-size 查找指定大小的文件**
        * +大于
        * <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786248504249-9df7d78c-cd2e-4d8b-b6d6-9964ec295121.png" width="808.5333333333333" alt="" title="" crop="0,0,1,1" id="ud3dcbf62" class="ne-image">
        * - 小于
        * <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786248757400-8d3812c4-a1cf-414e-9e79-3662a8eb1902.png" width="437.3333333333333" alt="" title="" crop="0,0,1,1" id="u253b4774" class="ne-image">
    - **-user 查询某一个用户拥有的文件**
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786248864115-bc7f361c-bb22-4f30-99c1-82e5256915e4.png" width="842.1333333333333" alt="" title="" crop="0,0,1,1" id="u7f550208" class="ne-image">

### 2.locate快速定位文件路径
+ 概述：locate指令可以快速在整个系统中定位文件路径。locate指令利用事先建立的系统中所有文件名称及路径的locate数据库实现快速定位给定的文件，locate指令无需遍历整个文件系统，查询速度较快。为了保证结果的准确度，使用前update db创建locate数据库
+ 语法
    - locate 要搜索的文件名
    - 先安装locate
        * yum install mlocate
    - 查找文件
        * <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786262568665-c0ddd475-685c-4074-9091-02db37cb4aff.png" width="461.3333333333333" alt="" title="" crop="0,0,1,1" id="uc9dedf89" class="ne-image">

### 3.管道符
+ 概述：管道符“|”,表示将前一个命令的处理结果输出传递给后面的命令处理

### 4.grep过滤查找
+ 语法
    - grep [选项] PATTERN [file]

## 六.压缩与解压缩指令
### 1.gzip与gunzip
+ 语法
    - gzip 文件 压缩文件后缀名.gz文件
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786263678254-32f27fb0-934f-4088-a631-4b28760743cc.png" width="508.8" alt="" title="" crop="0,0,1,1" id="ud6762dca" class="ne-image">
    - gunzip 文件.gz 解压文件
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786263828389-afe46b7e-e54d-4079-ac6a-2729a08aeff8.png" width="549.3333333333334" alt="" title="" crop="0,0,1,1" id="u71bd9bc2" class="ne-image">
        * 注意：
            + 不会保留原来文件
            + 不能压缩目录，只能压缩文件
            + 压缩多个文件也是出来多个压缩包

### 2.zip与unzip
+ **解压和压缩之后原文件还会保留**
+ **需要先安装yum install zip**
+ 语法
    - zip [选项] 名称.zip 压缩文件
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786448956811-39977d87-f37f-42af-b827-0b7aa8dfae75.png" width="718.9333333333333" alt="" title="" crop="0,0,1,1" id="uf7d2afc4" class="ne-image">
    - unzip [选项] 名称.zip
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786449749835-30952186-ac78-4720-a9ad-8fdb79c743b7.png" width="722.1333333333333" alt="" title="" crop="0,0,1,1" id="uecdeab71" class="ne-image">
    - 解压到指定目录
    - unzip  名称.zip  -d  目录名
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786449990556-9477ba8c-85f2-47a0-8d9a-842055f16b88.png" width="562.1333333333333" alt="" title="" crop="0,0,1,1" id="u35480d0b" class="ne-image">
    - 压缩到指定目录
    - zip  名称.zip  -r  目录名

### 3.tar打包命令
+  语法
    - tar [选项] xxx.tar.gz [打包的内容]
        * 选项说明
            + -c ：产生.tar.gz打包文件
            + -v ：显示详细信息
            + -f  ：指定压缩后的文件名
            + -z  ：打包同时压缩
            + -x  ：解压.tar.gz文件
            + -c  ：指定解压到哪个目录
    - **压缩文件 tar  -zcvf**
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786451130567-fc9d5f0e-0240-4c2e-ad57-cd51f92bbdce.png" width="913.6" alt="" title="" crop="0,0,1,1" id="u0fcdeea2" class="ne-image">
    - **解压文件 tar  -zxvf**
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786451254898-b9d366a1-0cb5-49ce-b34e-949e509af8c5.png" width="720" alt="" title="" crop="0,0,1,1" id="u37fc6fb6" class="ne-image">

## 七.文件权限指令
   概述:linux文件调用权限分为三级（owner）(group) (otherusers)         

### 1.每个位置代表的权限<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786535689976-895160f0-066c-46ff-8847-13439b37d776.png" width="918.9333333333333" alt="" title="" crop="0,0,1,1" id="u06fcf185" class="ne-image">
### 2.作用与文件和目录的区别
+ 文件
    - r ---读
    - w---写（有写的权限不代表可以删除该文件，必须具有该**文件目录**写的权限才能删除）
    - x ---执行
+ 目录
    - r ---读
    - w ---写（目录内创建，删除，重命名目录）
    - x ---执行

### 3.操作演示
+ **ll 查看当前目录下所有文件和目录的权限**

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786535394061-5e2c4b1f-3729-449f-ad14-e5a2717090bc.png" width="1145" alt="" title="" crop="0,0,1,1" id="ub06132c6" class="ne-image">

### 4.chmod 改变文件和目录的权限
+ 语法
    - chmod 【model=421】文件或者目录

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786536221231-3c57951f-bfbf-4477-84af-fa550d2d59df.png" width="1207" alt="" title="" crop="0,0,1,1" id="u5cf1ae71" class="ne-image">

+ 数字最好用

### 5.chown改变所有者
+ 语法
+ chown 【用户】【文件目录】

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786536491875-996ad424-b820-441a-80ae-291fa1fe7237.png" width="1171" alt="" title="" crop="0,0,1,1" id="u0ba8d488" class="ne-image">

### 6.chgrp改变所属组
+ 语法
+ chgrp 【用户组】【文件目录】

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786536649589-83e65ad7-41f7-418d-8166-e70cbd858d74.png" width="1209" alt="" title="" crop="0,0,1,1" id="uf29054fa" class="ne-image">

改变目录的操作

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1786536846576-ffc35244-07b4-4c7d-91ed-7ba2b2d00713.png" width="1199" alt="" title="" crop="0,0,1,1" id="ue4120fab" class="ne-image">

### 7.总结
+ 第一不要轻易去动文件权限，除非你的leader让你去动
+ 留个心眼，避免同时坑你的时候，害你加班

## 八.磁盘查看
### 1.du查看目录或者文件的磁盘空间占用
+ 概述: disk usage
+ 语法
    - du 【可选】 目录或文件
        * 可选
            + -h 以K-M-G
            + -a 查看目录及其文件大小
            + -c 显示总和和目录和子目录大小
            + -s 只显示总和  

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787020604459-2777840c-0bb4-401b-8d81-181bbafeba62.png" width="1099" alt="" title="" crop="0,0,1,1" id="uee417068" class="ne-image">

### 2.df磁盘空间余额情况
+ 概述：disk free 空余空间
+ 语法
    - df 【-h】

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787021028551-6b839e09-729b-4df5-962c-4aec59c4c676.png" width="762.6666666666666" alt="" title="" crop="0,0,1,1" id="uf24e1182" class="ne-image">

# 四.进程管理
## 1.进程概述
+ 进程是正在执行的程序或命令，每一个进程都独立运行，都有自己的地址空间，并占用一定的系统资源
+ 以后开发会遇见：
    - 端口占用
    - 出现程序假死，卡死

## 2.查看系统运行进程
+ 语法
    - ps 【参数】
    - -a 显示当前终端下的所有进程信息
    - -u 以用户的格式显示进程信息
    - -x 显示后台进程运行的参数
    - -e 显示所有进程信息
    - -f 以全格式显示进程信息
+ 常用命令
    - ps -ef|grep xxx
    - ps -aux|grep xxx
+ ps -ef|grep xxx

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787022463731-dc583c06-e8b9-45f0-9550-51c69d3bc8c4.png" width="1049.0666666666666" alt="" title="" crop="0,0,1,1" id="u7d905f14" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787022629466-c72db060-206c-48fd-bc5c-e889cb952064.png" width="1285.8666666666666" alt="" title="" crop="0,0,1,1" id="ub39f5fe9" class="ne-image">

| 信息 | 说明 | |
| --- | --- | --- |
| UID | 用户id | |
| PID | 进程id | |
| PPID | 父进程id | |
| C | cpu计算优先级因子 | |
| STIME | 进程启动时间 | |
| TTY | 终端名称 | |
| TIME | cpu运行时间 | |
| CMD | 启动进程所用的命令和参数 | |


+ ps -aux|grep xxx

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787023290472-cc928547-f4d8-4921-9639-f18d76f591d1.png" width="1348.2666666666667" alt="" title="" crop="0,0,1,1" id="u86aa9388" class="ne-image">

| 信息 | 说明 | |
| --- | --- | --- |
| USER | 进程产生的用户 | |
| PID<br/>%CPU<br/>%MEM<br/>VSZ<br/>RSS<br/>TTY<br/>STAY<br/>START<br/>TIME<br/>CMD | 进程id<br/>cpu执行占用%比<br/>内存占用率<br/>占用虚拟内存大小KB<br/>占用实际物理内存大小KB<br/>终端名称<br/>进程状态S：睡眠R：运行T：暂停Z：僵尸状态s：包含子进程，l：多线程<br/>进程启动时间<br/>进程占用cpu运算时间<br/>运行命令 | |


## 3.终止进程
+ 语法
    - kill 【选项】pid（进程名称）
    - 选项 -9 强制杀进程
    - 演示杀进程
    - kill -9 pid 

## 4.top监控系统进程
+ 语法
    - top 【选项】 
+ 选项
    - -d 秒：每隔几秒更新
    - -i ：不显示闲置僵死的进程
    - -p ：监控具体进程ip
+ 排序显示
    - p ：以cpu使用率排序
    - M ：以内存使用率排序
    - N ：以PID排序
    - q ：退出

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787037144061-e7cf6e02-3acd-4fe1-a47a-5357bc4863a1.png" width="1243.7333333333333" alt="" title="" crop="0,0,1,1" id="u5d3b0ebe" class="ne-image">

## 5.netstat显示网络状态或者端口占用信息
+ 语法
    - netstat -anp|grep pid
    - netstat -nlp|grep port
+ 选项
    - -a：显示所有正在监听和未监听的套接字（socket）
    - -n：能显示数字显示数字，不显示别名
    - -l：列出监听的服务状态
    - -p：列出进程调用
+ 查看端口是否占用

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787108716423-6cfe1d6a-9677-4320-9a12-36efc05142c2.png" width="1149.8666666666666" alt="" title="" crop="0,0,1,1" id="u7b568e51" class="ne-image">

+ 通过端口是否占用，可以快速的给出自己信息方便部署项目

# 五.服务管理
## 1.概述
** 服务**：是支持linux运行的一些必要程序，本质上也是进程，叫**守护进程**。比如sshd，防火墙等

## 2.指令
+ 语法
    - systemctl【可选】服务名称
        * 可选参数
            + start开启
            + stop停止
            + restart重启
            + reload重新加载
            + status服务状态
            + enable开机启动

## 3.防火墙的操作
+ firewalld 服务名称
+ 查看状态操作
    - systemctl status firewalld

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787109631179-0e4afdc7-8df6-4578-8916-62369aeda8b5.png" width="1349.8666666666666" alt="" title="" crop="0,0,1,1" id="u0268f3a2" class="ne-image">

+ 停止防火墙操作
    - systemctl stop firewalld

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787110285105-ece7dd14-80fa-44e9-be21-3ff2a2819ec0.png" width="1349.3333333333333" alt="" title="" crop="0,0,1,1" id="u46b7a021" class="ne-image">

+ 开启防火墙操作
    - systemctl start firewalld

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787110382615-3f5266b6-0af9-4d81-a82d-fcb0eebdcfa7.png" width="1351.4666666666667" alt="" title="" crop="0,0,1,1" id="ufc534ab1" class="ne-image">

## 4.开放指定端口
+ **问题**：以后部署项目的时候，经常发现访问不了，或者从本地开发环境测试的中间件观察数据时，发现联不通

### 4.1检测防火墙是否开启
+ systemctl status firewalld

### 4.2开放指定端口
+ **需求：开放8080端口**
    - 检测8080端口是否已经开通
    - telnet ip port
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787295651867-45821537-7839-4efc-8037-614fc814ecea.png" width="427.73333333333335" alt="" title="" crop="0,0,1,1" id="u3ab88171" class="ne-image">
    - 开启Windows的telnet命令
        * 打开控制面板
        * 点击程序
        * <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787295748766-288b8f88-d991-4cf0-a8b9-40d3e5dde8bf.png" width="443.42857142857144" alt="" title="" crop="0,0,1,1" id="uefd4fe52" class="ne-image">
        * 启动或关闭Windows功能
        * <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787295844843-7f330e93-ee80-47ec-b442-2f67b23f5261.png" width="404.57142857142856" alt="" title="" crop="0,0,1,1" id="ueb75edb8" class="ne-image">
        * 勾选中telnet客户端
        * <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787295914388-adf0b84b-2610-4003-8575-f2bcda0c316c.png" width="238.0952380952381" alt="" title="" crop="0,0,1,1" id="ub35ae0e6" class="ne-image">
        * 测试8080端口是否通
        * <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787296418415-1752b0ee-53a5-4bdd-a007-58d239382924.png" width="418.2857142857143" alt="" title="" crop="0,0,1,1" id="ubbc7d4c5" class="ne-image">
    - 使用命令添加端口
    - firewall-cmd --zone=public --add-port=8080/tcp --permanent
        * 命令含义
            + -zone #作用域
            + -add-port=8080/tcp #添加端口，格式为：端口/通讯协议
            + -premanent #永久生效，没有此参数重启后失效

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787296732889-27e02f28-bf97-4be2-9caf-2f599cb00498.png" width="738.2857142857143" alt="" title="" crop="0,0,1,1" id="u27c98689" class="ne-image">

    - 查看端口是否开启成功ww
        * firewall-cmd --query-port=8080/tcp
    - 重启防火墙
        * firewall-cmd --reload      

## 5.查看网络是否通
#### ping命令
+ **ping命令**：是一种网络检测工具，他主要适用于检测远程主机是否正常，或是两部主机间的介质是否为断，网线是否脱落或网卡故障
    - 语法
        * ping 目标ip
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787298863739-1c888fb9-cf00-4d68-afc0-7fac31a74cf4.png" width="332.1904761904762" alt="" title="" crop="0,0,1,1" id="u9adc6089" class="ne-image">

#### curl命令
+ **curl命令**：用来发送HTTP请求
    - 语法
        * curl 【可选】
        * 可选
            + -X参数：指定请求方式
            + -V参数：显示响应结果
            + -U参数：携带用户名/密码
            + -H参数：携带请求消息头信息
    - 给百度发起请求
        * curl -X get -v https://www.baidu.com

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787299300446-50db274c-7351-418d-b746-018826455921.png" width="900.1904761904761" alt="" title="" crop="0,0,1,1" id="u5b303aae" class="ne-image">

#### telnet命令
+ telnet:测试端口通否
    - 语法
        * telnet ip port

测试与www.sycoder.cn 80端口通与否

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787299948223-88759324-330c-4a73-b381-a2fcf20e9f5d.png" width="454.0952380952381" alt="" title="" crop="0,0,1,1" id="u61fd7ea7" class="ne-image">

## 6.linux系统操作
+ **作为开发人员几乎不用**
+ 重启
    - 立刻重启
        * shutdown -r now
        * reboot
+ 关机
    - shutdown now
+ 注意：不到万不得已，不要去用，除非你的领导让你去用

# 六.软件包管理
## 1.文件上传与下载
+ 先下载lrzsz工具
    - yum install lrzsz
+ 用来做文件上传与下载的
+ rz从Windows上传文件到linux
    - rz 会弹出一个选择框
+ sz从linux下载文件到Windows
    - sz 文件名
+ 应用场景
    - **修改上传配置文件**
    - **上传jar包**

## 2.RMP包管理（了解）
###    
+ 概述：用于互联网下载包的打包及安装工具，它生成具有.RPM扩展名的文件

## 3.yum包管理
### 3.1概述
+ 概述：yum是一个shell前段软件包管理器。**基于RPM包管理**，能够从指定的服务器（在公网上）**自动下载RPM包并且安装**，可以**自动处理赖性关系**，并且一次安装所有依赖的软件包

### 3.2安装
+ 语法
    - yum install 包名 
+ 安装firefox
    - yum install firefox

### 3.3查询
+ 语法       
    - yum list|grep xxx
+ 查询yum安装的火狐
    - yum list|grep firefox

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787366225370-dcb67356-401c-419c-8607-3ee17dd4f145.png" width="750.0952380952381" alt="" title="" crop="0,0,1,1" id="u75cc1b66" class="ne-image">

### 3.4卸载
+ 语法
    - yum remove 软件包

# 七.linux软件下载
## 1.MySQL8.0安装
+ 下载MySQL安装包
+ rz上传安装包

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787390707785-0c6701a4-89a9-4600-94d6-88b7fadb8a0f.png" width="658.6666666666666" alt="" title="" crop="0,0,1,1" id="u92c0b42e" class="ne-image">

+ 安装xz工具
    - yum install xz
+ 解压xz压缩包
    - xz mysql 文件名.xz

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787391096142-34b42236-9457-47f8-8e9a-087720519d6e.png" width="456" alt="" title="" crop="0,0,1,1" id="u73081470" class="ne-image">

+ 解压tar压缩包
    - tar -xvf  mysql 文件名.tar

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787391251616-b52afc19-20b7-49eb-b014-aecaa955c901.png" width="708.5714285714286" alt="" title="" crop="0,0,1,1" id="ua094f7e7" class="ne-image">

+ 重命名mysql为mysql8.0
    - mv 原mysql名称 新mysql名称

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787391411387-60ff65ac-5ca8-482d-bcd3-7a1feb200da2.png" width="696" alt="" title="" crop="0,0,1,1" id="u4d886968" class="ne-image">

+ mysql不建议用root用户启动，所以要新建一个用户来启动
    - 新建mysql用户
        * useradd mysql

# 八.shell学习
## 1.shell概述
+ **shell**是一个命令行解释器，用于**接收用户命令**，调度操作系统内核，同时还是一个**脚本程序设计语言**。

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787559454352-cbd90667-f668-48a2-82ed-30fe1f87dc59.png" width="291.04761904761904" alt="" title="" crop="0,0,1,1" id="u62404b21" class="ne-image">

+ shell功能特点：
    - 易编写
    - 易调试
    - 高灵活性

## 2.linux提供的shell解析器
+ 解析器
    - cat /etc/shells

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787559705854-85c6f56b-9adc-4e80-b1f0-2556a5e77562.png" width="337.5238095238095" alt="" title="" crop="0,0,1,1" id="ub251719f" class="ne-image">

+ 分类
    - sh
    - bash
+ sh和bash的关系
    - sh和bash都是linux系统shell的一种，其中bash命令是sh命令的超集，大多数sh脚本都可以在bash下运行
+ rockey默认的shell
    - echo $SHELL

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787560615482-628e4f0d-3a7e-4c94-9d93-dbbc3bfda916.png" width="328.3809523809524" alt="" title="" crop="0,0,1,1" id="u9a53d89a" class="ne-image">

## 3.shell脚本快速入门
### 1.脚本格式
+ 指定解析器：必须以#!/bin/bash开头
    - #!/bin/bash

### 2.第一个shell脚本
+ 需求：第一个shell脚本：HelloWorld.sh，打印HelloWorld Shell
+ 代码

```shell
#!/bin/bash
echo "HelloWorld shell"
```

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787562192319-84560345-fd79-46a7-b15a-63527897bcf0.png" width="378.2857142857143" alt="" title="" crop="0,0,1,1" id="u24e45dd2" class="ne-image">

### 3.常用运行方式
+ 目的是运行shell代码

#### 3.1以sh/bash运行
+ 绝对路径执行（从/ 目录往下执行）

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787562358643-54d664be-7ad4-4734-83f5-ba2f576603d4.png" width="505.14285714285717" alt="" title="" crop="0,0,1,1" id="ud2e21c01" class="ne-image">

+ 相对路径执行

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787562438544-d01d63a1-e420-49b2-9426-440b21d0f315.png" width="417.9047619047619" alt="" title="" crop="0,0,1,1" id="ub2d3f69d" class="ne-image">

#### 3.2赋予shell脚本可执行权限
+ 给脚本赋予可执行权限 +x
    - chmod +x HelloWorld.sh
    - 绿色是可执行文件

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787562743791-613d4811-7ff9-4b0d-ae16-086617268725.png" width="542.0952380952381" alt="" title="" crop="0,0,1,1" id="uccf72cb4" class="ne-image">

+ 直接运行脚本
    - 绝对路径

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787562881251-91724299-9f35-433a-b558-7881ebad6c8e.png" width="474.6666666666667" alt="" title="" crop="0,0,1,1" id="ub6918153" class="ne-image">

    - 相对路径

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787562907245-804805c3-3f45-46e1-85ac-fd410e8e0bfe.png" width="385.9047619047619" alt="" title="" crop="0,0,1,1" id="u7bb59eba" class="ne-image">

#### 3.3两种方式的区别
+ 第一种本质上是**bash解析器去完成我们脚本的执行**
+ 第二种，**脚本自己执行**，所以需要可执行权限

## 4.shell语法
### 1.变量
#### 1.1系统预定义变量
+ $HOME
+ $PWD
+ $SHELL
+ $USER

 <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787712210001-25c0377b-10cd-4174-b481-e8fb63897c8c.png" width="369.5238095238095" alt="" title="" crop="0,0,1,1" id="u4fdb4e7a" class="ne-image">

#### 1.2自定义变量
+ 定义变量语法
    - 变量名=变量值，注意：=号前后不能有空格
+ 定义变量age=18
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787712959311-3ac97fe4-ac0a-4ed8-8eb3-5a37344f8e64.png" width="343.23809523809524" alt="" title="" crop="0,0,1,1" id="uc346cb99" class="ne-image">
+ 撤销变量
    - unset 变量名
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787713037347-205432a9-e6f3-4ab3-a944-2618b0dfcbcf.png" width="334.0952380952381" alt="" title="" crop="0,0,1,1" id="udfe2ca02" class="ne-image">
+ 生命静态变量（一旦声明不可撤销）
    - readonly 变量名
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787713798116-6c9d29b8-97ea-4a4a-93c2-aa6d7db39d9d.png" width="409.5238095238095" alt="" title="" crop="0,0,1,1" id="u2117d866" class="ne-image">
+ 变量命名规则
    - 变量名称可以由字母，数字和下划线组成，但是不能以数字开头，环境变量名建议大写
    - 等号两侧不能有空格
    - 变量的值如果有空格，需要使用双引号或单引号括起来

#### 1.3特殊变量
+ $n
    - n为数字，$0代表该脚本名称，$1-$9代表第一到第九个参数，十以上的参数，十以上的参数需要用大括号包含，如${20}
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787714668292-f618ff20-7c76-4b16-bb19-da36dde7e47e.png" width="521.5238095238095" alt="" title="" crop="0,0,1,1" id="ub9dd9c3c" class="ne-image">
+ $#
    - 获取所有输入参数个数，常用于循环，判断参数的个数是否正确以及加强脚本的健壮性 
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787714988708-6642054f-c24f-4794-b81c-0238e25c5c10.png" width="497.5238095238095" alt="" title="" crop="0,0,1,1" id="ubb1a8b08" class="ne-image">
+ $*
    - 代表命令行中的所有的参数，$*把所有的参数看成一个整体
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787715261795-4cb7b20c-6b5e-419d-9240-3a895521e070.png" width="472.3809523809524" alt="" title="" crop="0,0,1,1" id="ua9143d1f" class="ne-image">
+ $@
    - 代表命令行中所有的参数，不过$@把每个参数区分对待
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787715322970-a2a7827f-129b-406a-8d66-139cdbc4420e.png" width="472.3809523809524" alt="" title="" crop="0,0,1,1" id="ucfe6f318" class="ne-image">
+ $?
    - 最后一次执行的命令的返回状态。如果这个变量的值为0，证明上一个命令正确执行；如果这个变量的值为非0（具体是哪个数，由命令自己来决定），则证明上一个命令执行出错了

### 2.运算符
+ 语法
    - $((运算式))或$[运算式]
+ 计算(3+3)/2
    - $[(3+3)/2]
    - <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787716010586-e7745634-0d3d-47cb-943e-927518952828.png" width="403.8095238095238" alt="" title="" crop="0,0,1,1" id="ua896398f" class="ne-image">

### 3.条件语句
+ 语法
    - [ condition ] **注意：condition 前后要有空格**

#### 3.1两个整数之间比较
| condition | 说明 | 英语 |
| --- | --- | --- |
| -eq | 等于 | equal |
| -ne | 不等于 | not equal |
| -lt | 小于 | less than |
| -gt | 大于 | greater than |
| -le | 小于等于 | less equal |
| -ge | 大于等于 | greater equal |


#### 3.2.字符串比较
+ = 相等
+ != 不相等

#### 3.3文件权限判断
+ -r有读的权限
+ -w有写的权限
+ -x有执行的权限

#### 3.4文件类型判断
+ -e文件存在   吗， 吗
+ -f文件存在并且是一个常规的文件（file）
+ -d文件存在并且是一个目录（directory）

#### 3.5 && ||
+ &&满足前才执行
+ ||满足其一就行

### 4.流程控制语句
#### 4.1if判断
```shell
if [ 条件判断式 ]
then
    程序
fi
```

```shell
if [ 条件判断式 ]
then
    程序
elif [ 条件判断式 ]
then
    程序
else
    程序
fi
```

#### 4.2case语句
```shell
#!/bin/bash
case $1 in
        'java')
        echo "java 工程师"
;;
        'vue')
        echo "前端工程师"
;;
        *)
        echo "其他工种"
;;
esac
```

#### 4.3for循环
```shell
for 变量 in 值1 值2 值3
do 
    程序
done
```

#### 4.3while循环
```shell
while [ 条件判断式 ]
do 
    程序
done
```

### 5.函数
#### 5.1系统函数
+ basename
    -  拿到路径里的文件名，把前面的目录路径全部去掉  
+ dirname
    -  从完整路径中，提取【目录部分】，把文件名切掉  

##### 5.2自定义函数
```plain
function 函数名 {
    echo "第二种写法"
}

函数名
```

## 5.正则匹配
+ ^匹配一行的开头

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787822375241-474c06e8-4965-4910-a0d8-ce6514aed303.png" width="458.6666666666667" alt="" title="" crop="0,0,1,1" id="u0b6e2f9c" class="ne-image">

+ $匹配一行的结束

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787822444130-a6a4fde9-15f4-4fe2-9b5b-061f51291106.png" width="514.6666666666666" alt="" title="" crop="0,0,1,1" id="udfacee5c" class="ne-image">

+ **.**匹配一个任意字符

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787822532449-d96b342b-eeaf-4755-b97d-d81661bb8453.png" width="484.95238095238096" alt="" title="" crop="0,0,1,1" id="ubbe1679d" class="ne-image">

+ *不单独使用，他和上一个字符连用，表示匹配上一个字符0次或多次

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787822700089-c2c75e65-2138-487c-91f3-8d83c9f3eaea.png" width="480" alt="" title="" crop="0,0,1,1" id="u0a630ce1" class="ne-image">

+ [] 表示匹配某一个范围内的一个字符
    - [1,3]-------匹配1或者3
    - [0-9]-------匹配一个0-9的数字
    - [0-9]*------匹配任意长度的数字字符串
    - [a-z]--------匹配一个a-z之间的字符
    - [a-z]*-------匹配任意长度的字母字符串
    - [a-c,e-f]----匹配a-c或者e-f之间的任意字符
+ \表示转义

## 6.文本处理工具
### 1.概述
+ **awk**：文本分析工具，把文件逐行的读入，以空格为默认分隔符将每行切片，切开的部分在进行分析处理

### 2.语法
+ awk [参数] '/pattern1/{action1}...' filename

pattern:表示awk在数据中查找的内容，就是匹配模式

action：在找到匹配内容是所执行的一系列命令

参数

-F 指定输入文件分隔符

-V 赋值一个用户定义变量

+ 拷贝数据为了避免出现问题

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787830462415-9bf3623d-38b5-40b6-9664-d74e48ee2d41.png" width="441.14285714285717" alt="" title="" crop="0,0,1,1" id="uca9a09d4" class="ne-image">

+ 查看以root开头的数据的第二列的数据

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787830722525-14d79505-342d-447b-aa71-cd2f40ca06a0.png" width="558.0952380952381" alt="" title="" crop="0,0,1,1" id="u08ecf400" class="ne-image">

+ 查看以root开头的数据的第二列和第五列的数据

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787830814629-14aa69c0-6617-41aa-8a17-fdc64e60ef41.png" width="606.8571428571429" alt="" title="" crop="0,0,1,1" id="ub897f453" class="ne-image">

+ 找到passwd中第一列的值

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787831097961-33570156-8e99-4e25-9c2b-9d4458a935c6.png" width="535.2380952380952" alt="" title="" crop="0,0,1,1" id="ue729ea23" class="ne-image">

### 3.awk的内置变量
+ FILENAME文件名
+ NR已读的记录数（行号）
+ NF浏览记录的域的个数（切割后，列的个数）
+ 需求
    - 统计passwd每行行号

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787831453031-d0cd8c48-0acd-4790-a712-b9b68599b381.png" width="610.6666666666666" alt="" title="" crop="0,0,1,1" id="u5bc3d31f" class="ne-image">

    - 查找ip地址

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787831888652-0ae0ce9b-97b9-4756-9830-1893a623946b.png" width="624" alt="" title="" crop="0,0,1,1" id="u730dadd1" class="ne-image">

# 九.任务布置
+ 对于vim/vi的正常使用要会
+ 查看日志
+ 文件目录指令
+ 查找路径指令
+ 压缩和解压
+ 文件权限指令
+ 磁盘查看
+ 查看进程
+ 开放端口信息
+ 检查网络是否通
+ 环境配置
