---
layout: post
title: "HTML学习1-基础标签"
description: ""
category: LearnHTML
tags: [HTML]
---
{% include JB/setup %}
## HTML 基础标签实例 ##
* * *
**HTML代码如下:**

    <html>
    <head>
    	<title> HTML 基础标签实例 </title>
    </head>
    
    <body bgcolor="blue">
    
    	<h1 align="center">设置1号标题样式并居中显示</h1>
    	<h2>2号标题样式</h2>
    	<h3>3号标题样式</h3>
    	<h4>4号标题样式</h4>
    	<h5>5号标题样式</h5>
    	<h6>6号标题样式</h6>
    
    	<p>head元素表示页面的头</p>
    	<p>title元素表示页面的标题</p>
    	<p>body元素表示页面正文</p>
    	<p>p标签表示一个段落。</p>
    
    	<p>
    		段落的行数依赖于浏览器窗口的大小，
    		如果调节浏览器窗口的大小，将改变段落中的行数。
    	</p>
    	<p>	在段落中不会自动换行的，如果想要换行需要使用br标签</p>
    	
    	<p>
    		春眠不觉晓，<br />
    		处处闻啼鸟。
    	</p>
    
    	<p>在页面中增加水平线，要用hr标签</p>
    	<hr />
    
    	<p>在页面中增加注释的话，用!--和--标签 </p>
    	<!--这是一段注释。-->
    
    	<p>设置页面的背景色，则用到的是bgcolor标签</p>
    
    </body>
    </html>
