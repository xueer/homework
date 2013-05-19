---
layout: post
title: "HTML学习4-表单标签"
description: ""
category: LearnHTML
tags: [HTML]
---
{% include JB/setup %}
## HTML 表单与输入实例 ##

----------

### 创建文本域(Text fields) ###

**代码如下:**

    <html>
    
    <body>
    
    <form>
    名：
    <input type="text" name="firstname">
    <br />
    姓：
    <input type="text" name="lastname">
    </form>
    
    </body>
    </html>

### 创建密码域 ###

**代码如下:**

    <html>
    
    <body>
    
    <form>
    用户：
    <input type="text" name="user">
    <br />
    密码：
    <input type="password" name="password">
    </form>
    <p>
    请注意，当您在密码域中键入字符时，浏览器将使用项目符号来代替这些字符。
    </p>
    </body>
    </html>

### 创建复选框 ###

**代码如下:**

    <html>
    
    <body>
    
    <form>
    用户：
    <input type="text" name="user">
    <br />
    密码：
    <input type="password" name="password">
    </form>
    <p>
    请注意，当您在密码域中键入字符时，浏览器将使用项目符号来代替这些字符。
    </p>
    </body>
    </html>

### 创建单选按钮 ###

**代码如下:**

    <html>
    
    <body>
    
    <form>
    男性：
    <input type="radio" checked="checked" name="Sex" value="male" />
    <br />
    女性：
    <input type="radio" name="Sex" value="female" />
    </form>
    
    <p>当用户点击一个单选按钮时，该按钮会变为选中状态，其他所有按钮会变为非选中状态。</p>
    
    </body>
    </html>


### 创建简单的下拉列表框 ###

**代码如下:**

    <html>
    
    <body>
    
    <form>
    <select name="cars">
    <option value="volvo">Volvo</option>
    <option value="saab">Saab</option>
    <option value="fiat">Fiat</option>
    <option value="audi">Audi</option>
    </select>
    </form>
    
    </body>
    </html>


### 创建一个简单的带有预选值的下拉列表 ###

**代码如下:**

    <html>
    
    <body>
    
    <form>
    <select name="cars">
    <option value="volvo">Volvo</option>
    <option value="saab">Saab</option>
    <option value="fiat" selected="selected">Fiat</option>
    <option value="audi">Audi</option>
    </select>
    </form>
    
    </body>
    </html>

### 创建一个文本域（多行文本输入控件） ###

**代码如下:**

    <html>
    <body>
    
    <textarea cols="30" rows="5">
    领先的 Web 技术教程 - 全部免费
    在w3school，你可以找到你所需要的所有的网站建设教程。
    从基础的HTML到XHTML，乃至进阶的XML、SQL、数据库、多媒体和WAP。
    </textarea>
    
    <p>您无法对本例进行编辑，因为我们的在线编辑器使用 textarea 进行输入，
    而浏览器不允许 textarea 中存在另一个 textarea。</p>
    
    </body>
    </html> 

### 创建按钮 ###

**代码如下:**

    <html>
    
    <body>
    
    <form>
    <input type="button" value="Hello world!">
    </form>
    
    </body>
    </html>
    
### 如何在数据周围绘制一个带标题的框 ###

**代码如下:**

    <!DOCTYPE HTML>
    <html>
    
    <body>
    
    <form>
      <fieldset>
    <legend>健康信息</legend>
    身高：<input type="text" />
    体重：<input type="text" />
      </fieldset>
    </form>
    
    <p>如果表单周围没有边框，说明您的浏览器太老了。</p>
    
    </body>
    </html>


----------

## 表单实例 ##

----------

### 带有输入框和确认按钮的表单 ###

**代码如下:**

    <html>
    <body>
    
    <form action="/example/html/form_action.asp" method="get">
      <p>First name: <input type="text" name="fname" /></p>
      <p>Last name: <input type="text" name="lname" /></p>
      <input type="submit" value="Submit" />
    </form>
    
    <p>请单击确认按钮，输入会发送到服务器上名为 "form_action.asp" 的页面。</p>
    
    </body>
    </html>

### 带有复选框的表单 ###

**代码如下:**

    <html>
    
    <body>
    
    <form name="input" action="/html/html_form_action.asp" method="get">
    I have a bike:
    <input type="checkbox" name="vehicle" value="Bike" checked="checked" />
    <br />
    I have a car: 
    <input type="checkbox" name="vehicle" value="Car" />
    <br />
    I have an airplane: 
    <input type="checkbox" name="vehicle" value="Airplane" />
    <br /><br />
    <input type="submit" value="Submit" />
    </form> 
    
    <p>如果您点击 "Submit" 按钮，您将把输入传送到名为 html_form_action.asp 的新页面。</p>
    
    </body>
    </html>

### 带有单选按钮的表单 ###

**代码如下:**

    <html>
    
    <body>
    
    <form name="input" action="/html/html_form_action.asp" method="get">
    Male: 
    <input type="radio" name="Sex" value="Male" checked="checked">
    <br />
    Female: 
    <input type="radio" name="Sex" value="Female">
    <br />
    <input type ="submit" value ="Submit">
    </form> 
    
    <p>如果您点击 "Submit" 按钮，您将把输入传送到名为 html_form_action.asp 的新页面。</p>
    
    </body>
    </html>


### 从表单发送电子邮件 ###

**代码如下:**

    <html>
    
    <body>
    <form action="MAILTO:someone@w3school.com.cn" method="post" enctype="text/plain">
    
    <h3>这个表单会把电子邮件发送到 W3School。</h3>
    姓名：<br />
    <input type="text" name="name" value="yourname" size="20">
    <br />
    电邮：<br />
    <input type="text" name="mail" value="yourmail" size="20">
    <br />
    内容：<br />
    <input type="text" name="comment" value="yourcomment" size="40">
    <br /><br />
    <input type="submit" value="发送">
    <input type="reset" value="重置">
    
    </form>
    </body>
    </html>