from lxml import etree

tree = etree.parse('16.Xpath解析示例html文件.html')
result = tree.xpath('/html/body/ul/li/a/text()')
print(result) # return ['百度', '谷歌', '搜狗']

# 单独拿到文本 百度
result1 =tree.xpath('/html/body/ul/li[1]/a/text()')
print(result1) # return ['百度']，注意 xpath 解析的索引是从 1 开始数，而不是从 0 开始

# 单独拿到文本方法1 大炮
result2 =tree.xpath('/html/body/ol/li[2]/a/text()')
print(result2) # return ['大炮']

# 单独拿到文本方法2 大炮
result3=tree.xpath('/html/body/ol//li/a[@href="dapao"]/text()')
print(result3) # return ['大炮']

# 对 ol 里的 li 进行遍历
ol_li_list = tree.xpath('/html/body/ol/li')
for li in ol_li_list:
    print(li.xpath('./a/text()')) # ./ 表示从当前节点开始查找
    print(li.xpath('./a/@href')) # 拿取 href 属性的值

ol_li_list1 = tree.xpath('/html/body/ol/li/a/text()')
for li_text in ol_li_list1:
    print(li_text) # 输出结果不同，但目标效果是一样的


