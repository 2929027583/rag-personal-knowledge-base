# 第一讲
# 一.工作区，工作簿，工作表的联系
## <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">1.工作表是什么？</font>
## **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">工作表 = Excel 里你真正用来填数据的那张 “表格纸”</font>**
## <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">就是你打开 Excel 后，看到的</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">由无数格子组成的页面</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">，底部有标签：</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">Sheet1</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">、</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">Sheet2</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">、</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">Sheet3</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">……</font>
---

## <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">2.三者关系（一次理清）</font>
## **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">工作簿（.xlsx 文件）</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">整个 Excel 文件，相当于</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">一个文件夹 / 一本本子</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">。</font>
## **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">工作表（Sheet）</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">本子里的</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">每一页纸</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">，用来写数据、做表格。一个工作簿里可以有很多张工作表。</font>
## **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">单元格</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">工作表上的</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">每一个小格子</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">（A1、B2 这种）。</font>
---

## <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">3.举个超通俗的例子</font>
## **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">工作簿 = 一本笔记本</font>**
## **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">工作表 = 笔记本里的每一页</font>**
## **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">单元格 = 每页纸上的格子</font>**
## <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">你在</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">一页纸上写字</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"> → 操作</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">工作表</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">你把</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">整本书保存</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"> → 保存</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">工作簿</font>**
---

## <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">4.简单总结</font>
## <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">工作表 = 你填表的那张</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">页面</font>**
## <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">工作簿 = 包含很多工作表的</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">整个文件</font>**
## **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"> Excel 里的工作簿文件是存数据的实体文件，工作区文件是记录多工作簿布局的 “快捷方式”  </font>**
## **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"></font>**
# <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">二.excel操作技巧</font>
## **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">1.快速定位：选中一个单元格时，将鼠标放在边框的四个边时，出现四个箭头的标志双击一下可以快速定位到四个方向的最远处。</font>**
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774705553849-1b157a19-785f-4aa1-810b-af68303a3d6c.png" width="432" alt="" title="" crop="0,0,1,1" id="ua83667ea" class="ne-image">

## 2.冻结窗格：选中第几行点击冻结窗格就可以让这行上面的所有行列冻结锁定，当选中几行几列的单元格时点击冻结窗格可以使这个单元格的上方和左侧被冻结。


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774787783133-cd3b2dbd-4b74-4913-988d-450cbde52acf.png" width="533.6666870117188" alt="" title="" crop="0,0,1,1" id="uc83fee81" class="ne-image">

## 3.填充柄的使用：选中一个单元格后，将鼠标拖至边界出现黑色填充的十字架图案后右键拖拽可以自定义填充，有复制，序列等方式


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774789666283-f9f670ec-7de9-48b3-82f9-e525b3db98fc.png" width="293.66668701171875" alt="" title="" crop="0,0,1,1" id="uf4965dc6" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774789826233-02a70a0a-c2a1-4944-b625-e27e6d87a992.png" width="259.66668701171875" alt="" title="" crop="0,0,1,1" id="uac59d9bd" class="ne-image">



## 4.选中大范围的区域:选中2到900行的所有区域


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774789738205-b45e19f2-0774-48ed-a2ba-15372bc8b3ae.png" width="504.66668701171875" alt="" title="" crop="0,0,1,1" id="u3375f5ca" class="ne-image">

## 5.快速删除多张工作表：选中一张工作表，按住ctrl,在选择其他表
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774790330149-0f22d16f-08ed-4a21-8c3f-6f48a95964ac.png" width="396" alt="" title="" crop="0,0,1,1" id="ue3f43e1c" class="ne-image">

## 6.选中一列，鼠标放在这个位置双击将这列的单元格宽度设为内容宽度


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774791231161-32d9dafe-465a-4179-b86e-3b890fab5f5e.png" width="491" alt="" title="" crop="0,0,1,1" id="u2fb84727" class="ne-image">

## 7.更换两列位置：鼠标放到这个位置，按住shift拖拽到想要更换的列


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774791509982-3f1bde1f-9d4f-4572-8da4-ca87f1a5a8c5.png" width="394.66668701171875" alt="" title="" crop="0,0,1,1" id="ua7a7a3ba" class="ne-image">

# 第二讲
# 一.单元格格式设置
## 1.使用单元格格式工具美化表格
### 将多个单元格进行合并<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774960109819-67082d24-c6cd-45b6-b4d3-8c2f07626cf7.png" width="666" alt="" title="" crop="0,0,1,1" id="u1bb445dd" class="ne-image">
### 设置单元格格式
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774960454601-f0652781-4299-4b2c-8b97-8b86725ca766.png" width="401.66668701171875" alt="" title="" crop="0,0,1,1" id="uc11dd7a5" class="ne-image">

### 单元格格式互换
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774960626301-10673d50-e5d5-46f5-b181-138f1d859182.png" width="449.3333740234375" alt="" title="" crop="0,0,1,1" id="u3d2d5a9b" class="ne-image">

### 边框调整


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1774960668697-cecc91e6-8ac3-4714-b15f-57da699212c4.png" width="447.66668701171875" alt="" title="" crop="0,0,1,1" id="u8b829321" class="ne-image">

### 
# 第三讲
## 一.查找与替换
### 1.按值查找
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775042652697-867570bc-04e8-4b4e-adbb-c6c44033753b.png" width="394.3333435058594" alt="" title="" crop="0,0,1,1" id="u6e150696" class="ne-image">



### 2按格式查找
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775043124435-8b675631-8757-4774-b3d9-d7c0c8a74287.png" width="354" alt="" title="" crop="0,0,1,1" id="u2f2a0839" class="ne-image">

### 3.是否开启单元格匹配
### 4.模糊查找 认识通配符 ？* ~
1.将姓张的员工都该为经理的亲戚

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775043384238-789793b0-4a8e-471c-8d45-5bb2334082be.png" width="417.3333740234375" alt="" title="" crop="0,0,1,1" id="u7d569b4e" class="ne-image">

2.将姓张并且名字为两个字的员工都改为经理的亲戚

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775043539950-58c5d3db-2cf3-40f1-80ec-f5acbdbf1e7b.png" width="367.66668701171875" alt="" title="" crop="0,0,1,1" id="ud16fa6e6" class="ne-image">

3.让带有通配符的名字改为想要的名字 例如将张*改为经理的亲戚

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775043716179-dc19da7e-e9e1-4e51-a752-04ccce1ee17a.png" width="412.3333435058594" alt="" title="" crop="0,0,1,1" id="uf2d360a5" class="ne-image">

## 二.定位工具
### 1.通过名称框定位单元格及区域位置
：代表到达

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775045026666-3793ba14-6a78-4c66-b74c-b4485c579281.png" width="282.6666666666667" alt="" title="" crop="0,0,1,1" id="u3ee34fd2" class="ne-image">

### 2.定义名称
给常用的区域起名方便查找

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775045308094-9f978975-5845-48f2-9aef-13ea3dded239.png" width="241.33334350585938" alt="" title="" crop="0,0,1,1" id="u507877de" class="ne-image">

### 3.使用"定位条件"解决以下问题
#### a.为有注释的单元格设置红色填充物
查找->定位条件->注释->点颜料桶

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775046669852-6976855c-9878-4809-b393-17b594c2f4b0.png" width="246" alt="" title="" crop="0,0,1,1" id="uac429013" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775046654090-b8488cf6-be81-4ab2-8ad1-57f7454b020e.png" width="292" alt="" title="" crop="0,0,1,1" id="ud54feb39" class="ne-image">

#### b.为有公式的单元格设置红色填充物
查找->定位条件->公式->点颜料桶

#### c.填充解除单元格合并后遗留的空白单元格
先取消合并单元格，然后查找->空值->=加上箭头->ctrl +回车

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775048433470-754e5cc8-5a5d-4864-a06a-54c1b93f6d44.png" width="361.66668701171875" alt="" title="" crop="0,0,1,1" id="u52770b88" class="ne-image">

#### d.批量删除图片
定位->对象->删除

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775048602127-27d54348-36ef-4141-bea3-f80b690ec085.png" width="362" alt="" title="" crop="0,0,1,1" id="ub885f575" class="ne-image">

# 第四讲
## 一.排序
### 1.简单排序


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775478237418-ff656a0d-3a86-4cfc-8f7c-6dccdbc90bea.png" width="202" alt="" title="" crop="0,0,1,1" id="u7710ae32" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775478253881-f1bd4775-7b6a-4865-8bab-112f777ce6ee.png" width="113" alt="" title="" crop="0,0,1,1" id="u591965ed" class="ne-image">



### 2.多条件排序
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775478547037-f1023386-05b2-487e-b850-7818233909c9.png" width="377.66668701171875" alt="" title="" crop="0,0,1,1" id="u34cd236b" class="ne-image">

### 3.2003版本时超过三个排序条件时如何处理
先排次要关键字，再排主要关键字，

### 4.按颜色排序


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775479904111-d0e9e41a-8e8e-44c5-b6fe-f968e3c13d60.png" width="324.66668701171875" alt="" title="" crop="0,0,1,1" id="ufb502f51" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775479904214-aba00281-6b8d-4d94-b0c5-a04642dc2b0a.png" width="339.66668701171875" alt="" title="" crop="0,0,1,1" id="uaf9b0ecf" class="ne-image">

### 5.自定义排序次序


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775479944747-466f80be-d703-46a4-92c2-b695884155c0.png" width="498.66668701171875" alt="" title="" crop="0,0,1,1" id="u702457da" class="ne-image">

### 6.利用排序插入行
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775480302690-facf990e-d645-4090-9ff2-80f13301302c.png" width="589.6666870117188" alt="" title="" crop="0,0,1,1" id="u8ba6e17b" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775480253378-388764ff-b985-4a69-a6b1-8e8ff7bd9898.png" width="550.6666870117188" alt="" title="" crop="0,0,1,1" id="uca2f0e45" class="ne-image">

## 二.筛选
### 1.使用筛选
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775483429552-ae838819-edbd-4908-a891-d3b86c1dc116.png" width="394.66668701171875" alt="" title="" crop="0,0,1,1" id="u9172bf4e" class="ne-image">



### 2.在筛选中使用多个条件
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775483475710-62bd3c9d-0a2f-4bc4-9f75-ea9d06c7e59b.png" width="375.66668701171875" alt="" title="" crop="0,0,1,1" id="u459b07b1" class="ne-image">

### 3.高级筛选
条件区域表示且的意思

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775483007825-4954fe8c-51e8-4357-ae54-a03e3e00d27d.png" width="448" alt="" title="" crop="0,0,1,1" id="u05734acb" class="ne-image">

条件区域表示或的意思



<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775483128919-9908883a-7e47-4da7-b4de-62a9237a7b58.png" width="419" alt="" title="" crop="0,0,1,1" id="u7249b2a1" class="ne-image">

# 第五讲
## 一.分类汇总工具
### 1.认识分类汇总
### 2.使用分类汇总前先排序
先可以升序或者降序

### 3.分类汇总的嵌套
排序完成之后，先按所属区域分类汇总，然后按产品类别分类汇总

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775561773007-17c93e15-dcc6-466f-befe-b057a29fe227.png" width="249.66668701171875" alt="" title="" crop="0,0,1,1" id="uf263d4df" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775561753072-0b5dca90-7eac-4202-99e4-f395f137c466.png" width="235" alt="" title="" crop="0,0,1,1" id="u43924e32" class="ne-image">



<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775561926728-465cace3-e9ba-4ad2-8611-0da066d3e59d.png" width="451.66668701171875" alt="" title="" crop="0,0,1,1" id="u9a67e40b" class="ne-image">



### 4.复制分类汇总的结果区域
选中区域在开始菜单中点击查找与选择，点击定位条件选则可见单元格，即可复制仅仅看见的区域

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775562119213-bd1c613e-ea22-4fd9-b919-93ac3ea94df3.png" width="474.66668701171875" alt="" title="" crop="0,0,1,1" id="u62ec7569" class="ne-image">

### 5.使用分类汇总批量合并内容相同的单元格
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775562987639-d68ab4ae-6f8e-4e52-8e31-30cd7be875da.png" width="245.33334350585938" alt="" title="" crop="0,0,1,1" id="u1786f3cd" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775563003243-8cbdaa1f-6f90-4ef9-854a-e7881625526a.png" width="279.66668701171875" alt="" title="" crop="0,0,1,1" id="uf010440a" class="ne-image">

## 二.设置数据验证


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775563441074-62bc0af1-68e8-4e58-8d73-56703607af68.png" width="480.66668701171875" alt="" title="" crop="0,0,1,1" id="udb26be4d" class="ne-image">

### 1.设置整数数据验证


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775563423315-658cb5c5-f630-4503-9ab1-3215be131b03.png" width="347.66668701171875" alt="" title="" crop="0,0,1,1" id="ufc6dad34" class="ne-image">

### 2.设置文本长度数据验证


<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775563470426-1d74cbe7-469f-4733-b492-cb69c37642c7.png" width="394.66668701171875" alt="" title="" crop="0,0,1,1" id="u8493f2ec" class="ne-image">

### 3.设置序列数据验证
来源中的逗号必须是英文逗号

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775563489059-7fdf5570-3bd0-4de7-b100-4139f562b5f0.png" width="338.66668701171875" alt="" title="" crop="0,0,1,1" id="u57de04f9" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775563489058-28d8583b-4488-4d61-ba4a-90a172b8a288.png" width="339.66668701171875" alt="" title="" crop="0,0,1,1" id="u176eb22e" class="ne-image">

### 4.数据验证的其他设置
#### a.输入法切换
#### <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775565108376-14ff55cd-55f3-48be-9d5e-e2c40f129e77.png" width="249.66668701171875" alt="" title="" crop="0,0,1,1" id="ucac008ff" class="ne-image">
b.**单元格信息**



c.**单元格信息保护**

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775565132590-f47bf32d-7b62-41f7-a2e5-138e44def7d9.png" width="350.66668701171875" alt="" title="" crop="0,0,1,1" id="u65914f29" class="ne-image">

# 第六讲
## 一.数据透析表
### 1.创建数据透析表
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775632758187-9234f81d-c9a1-4c0e-85b8-5f53c4cf0052.png" width="226.66668701171875" alt="" title="" crop="0,0,1,1" id="uaa9d7f73" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775632841771-b8d2cbf3-295a-4224-b96f-a827db14b105.png" width="448.66668701171875" alt="" title="" crop="0,0,1,1" id="ub04c6964" class="ne-image">

### 2.更改数据透析表汇总方式


### 3.数据透析表中的组合
将日期改为季度

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775633020596-e5e040d3-8867-4f79-86e8-04cce52b7fe6.png" width="300" alt="" title="" crop="0,0,1,1" id="u0424c50c" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775633043811-a21df2c2-522c-4d20-9355-5727fa65905e.png" width="275.66668701171875" alt="" title="" crop="0,0,1,1" id="u297eac50" class="ne-image">

### 4.汇总多列数据
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775632908409-1d790c7c-8196-41be-8e25-728887f95cb1.png" width="426.66668701171875" alt="" title="" crop="0,0,1,1" id="uc11c2592" class="ne-image">

### 5.在透析表中使用计算
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775633275752-f12e6b40-b103-4d12-8b9f-0c964920a1c5.png" width="258" alt="" title="" crop="0,0,1,1" id="u1a3d4dc0" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775633369084-2b1c9347-7ea6-41bb-973b-ee9f036e81ba.png" width="423.66668701171875" alt="" title="" crop="0,0,1,1" id="u38c78575" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775633294798-2748f6e6-6d26-4284-bf11-b1e8ddeb4c33.png" width="442.66668701171875" alt="" title="" crop="0,0,1,1" id="u4c675967" class="ne-image">

### 6.利用筛选字段自动创建工作表
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775634006089-840d0164-a88c-44ce-af5c-b971438411bb.png" width="290.66668701171875" alt="" title="" crop="0,0,1,1" id="uc4495412" class="ne-image">

# 第七讲
## 一.认识excel公式
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775634208532-02f17bc9-3082-4311-af2b-4ddc0b5f2720.png" width="437.66668701171875" alt="" title="" crop="0,0,1,1" id="ub76182ff" class="ne-image">

### 1.运算符
#### 算术运算符 + - * / & % ^
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775635009638-6436a1da-ccdb-41c2-a525-3fd62422d165.png" width="248.66668701171875" alt="" title="" crop="0,0,1,1" id="u039dc622" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775635026131-5320cba1-3cde-4fa8-bb78-ca81a594c01a.png" width="225.66668701171875" alt="" title="" crop="0,0,1,1" id="uada59ebd" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775635099461-2e7346c2-3e50-4df2-8629-7fbc88d63f80.png" width="224.66668701171875" alt="" title="" crop="0,0,1,1" id="ucdcc0e9f" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775635110649-69f01b4f-d52f-470d-9d6f-bbe53dd66510.png" width="273.66668701171875" alt="" title="" crop="0,0,1,1" id="u90393620" class="ne-image">

#### 比较运算符 = < > >= <= <>
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775635998758-911f80fe-acb0-46da-a40b-c216051dd6ec.png" width="450.66668701171875" alt="" title="" crop="0,0,1,1" id="ub1aabfca" class="ne-image">

### 2.公式中的比较判断
### 3.运算符优先级
### 4.单元格引用
绝对引用:必须$符号来锁定你想确定的值

相对引用:不需要使用$

### <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775637737127-3847072d-85da-475a-ae97-2cc14b9bdaec.png" width="1226" alt="" title="" crop="0,0,1,1" id="ubaadb387" class="ne-image">
## 二.认识函数
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775634261788-b9297920-e9df-4575-a9b6-243edddc83d6.png" width="404" alt="" title="" crop="0,0,1,1" id="u5775013b" class="ne-image">

### 1.如何使用函数
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775638456970-333fa826-053a-4a51-97ec-4d76bf9eee59.png" width="262.66668701171875" alt="" title="" crop="0,0,1,1" id="u229c2fd6" class="ne-image">

### 2.学习以下函数
sum average max min rank

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775638729933-8ec55fad-21a7-482c-a1f9-a1f0358aceab.png" width="599.3333740234375" alt="" title="排名次要锁定整体,参数有两个" crop="0,0,1,1" id="imWRu" class="ne-image">

### 3.利用定位工具选择输入公式的位置
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775639033783-4e0a15bf-caa6-4f00-bd22-33d702989a38.png" width="358.66668701171875" alt="" title="" crop="0,0,1,1" id="uec2aa4a3" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775639034059-69a2918d-124c-4c92-974f-308bf8906919.png" width="396.66668701171875" alt="" title="" crop="0,0,1,1" id="u4693ad85" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775639033635-cc1140de-521a-41ab-8866-f54c1399d30e.png" width="287.66668701171875" alt="" title="" crop="0,0,1,1" id="u93f1239d" class="ne-image">

先依旧定位空值,然后相对引用写公式

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775639315812-54016a2b-fcd1-4043-bcf1-0f2a52b995c3.png" width="1527" alt="" title="" crop="0,0,1,1" id="ud1e83f66" class="ne-image">

CTRL加回车 批量填充

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775639316106-0cf91e65-6939-4251-8c31-a362f89f476f.png" width="1510" alt="" title="" crop="0,0,1,1" id="uc1bd3067" class="ne-image">

# 第八讲.
## 一.使用if函数
### 1.if函数的基本用法
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775734566132-b4e0dd96-65df-4153-846f-432362e44f89.png" width="392" alt="" title="" crop="0,0,1,1" id="u0e0b70e8" class="ne-image">

### 2.if函数的嵌套
将专业改为字母代号

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775735482949-ddb3f116-cc8e-4fa0-9ad0-ad4eef339c99.png" width="683.6666870117188" alt="" title="" crop="0,0,1,1" id="u8cd0a9d5" class="ne-image">

本地学生原始分加30，本省加20，外省学生加10

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775735795398-70d2ec15-7543-42df-839b-608fee5b23a8.png" width="552.6666870117188" alt="" title="" crop="0,0,1,1" id="ue8f30456" class="ne-image">

### 3.如何尽量回避if函数的嵌套
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775738578165-e9644f9e-8b88-4be7-a43b-50d167d6a499.png" width="1916" alt="" title="" crop="0,0,1,1" id="u235f563d" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775738578060-cbe01989-2cea-403e-9f22-9024b5239e01.png" width="1731" alt="" title="" crop="0,0,1,1" id="udc33f905" class="ne-image">

### 4.用if函数处理运算错误 iserror函数
iserror判断表达式是否错误

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775738814357-3e461c94-bfe1-4cbc-a806-e7cf9364610a.png" width="546.6666870117188" alt="" title="" crop="0,0,1,1" id="ub42c2ec9" class="ne-image">

## 二.and函数与or函数
### 1.and函数：表示且的关系
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775739800252-2fab9db0-fcfd-44b5-a27f-21c38d5f7943.png" width="1792" alt="" title="" crop="0,0,1,1" id="uaec7810d" class="ne-image">

### 2.or函数 ：表示或的关系
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775739812268-01d55346-3ecd-48c8-b5f2-d108789c8ad9.png" width="1432" alt="" title="" crop="0,0,1,1" id="uba9590af" class="ne-image">

### 3.综合
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775739834841-caffd478-c96f-4e73-9b6f-667a2ec3d280.png" width="1063.3333333333333" alt="" title="" crop="0,0,1,1" id="ub4334160" class="ne-image">

# 第九讲
## 一.使用countif函数
+ **<font style="color:rgb(15, 17, 21);">COUNTIF = 数个数</font>**<font style="color:rgb(15, 17, 21);">  
</font><font style="color:rgb(15, 17, 21);">它在指定区域里，</font>**<font style="color:rgb(15, 17, 21);">数一数</font>**<font style="color:rgb(15, 17, 21);">有多少个单元格符合你给的条件。  
</font><font style="color:rgb(15, 17, 21);">👉</font><font style="color:rgb(15, 17, 21);"> 比如：统计“一班”有多少个学生，或者“大于60分”的分数有几个。</font>

### 1.count函数
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775787622344-8842f75f-e39c-4c4b-9b76-aab1c5109a21.png" width="284.66668701171875" alt="" title="" crop="0,0,1,1" id="u8fc448f1" class="ne-image">

### 2.countif函数语法
countif在一个给定的区域里，设一个条件进行计数，返回一个数值可以作为表达式

### <img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775787667330-d4a50d74-3a6b-4dff-a5d2-9369986a3247.png" width="602" alt="" title="" crop="0,0,1,1" id="u452b07fd" class="ne-image">
### 3.countif函数计算数值区间
因为>=60不是表达式，而是文本形式，所以需要加上引号

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775788564137-1b2dca44-87d2-4a92-b31a-21987f8da6f0.png" width="515.6666870117188" alt="" title="" crop="0,0,1,1" id="u11d7b627" class="ne-image">

### 4.countif函数超过15位子符的错误
因为countif只能识别15位，所以需要用连字符连上后三位才能判断出来想要的个数

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775788537972-673651d3-97fd-4eb8-850c-912967f7b853.png" width="595.6666870117188" alt="" title="" crop="0,0,1,1" id="u30e52782" class="ne-image">

## 二.常见应用实例
### 1.在数据区域中寻找重复数据
用文字检验是否体检使用countif函数和if函数组合

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775789026393-06c252dc-9a33-42cb-b3f4-348d0037316a.png" width="643.6666870117188" alt="" title="" crop="0,0,1,1" id="ueff22cee" class="ne-image">

用单元格填充色检验是否体检，使用countif函数就可以

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775789367812-8dcf0777-7e26-47d1-9580-02fa94a0cb54.png" width="624.6666870117188" alt="" title="" crop="0,0,1,1" id="u5d2d7169" class="ne-image">



<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775789532301-16e75647-0ae8-46f0-a37a-d7f27617ca72.png" width="540.6666870117188" alt="" title="" crop="0,0,1,1" id="u93bb3ec7" class="ne-image">

### 2.在数据验证中使用countif函数
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775790653200-4ddb2475-7ea9-46ed-8a3b-1e83ba1d772f.png" width="430.66668701171875" alt="" title="" crop="0,0,1,1" id="uf6d4d609" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775790652951-b1ad49bd-98f2-46c3-b229-af90223a9a95.png" width="425.66668701171875" alt="" title="" crop="0,0,1,1" id="u8de32dc7" class="ne-image">

### 3.在条件格式中使用countif函数
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775791047144-69fd29b3-383d-44ed-9834-d49468a6f85f.png" width="576.6666666666666" alt="" title="" crop="0,0,1,1" id="u480b17b5" class="ne-image">

## 三.2007及以上版本的countifs函数
多条件计数

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775791162044-ed0966e9-4b85-46b0-a7d9-4b4044b00054.png" width="1246.6666666666667" alt="" title="" crop="0,0,1,1" id="uaa99a68e" class="ne-image">

# 第十讲
| | | | | |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| 一、 | <font style="color:red;">使用Sumif函数</font> | | | |
| | | | | |
| | 1、Sumif函数语法 | | | |
| | | =sumif(range,criteria,[sum_range]) | | |
| | | | | |
| | 2、Sumif函数计算数值区间 | | | |
| | | | | |
| | 3、Sumif函数超过15位字符时的错误 | | | |
| | | | | |
| | 4、关于第三参数简写时的注意事项 | | | |
| | | | | |
| | 5、在多列中使用Sumif函数 | | | |
| | | | | |
| | 6、使用辅助列处理多条件的Sumif | | | |
| | | | | |
| | 7、Sumifs函数 | | | |
| | | | | |
| | 9、复习数据有效性 | | | |
| | | | | |
| | | | | |


# 一.使用sumif函数
+ **<font style="color:rgb(15, 17, 21);">SUMIF = 算总和</font>**<font style="color:rgb(15, 17, 21);">  
</font><font style="color:rgb(15, 17, 21);">它在指定区域里，找到符合条件的所有单元格，然后把</font>**<font style="color:rgb(15, 17, 21);">另一列里对应的数字加起来</font>**<font style="color:rgb(15, 17, 21);">。  
</font><font style="color:rgb(15, 17, 21);">👉</font><font style="color:rgb(15, 17, 21);"> 比如：把“一班”所有学生的语文成绩加在一起，或者把“大于60分”的分数加起来。</font>

## 1、Sumif函数语法
=sumif(range,criteria,[sum_range])（条件区域，条件，求和项）

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775912242341-223e2754-1454-42ef-9b01-ea09e243abd5.png" width="526.6666870117188" alt="" title="" crop="0,0,1,1" id="u70ef415e" class="ne-image">

## 2、Sumif函数计算数值区间
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775912329604-2aa4fd3a-7ad5-463d-a9af-69ef3e4b1fbc.png" width="357.3333740234375" alt="" title="" crop="0,0,1,1" id="u4982112d" class="ne-image">

## 3、Sumif函数超过15位字符时的错误
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775912632837-101edf60-d7fa-4edd-8b56-da67b846335e.png" width="502.66668701171875" alt="" title="" crop="0,0,1,1" id="u66451216" class="ne-image">

## 4、关于第三参数简写时的注意事项
这样算出的结果是错误的，会导致D1与F2对应，所以不要简写第三参数

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775913325150-c0c7a8e6-936f-4b3a-bce9-24a510e5664d.png" width="513.6666870117188" alt="" title="" crop="0,0,1,1" id="u1a144a08" class="ne-image">

## 5、在多列中使用Sumif函数
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775913959738-f502679d-5d80-4e44-a57f-87a42b542c3d.png" width="1318" alt="" title="" crop="0,0,1,1" id="uf80ab421" class="ne-image">

## 6、使用辅助列处理多条件的Sumif
先创建一个辅助列，将两个列合并，在进行sumif计算

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775913940538-69113716-ee38-4d75-a328-b8a5ffc349ce.png" width="1512" alt="" title="" crop="0,0,1,1" id="uef4086ff" class="ne-image">

## 7、Sumifs函数
sumifs(求和项,条件区域1,条件1,条件区域2,条件2,......)

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775914435073-1675647b-bcec-44e4-99f4-91be0b7397d5.png" width="641.6666870117188" alt="" title="" crop="0,0,1,1" id="u68b224ca" class="ne-image">

## 9、复习数据验证
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775916293437-0dcc7342-cecf-4aa0-98ea-989674134d7e.png" width="562.6666870117188" alt="" title="" crop="0,0,1,1" id="u0f25cbc0" class="ne-image">

# 第十一讲
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775971918683-4d414b43-febd-4cd7-970f-b51307782274.png" width="844.6666666666666" alt="" title="" crop="0,0,1,1" id="u428cd1fb" class="ne-image">

## 一.使用vlookup函数
### 1.vlookup函数语法  查找引用函数
VLOOKUP(lookup_value,table_array,col_index_num,[range_lookup])

**<font style="color:rgb(15, 17, 21);">=VLOOKUP(你要找什么， 去哪找， 回来时拿第几列的东西， 精确找还是近似找)</font>**

参数一：要找的目标人物，参数二：查找的区域，且必须使得查找区域的第一列为要找的目标人物，最后一列可以是目标人物的数据，也可以多选几列，参数三：目标人物的数据所在列 ，参数四：0代表精确查找，1代表模糊查找

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775972748301-fe5e2ac8-c26c-402d-b39a-e997c7fb0710.png" width="1002" alt="" title="" crop="0,0,1,1" id="u77f8c820" class="ne-image">

**跨表查询**

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775973489166-f79f3f52-b84b-4bed-b12a-a55955a4bd85.png" width="471.3333740234375" alt="" title="" crop="0,0,1,1" id="u7ab88770" class="ne-image">

### 2.vlookup中使用通配符
当查找目标为关键字(简化了名称)时，可能会查不到，发生#N/A的错误，这时候需要使用通配符

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775973881899-5f7b5703-539f-421f-8947-f9b4abd49481.png" width="358.66668701171875" alt="" title="" crop="0,0,1,1" id="u69ec9837" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775974018653-1745e74c-8fd7-4ba3-bda2-6d83d4aa4cd0.png" width="358.3333435058594" alt="" title="" crop="0,0,1,1" id="udac9e987" class="ne-image">

### 3.vlookup模糊查找
模糊查找适用于哪些区间范围内的查找，且查找的值一定是小于等于自己本身的

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775974600208-8616506c-3d02-40e4-bd85-b60fec6a4cd2.png" width="507.66668701171875" alt="" title="" crop="0,0,1,1" id="u7297a8f5" class="ne-image">

### 4.使用isna函数处理数字格式引起的错误
isna函数判断结果是否为#N/A错误

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775975547891-25df22d0-220b-4da4-992f-3b97a5e6444f.png" width="635.6666870117188" alt="" title="" crop="0,0,1,1" id="u5fbf88f5" class="ne-image">

### 5.hlookup函数
hlookup以行为区域来找目标数据,vlookup以列为区域来找目标数据

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775975712919-0523e091-4e15-42ca-b7ad-3531bfba4ac4.png" width="562.6666870117188" alt="" title="" crop="0,0,1,1" id="u8767cfcf" class="ne-image">

# 第十二讲
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775997207533-bbad0321-fa2e-4320-b4dc-3452c71d313e.png" width="514.3333740234375" alt="" title="" crop="0,0,1,1" id="uef88de3a" class="ne-image">

## 一.Match与Index函数
### 1.函数语法
<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1775998926388-78168b53-7b9e-43de-825e-2d103838cbbb.png" width="292" alt="" title="" crop="0,0,1,1" id="ueebbc04e" class="ne-image">

### 2.match+index与vlookup函数比较
+ **<font style="color:rgb(15, 17, 21);">VLOOKUP</font>**<font style="color:rgb(15, 17, 21);">：只能</font>**<font style="color:rgb(15, 17, 21);">从第一列向右查找</font>**<font style="color:rgb(15, 17, 21);">，返回右侧某列的值。</font>
+ **<font style="color:rgb(15, 17, 21);">INDEX+MATCH</font>**<font style="color:rgb(15, 17, 21);">：可以在</font>**<font style="color:rgb(15, 17, 21);">任意方向查找</font>**<font style="color:rgb(15, 17, 21);">（左、右、上、下），位置更自由。</font>

### 3.使用match与vlookup函数嵌套返回多列结果
**相对引用：向下拖拽行变化A1->A2->A3.....，向右拖拽列变化A1->B1->C1....**

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1776000550635-61f929f9-06e2-4447-8655-640facf3ffc2.png" width="1258" alt="" title="" crop="0,0,1,1" id="u1251a61d" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/66588345/1776002724752-51c2a1c2-5f0c-4727-bd1d-74a3b47cfd83.png" width="1619.3333333333333" alt="" title="" crop="0,0,1,1" id="u7cdbb39a" class="ne-image">

### 4.认识column函数
colunm()返回当前所在列的列数








