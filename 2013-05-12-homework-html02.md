---
layout: post
title: "HTML学习2-链接标签"
description: ""
category: LearnHTML
tags: [HTML]
---
{% include JB/setup %}
## HTML链接实例 ##


----------

###创建超级链接###



**例子代码:**

    <html>
    	<body>
    		<p>
    		   <a href="/index.html">本文本</a>是一个指向本网站中的一个页面的链接.
    		</p>
    		
    		<p>
    		   <a href="http://www.baidu.com/">本文本</a>是一个指向万维网上的页面的链接。
    		</p>
    	</body>
    </html>


###将图像作为链接###

**例子代码：**

    <html>
    	<body>
    		<p>可以用图像来做链接<a href="/example/html/lastpage.html"><img border="0" src="/img/button_next.gif"/></a>
    		</p>
    	</body>
    </html>


###在新的浏览器窗口打开链接###

**例子代码：**
    
    <html>
    	<body>
    		<a href="http://www.baidu.com/" target="_blank">百度一下，你就知道</a>
    		<p>把链接的target的属性设置为"_blank"，该链接会在新窗口中打开。</p>
    	</body>
    </html>


###链接到同一个页面的不同位置###

**例子代码：**

    <html>
    	<body>
    		<p>
    			<a href="#C4">查看 Chapter 2。</a>
    		</p>
    
    		<h2>Chapter 1</h2>
    		<p>This chapter explains ba bla bla</p>
    
    		<h2>Chapter 2</h2>
    		<p>This chapter explains ba bla bla</p>
    
    		<h2>Chapter 3</h2>
    		<p>This chapter explains ba bla bla</p>
    
    		<h2><a name="C4">Chapter 4</a></h2>
    		<p>This chapter explains ba bla bla</p>
    
    	</body>
    </html>


###跳出框架###

**例子代码：**
    
    <html>
    	<body>
    		<p>被锁在框架中了吗？</p> 
    		<a href="/index.html" target="_top">请点击这里！</a> 
    	</body>
    </html>

###创建电子邮件链接###

**例子代码：**

    <html>
    	<body>
    		<p>这是邮件链接：
    		<a href="mailto:someone@microsoft.com?subject=Hello%20again">发送邮件</a>
    		</p>
    
    		<p>
    		<b>注意：</b>应该使用 %20 来替换单词之间的空格，这样浏览器就可以正确地显示文本了。
    		</p>
    	</body>
    </html>


###创建电子邮件链接 2###

**例子代码：**

    <html>
    	<body>
    		<p>
    			这是另一个 mailto 链接：
    		<a href="mailto:someone@microsoft.com?cc=someoneelse@microsoft.com&
    		bcc=andsomeoneelse2@microsoft.com&subject=Summer%20Party&
    		body=You%20are%20invited%20to%20a%20big%20summer%20party!">发送邮件！</a>
    		</p>
    
    		<p>
    		<b>注意：</b>应该使用 %20 来替换单词之间的空格，这样浏览器就可以正确地显示文本了。
    		</p>	
    	</body>
    </html>
    



