# -*- coding: cp936 -*-
a={'hh':'hello', 'user':'huyoo'}
b={'hh1':'hello', 'user2':'huyoo'}
a.update(b)
print a
print b
common_dict={
    "sitename":"我的网站测试中。。。",
    "sitedomain":"127.0.0.1",
}

article_dict = {
'queryset': '1',
'date_field': 'pub_date',
}

article_dict.update(common_dict)
print article_dict
