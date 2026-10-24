# 一.FastAPI基础入门
## 1.第一个FastAPI项目
### 为什么要创建虚拟环境
<font style="color:#DF2A3F;">隔离项目运行环境，避免依赖冲突，保持全局环境的干净和稳定</font>

### 怎么运行FastAPI项目
<font style="color:#DF2A3F;">run项目</font>

<font style="color:#DF2A3F;">uvicorn main:app --reload</font>

### 怎么访问FastAPI交互式文档
<font style="color:#DF2A3F;">127.0.0.1:8000/docs</font>

## 2.路由
路由就是**<font style="color:#DF2A3F;">URL地址</font>**和**<font style="color:#DF2A3F;">处理函数</font>**之间的映射关系，它决定了当用户访问某个特定网址时，服务器应该执行哪段代码来返回结果

**<font style="color:#DF2A3F;">FastAPI的路由定义基于Python的装饰器模式</font>**

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787194606155-cf72ca93-136d-42d6-9dcd-7d351e11dbc6.png" width="554.1333333333333" alt="" title="" crop="0,0,1,1" id="uda016653" class="ne-image">

练习：

需求：访问路径/user/hello，响应结果是{"msg":"我正在学习FastAPI......"}

## 3.参数简介和路径参数
### 路径参数
位置：URL路径的一部分<font style="color:#DF2A3F;">/book/{id}</font>

作用：指向唯一的，特定的资源

方法：<font style="color:#DF2A3F;">GET</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787214088702-fc42d1aa-64db-4de8-adb8-d40ad1d57c89.png" width="1014.4" alt="" title="" crop="0,0,1,1" id="u7798bbd8" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787214127435-1ed41d50-f1c5-40fd-9eed-3c7f48e07dd9.png" width="1240.5333333333333" alt="" title="" crop="0,0,1,1" id="u9b321312" class="ne-image">

**路径参数出现在什么位置？**

<font style="color:#DF2A3F;">U</font>**<font style="color:#DF2A3F;">RL路径的一部分   /book/{id}</font>**

### <font style="color:#000000;">路径参数Path类型注解</font>
**如何为路径参数添加类型注解？**

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787214046987-661908d4-e5e5-4f19-97f8-196281add519.png" width="1064.5333333333333" alt="" title="" crop="0,0,1,1" id="ua93261fb" class="ne-image">需求：定义两个接口，携带路径参数，并使用Path来实现类型注解

具体如下：

+ 接口1：以新闻分类id为参数设计URL，id范围为1-100
+ 接口2：以新闻分类名称为参数设计URL，分类名称长度为2-10

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787215418502-9e16c645-2a1c-4379-bae2-b433078ab1d3.png" width="1037.3333333333333" alt="" title="" crop="0,0,1,1" id="ud0a294fa" class="ne-image">

### 查询参数和query类型注解
**查询参数**

声明的参数不是路径参数时，路径操作函数会把该参数自动解释为查询参数

位置：URL<font style="color:#DF2A3F;">？k1=v1&k2=v2</font>

作用：对资源集合进行过滤，排序，分页等操作

方法：<font style="color:#DF2A3F;">GET</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787279876051-87908ff7-95ec-4865-80d4-e5ed627d0a39.png" width="807.4666666666667" alt="" title="" crop="0,0,1,1" id="u6897ccb5" class="ne-image">

### 请求体参数
位置：HTTP请求的<font style="color:#DF2A3F;">消息体（body）</font>中

作用：创建，更新资源携带大量数据，如json

方法：<font style="color:#DF2A3F;">POST，PUT</font>等

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787280680923-a220c8b4-ee7a-4250-a3db-f367ae4b8f17.png" width="738.1333333333333" alt="" title="" crop="0,0,1,1" id="ud52e5cf8" class="ne-image">

**需求:设计接口新增图书，图书信息包含：书名，作者，出版社，售价**

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787281300709-16f90489-e56f-43e3-994e-9bbe39e762e9.png" width="523.2" alt="" title="" crop="0,0,1,1" id="u97f9c1d1" class="ne-image">

### 请求体参数和Field类型注解
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787285964761-a4e2e9cc-9875-4e23-b0e5-12e573904d0d.png" width="541.3333333333334" alt="" title="" crop="0,0,1,1" id="u1350cf70" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787285920447-9c1e090b-1627-422d-9e21-082296f6c5e2.png" width="1081.6" alt="" title="" crop="0,0,1,1" id="u55e62d01" class="ne-image">

## 4.响应类型
**<font style="color:#DF2A3F;">默认情况下</font>**，FastAPI会**<font style="color:#DF2A3F;">自动</font>**将路径操作返回的**<font style="color:#DF2A3F;">python对象</font>**（字典，列表，pydantic模型等），经由jsonable_encoder转换为**<font style="color:#DF2A3F;">JSON</font>**兼容格式，并包装为JSONResponse返回。这省去了手动序列化的步骤，让开发者能更专注于业务逻辑。**<font style="color:#DF2A3F;">如果需要返回非JSON数据（如HTML，文件流），FastAPI提供了丰富的响应类型来返回不同数据。</font>**

### 响应HTML格式
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787639192988-1a27c650-aadd-4f0d-b5b6-a337449c90c6.png" width="406.85714285714283" alt="" title="" crop="0,0,1,1" id="u49ccfe8f" class="ne-image">

### 响应文件格式
**<font style="color:#DF2A3F;">FileResponse</font>**是FastAPI提供的专门用于高效返回文件内容（如图片，PDF，Excel，音视频等）的响应类。它能够智能处理文件路径，媒体类型推断，范围请求和缓存头部，是服务静态的推荐方式。

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787639891697-f8ac2a2b-08eb-4c78-ab32-9df43c77e6e9.png" width="514.2857142857143" alt="" title="" crop="0,0,1,1" id="ub513f95b" class="ne-image">

### 自定义响应数据格式
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787640853041-c007ab99-46f9-405d-9675-3d78ff64539b.png" width="478.4761904761905" alt="" title="" crop="0,0,1,1" id="uf45d8541" class="ne-image">

### 异常响应处理
对于客户端引发的错误（4xx，如资源未找到，认证失败），应使用fastapi.HTTPException来中断正常处理流程，并返回标准错误响应。

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1787641649620-598ceac1-e3a1-49fa-ba5e-3bb4bed42522.png" width="551.6190476190476" alt="" title="" crop="0,0,1,1" id="ua0993ae4" class="ne-image">

# 二.FastAPI进阶
## 1.中间件
中间件是一个在每次请求进入FastAPI应用时都会被执行的函数。它在请求到达实际的路径操作（路由处理函数）之前运行，并且在响应返回给客户端之前在运行一次。

+ 中间件作用是什么？

<font style="color:#DF2A3F;">为每个请求添加统一的处理逻辑（记录日志，身份认证，跨域，设置响应头，性能监控等）</font>

+ 中间件怎么定义？

函数的顶部使用装饰器<font style="color:#DF2A3F;">@app.middleware("http")</font>

+ 多个中间件的执行顺序

<font style="color:#DF2A3F;">自下而上</font>

## 2.依赖注入
+ FastAPI中，依赖注入系统有什么用？

<font style="color:#DF2A3F;">抽取可复用的组件，实现代码复用，解耦且可轻松替换依赖项进行测试</font>

+ 怎么使用依赖注入系统？

<font style="color:#DF2A3F;">创建依赖项----导入depends----声明依赖项</font>

## <font style="color:#000000;">3.ORM</font>
### 3.1ORM简介和安装
ORM（Object-RelationalMapping,对象关系映射）是一种编程技术，用于在<font style="color:#DF2A3F;">面向对象编程语言和关系型数据库之间建立映射</font>。它允许开发者通过<font style="color:#DF2A3F;">操作对象的方式</font>与数据库进行交互，而无需直接编写复杂的SQL语句

优势

+ 减少复杂的sql代码
+ 代码更简洁易懂
+ 自动处理数据库连接和事务
+ 自动防止sql注入攻击

### 3.2ORM建表



