a CMS based on django 1.0,supported by Django Dream Team,created by huyoo353 on 2008-NOV-10.

当前发布的版本是0.2.5, 基于django1.2.


---

# ddtcms ver0.1一些说明： #
  * 取消了registration的整合,因为它在google code不弄了,我用了userprofile,功能更强
  * 使用的photologue加了自动修改上传的图片名,采用时间和随机码

# 0.2.4.0 #
  * 开始使用django1.2.x的版本.
  * 所有的模板均修改为html5的
  * 准备将jiathis工具和统计代码放上去.
  * 重点强化默认模板的风格优化

# 0.2.4.1.20110802 #
  * 将图片随机命名全部改为小写,因为linux下面区分大小写,但是windows不区分,所以
  * 另外将jiathis工具和统计代码放上去了.
  * 更新了ddtcms.com网站代码,将原来的0.2.3.2.2010的全部删除,部署上了0.2.4.0,修改了一下文件上传名字小写问题就小升了一个版本.
# 0.2.4.2.20110804 #
  * 将字体文件放入captcha ,验证码程序在linux下找不到ttf字体.windows下可以找到.在linux下必须使用绝对路径.
  * 字体拷贝至/usr/share/fonts/truetype 和ddtcms项目根目录都不行.只有使用绝对路径.
# 0.2.4.2.20110806 #
  * 增加了dd\_belatedpng.js, 解决了IE6下PNG透明显示的问题.
  * 修改了默认主题的base.html和index.html的模板,主要是tab切换和整合js函数到一个general.js中去,使用DDTCMS命名空间.
  * 将图片切换的脚本有国人开发的flashslider1.0(问题主要是css的问题,脚本禁用情况下,图片全部显示了)更改为orbit1.2.3插件,并修复了一下半透明文字背景的效果.
  * 发现windows下面,nginx 的worker progress要是超过1个的话(比如2个或者4个),就会变得不稳定,浏览器访问将会没有反应,重启nginx之后几分钟就会出现死掉现象.

# 0.2.5.0.20110901 #
  * 开始使用django1.2.5的版本
  * 更新了profile
  * 更新了模板

# 0.3.0.0.20111104 #
  * 开始使用django1.3的版本
  * 对应修改一些固定文件到static的文件夹
  * 精简掉一些不使用的app,很久不更新的无用的app(僵尸APP)
  * 当前正在开发中...暂时不发布.


---

# DDTCMS #
## Summary: ##
```

DDTCMS(Django Dream Team's Content Management System),is a CMS based on django 1.0,supported by Django Dream Team,created by huyoo353 on 2008-NOV-10. 

http://code.google.com/p/ddtcms/

admin u/p: admin/admin 
```

## Requirements: ##
```
  * django 1.2  Django version 1.2 or greater. 
  * PILThe Python Imaging Library,Source: http://www.pythonware.com/products/pil/ 
  * markdown Markdown is a text-to-HTML conversion tool for web writers. http://daringfireball.net/projects/markdown/ 
  * django-navbar Site navigation controlled from the django admin with: Navigation bar Navigation tree Chained Navigation bars JSON sub tree requests (comming soon) Permission control on which entries are seen http://code.google.com/p/django-wikiapp/ 
  # django-wikiapp Django WikiApp is a pluggable application for Django that aims to provide a complete Wiki (for really small values of "complete") http://code.google.com/p/django-wikiapp/ 
  # django-photologue
  # django-forum
  # django-tagging
  # django-pressroom
  # gettext
Optional(needed when you use i18n tags in code or templates) 
  # Google Data API
Optional(allows image searching) Download it from http://code.google.com/p/gdata-python-client/ 
  # django-profile 
http://code.google.com/p/django-profile/ 
This is a Django pluggable user profile zone which can be used and customized easily in your social application web platform developed in django. 
```
## App Directory Structure: ##
  1. appname/
  1. --templates/
  1. ----appname/
  1. --templatetags/