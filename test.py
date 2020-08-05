import re

string = '里的被指定给this的属性会被所有通过此构造函数创造出的实例共享，这样就解决了使用构造函数方式创造对象时造成的重复问题。<br>在JavaScript中，所有的对象都是基于 Object；所有的对象都继承了Object.prototype的属性和方法，它们可以被覆盖（除了以null为原型的对象，如 Object.create(null)）。</p><h4>4.原型链</h4><p><img src="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3527360487,647213490&amp;fm=26&amp;gp=0.jpg" style="max-width:100%;"><br></p><p><br></p>'


def find_url(string):
    # findall() 查找匹配正则表达式的字符串
    # reg = re.compile('(http):[^\s]*?(jpge|jpg|png|PNG|JPG)', re.S)
    pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    url = re.findall(pattern, string)
    return url


urls = find_url(string)
print(urls)
