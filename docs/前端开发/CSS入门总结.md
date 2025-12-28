## CSS基础概念
### 什么是CSS？
+ **CSS = Cascading Style Sheets（层叠样式表）**
+ CSS描述HTML/XML文档的样式和外观
+ 目标：实现**内容与表现分离**

### 表现与内容分离的重要性
**传统HTML方式的问题：**

```html
<!-- 内容和表现混合 - 不推荐 -->
<h1 align="center">
  <font size="7" face="宋体" color="#800080">
    <strong>一个紫色的标题</strong>
  </font>
</h1>
```

**CSS方式 - 推荐：**

```html
<!-- HTML：只负责内容 -->
<h1>一个紫色的标题</h1>

<!-- CSS：只负责样式 -->
<style>
h1 {
  font-family: "宋体";
  font-size: 3em;
  font-weight: bold;
  color: #800080;
  text-align: center;
}
</style>
```

**分离的优势：**

+ 代码重用性好，提高开发效率
+ 网站代码可维护性高
+ 减少代码量，降低服务器负担
+ 加快浏览器解析速度

### CSS版本
+ **CSS1（基础版）**：HTML文档样式表
+ **CSS2（增强版）**：支持XML、定位功能
+ **CSS3（现代版）**：模块化设计，向后兼容

## CSS语法基础
### CSS规则结构
```css
选择器 {
  属性: 值;
  属性: 值;
}
```

**示例：**

```css
h1 {
  color: purple;
  font-size: 3em;
}
```

### CSS应用方式
#### 外链式（推荐）
```html
<link rel="stylesheet" type="text/css" href="styles.css" />
```

+ 样式写在独立.css文件中
+ 可被多个页面共用

#### 内嵌式
```html
<head>
  <style type="text/css">
    h1 { font-size: 3em; }
  </style>
</head>
```

+ 样式写在`<style>`标签中
+ 只对当前文档有效

#### 内联式
```html
<p style="color: red;">text</p>
```

+ 直接写在元素的style属性中

### 样式表层叠优先级（从高到低）
1. **用户样式表**
2. **内联样式表**
3. **内嵌样式表**
4. **外链样式表**
5. **浏览器样式表**

### CSS注释
```css
/* 这是一个注释 */
p {
  color: black; /* 这是另一个注释 */
}
```

## CSS基础属性
### 颜色和背景
#### 颜色表示方法
```css
/* 命名颜色 */
h1 { color: red; }

/* RGB数值 */
h1 { color: rgb(132,20,180); }

/* RGB百分比 */
h1 { color: rgb(12%,200,50%); }

/* 十六进制 */
h1 { color: #FF0000; }
h1 { color: #F00; }

/* CSS3新增 */
p { color: rgba(0,0,255,0.5); } /* 半透明 */
p { color: hsl(120, 100%, 75%); } /* HSL */
```

#### 背景属性
```css
background-color: #ccc;           /* 背景色 */
background-image: url(bg.jpg);    /* 背景图 */
background-repeat: no-repeat;     /* 重复方式 */
background-attachment: fixed;     /* 滚动方式 */
background-position: center;      /* 位置 */

/* 简写属性 */
background: white url(bg.gif) no-repeat fixed top right;
```

**图片使用原则：**

+ **内容相关图片**：放在HTML中用`<img>`标签
+ **装饰性图片**：放在CSS中用`background-image`

### 字体属性
#### 字体族（font-family）
```css
/* 具体字体名 */
font-family: "Times New Roman", Arial;

/* 通用字体族 */
font-family: serif;        /* 有衬线 */
font-family: sans-serif;   /* 无衬线 */
font-family: monospace;    /* 等宽字体 */
font-family: cursive;      /* 草书体 */
font-family: fantasy;      /* 幻想体 */

/* 推荐写法：具体字体 + 通用字体族 */
font-family: Tahoma, SimSun, Sans-Serif;
```

#### CSS3 @font-face 自定义字体
```css
@font-face {
  font-family: "French Script MT";
  src: url(frenchs4.eot);
}
p { font-family: "French Script MT"; }
```

#### 字体尺寸（font-size）
```css
/* 绝对单位 */
font-size: 12pt;    /* 点 */
font-size: 16px;    /* 像素 */

/* 相对单位 */
font-size: 1.2em;   /* 相对父元素 */
font-size: 80%;     /* 百分比 */

/* 关键字 */
font-size: small;   /* xx-small 到 xx-large */
font-size: larger;  /* 相对关键字 */
```

#### 其他字体属性
```css
font-weight: bold;           /* 字体加粗 */
font-style: italic;          /* 字体风格 */
font-variant: small-caps;    /* 字体变种 */

/* 字体简写属性 */
font: italic small-caps bold 12px/18px Arial;
```

### 文本属性
```css
letter-spacing: 2px;         /* 字母间距 */
word-spacing: 5px;           /* 单词间距 */
line-height: 1.5;            /* 行高 */
text-align: center;          /* 文本对齐 */
text-indent: 2em;            /* 文本缩进 */

/* 文本装饰 */
text-decoration: underline;   /* 下划线 */
text-decoration: line-through; /* 删除线 */
text-decoration: none;        /* 取消装饰（常用于链接） */

/* 文本转换 */
text-transform: uppercase;    /* 大写 */
text-transform: lowercase;    /* 小写 */
text-transform: capitalize;   /* 首字母大写 */
```

### 列表属性
```css
/* 列表项标记类型 */
list-style-type: decimal;        /* 数字 */
list-style-type: lower-roman;    /* 小写罗马数字 */
list-style-type: none;           /* 无标记 */

/* 自定义列表图标 */
list-style-image: url(arrow.gif);

/* 标记位置 */
list-style-position: inside;

/* 简写 */
list-style: square inside url(arrow.gif);
```

## CSS选择器
### 基础选择器
#### 元素选择器
```css
h1 { color: blue; }        /* 选择所有h1元素 */
* { margin: 0; }           /* 全局选择器 */
```

#### 类选择器
```css
.highlight { color: yellow; }
span.highlight { font-style: italic; }  /* 特定元素的类 */

/* 联合类选择器 */
.red { color: red; }
.alert { font-weight: bold; }
.red.alert { background: black; }  /* 同时有两个类 */
```

```html
<p class="highlight">高亮文本</p>
<p class="red alert">红色警告</p>
```

#### ID选择器
```css
#special { color: purple; background: black; }
```

```html
<h1 id="special">特殊标题</h1>
```

**Class vs ID：**

+ **Class**：可用于多个元素，表示同一类
+ **ID**：只能用于一个元素，表示唯一标识

### 伪类选择器
```css
/* 链接状态 */
a:link { color: red; }        /* 未访问链接 */
a:visited { color: green; }   /* 已访问链接 */
a:hover { color: black; }     /* 鼠标悬停 */
a:active { color: yellow; }   /* 点击时 */

/* 表单焦点 */
input:focus { border: 2px solid blue; }
```

顺序很重要：link → visited → hover → active

### 伪元素选择器
```css
p:first-letter { font-size: 200%; }     /* 首字母 */
p:first-line { color: purple; }         /* 首行 */
p:before { content: "前缀"; }           /* 元素前 */
p:after { content: "后缀"; }            /* 元素后 */
```

### 关系选择器
#### 后代选择器
```css
li a { text-decoration: none; }  /* li内的所有a元素 */
```

#### 子代选择器
```css
#nav > li { font-size: 14px; }   /* #nav的直接子li元素 */
```

#### 相邻兄弟选择器
```css
h1 + p { margin-top: 50px; }     /* 紧跟h1后的p元素 */
```

#### 选择器组合
```css
/* 复杂选择器组合 */
html > body table + ul { margin-top: 20px; }

/* 选择器分组 */
h1, h2, h3 { color: blue; }
```

## CSS布局基础
### 盒模型（Box Model）
#### 盒模型组成
从内到外：**内容 → 内边距(padding) → 边框(border) → 外边距(margin)**

```css
.box {
  width: 200px;           /* 内容宽度 */
  height: 100px;          /* 内容高度 */
  padding: 10px;          /* 内边距 */
  border: 1px solid #000; /* 边框 */
  margin: 20px;           /* 外边距 */
}
```

#### 简写属性规则
```css
/* 四个值：上 右 下 左（顺时针） */
margin: 20px 10px 20px 10px;

/* 三个值：上 左右 下 */
margin: 20px 10px 10px;

/* 两个值：上下 左右 */
margin: 20px 10px;

/* 一个值：四个方向相同 */
margin: 10px;
```

#### 不继承的属性
以下属性不会被子元素继承：

+ background（背景）
+ margin（外边距）
+ padding（内边距）
+ border（边框）
+ width（宽度）
+ height（高度）

### 尺寸属性
```css
width: 300px;            /* 宽度 */
height: 200px;           /* 高度 */
min-width: 200px;        /* 最小宽度 */
max-width: 800px;        /* 最大宽度 */
min-height: 100px;       /* 最小高度 */
max-height: 500px;       /* 最大高度 */
line-height: 1.5;        /* 行高 */
```

### 定位属性（Position）
#### 四种定位方式
**static（静态定位 - 默认）**

```css
position: static;  /* 按正常文档流排列 */
```

**relative（相对定位）**

```css
position: relative;
top: 20px;
left: 20px;
```

+ 相对于元素原始位置移动
+ **原来的空间仍会保留**

**absolute（绝对定位）**

```css
position: absolute;
top: 100px;
left: 100px;
```

+ 相对于**最近的已定位祖先元素**
+ **脱离文档流**

**fixed（固定定位）**

```css
position: fixed;
top: 200px;
left: 200px;
```

+ 相对于**浏览器窗口**定位
+ 不随页面滚动

#### 辅助属性
```css
top: 50px;           /* 距离顶部 */
bottom: 50px;        /* 距离底部 */
left: 50px;          /* 距离左侧 */
right: 50px;         /* 距离右侧 */
z-index: 10;         /* 层叠顺序 */
```

### 布局属性
#### float（浮动）
```css
float: left;     /* 向左浮动 */
float: right;    /* 向右浮动 */
float: none;     /* 不浮动 */
```

+ 元素脱离文档流，向指定方向移动
+ 常用于实现文字环绕效果

#### clear（清除浮动）
```css
clear: left;     /* 左侧不允许浮动元素 */
clear: right;    /* 右侧不允许浮动元素 */
clear: both;     /* 两侧都不允许浮动元素 */
```

### 显示属性
#### display
```css
display: block;      /* 块级元素 */
display: inline;     /* 内联元素 */
display: none;       /* 完全隐藏 */
```

#### visibility
```css
visibility: visible;   /* 可见 */
visibility: hidden;    /* 隐藏但保留空间 */
```

**区别：**

+ `display: none` - 完全隐藏，不占空间
+ `visibility: hidden` - 隐藏但保留原空间

## CSS布局实战
### 经典三栏布局实现
#### HTML结构
```html
<div id="wrap">
    <div id="header">页眉</div>
    <div id="nav">导航栏</div>
    <div id="main">主要内容</div>
    <div id="sidebar">侧边栏</div>
    <div id="footer">页脚</div>
</div>
```

#### CSS实现步骤
**【1】重置默认样式**

```css
html, body {
    margin: 0;
    padding: 0;
}
```

**【2】设置主容器**

```css
#wrap {
    width: 750px;
    margin: 0 auto;  /* 居中显示 */
}
```

**【3】主内容区和侧边栏并排**

```css
#main {
    float: left;
    width: 500px;
}

#sidebar {
    float: right;
    width: 250px;
}
```

**【4】页脚清除浮动**

```css
#footer {
    clear: both;
}
```

**【5】导航栏横向显示**

```css
#nav ul {
    margin: 0;
    padding: 0;
    list-style: none;
}

#nav li {
    display: inline;  /* 块级元素变内联 */
}
```

### 现代布局技术
#### Flex布局（推荐）
```css
.container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

#### CSS框架
**Bootstrap**之类的

## 长度单位详解
### 绝对单位
```css
width: 72pt;     /* 点 (1pt = 1/72英寸) */
width: 1in;      /* 英寸 */
width: 2.54cm;   /* 厘米 */
width: 25.4mm;   /* 毫米 */
width: 6pc;      /* 派卡 (1pc = 12pt) */
```

### 相对单位
```css
font-size: 1.2em;    /* 相对父元素字体大小 */
font-size: 2ex;      /* 相对字体x高度 */
width: 100px;        /* 像素 */
font-size: 120%;     /* 百分比 */
```

## CSS继承机制
+ **子元素会继承父元素的大部分CSS属性**
+ **子元素属性会覆盖父元素同名属性**

```css
body { 
    color: blue; 
    font-size: 12px; 
}

p { 
    font-size: 80%;  /* 继承color，覆盖font-size */
}
```

最终p元素：`color: blue; font-size: 9.6px;`

## 实用技巧总结
### 调试技巧
+ 使用不同背景色区分元素区域
+ 利用浏览器开发者工具检查元素
+ 渐进式添加样式，逐步调试

### 最佳实践
+ 优先使用外链CSS
+ 合理命名class和id
+ 遵循CSS重置规范
+ 保持代码简洁和可维护性

### 兼容性注意
+ IE6不支持：`position: fixed`、子代选择器、:before/:after
+ 使用CSS验证工具检查语法

## 学习资源
### 在线教程
+ [W3School CSS教程](https://www.w3school.com.cn/css/index.asp)
+ [MDN CSS参考](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference)
+ [CSS选择器手册](http://www.w3school.com.cn/cssref/css_selectors.asp)

### 实例练习
+ [W3School CSS实例](https://www.w3school.com.cn/css/css_examples.asp)
+ [HTML Dog实例](http://www.htmldog.com/examples/)

### CSS验证工具
+ [W3C CSS验证器](http://jigsaw.w3.org/css-validator/)

