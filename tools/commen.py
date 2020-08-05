import re
import html


def find_url(string):
    # findall() 查找匹配正则表达式的字符串
    pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[\u4E00-\u9FA5]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    url = re.findall(pattern, string)
    url = [html.unescape(item) for item in url]
    return url
