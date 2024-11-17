'''
Xpath 比 re 和 Bs4 更简单高效

1. Xpath 解析是在 XML 文档中搜索内容的一门语言
html 是 XML 的一个子集，因此 XML 可以处理，html 也可以处理
'''

'''
XML 示例，这里没有列出头信息
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
    </author>
</book>

这里的 <book> <id> <price> ... 都称为节点，而 <book> 又是 <id> <name> <price> <author> 的 父节点，反之前者是 <book> 的子节点

对于 Xpath 来说，这些节点的层级关系就像路径一样， 例如 /book/price 就能找到 price
'''

'''
Xpath 代码使用示例
'''
from lxml import etree # 导入 etree

xml = '''
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id='10086'>周大强</nick>
        <nick id='10010'>周芷若</nick>
        <nick class='joy'>周杰伦</nick>
        <nick class='jolin'>蔡依林</nick>
        <div>
            <nick>惹了</nick>
        </div>
        <span>
            <nick>惹了1</nick>
        </span>
    </author>
    
    <partner>
        <nick id='ppc'>胖胖陈</nick>
        <nick id='ppbc'>胖胖不陈</nick>
    </partner>
</book>
'''

tree = etree.XML(xml) # 把 XML 的内容加载成 etree 的对象

result = tree.xpath('/book') # 这行代码写入后，即可以正常使用 xpath 的功能，/表示层级关系，第一个/表示根节点
print(result) # return [<Element book at 0x29bb0bbcfc8>]，Element 即节点

result1 = tree.xpath('/book/name/text()') # text() 拿对应节点的文本内容
print(result1) # return ['野花遍地香']

result2 = tree.xpath('/book/author/nick/text()')
print(result2) # return ['周大强', '周芷若', '周杰伦', '蔡依林']，但是因为 惹了 在 div 下面，理所当然的拿不到

result3 = tree.xpath('/book/author//nick/text()')
print(result3) # return ['周大强', '周芷若', '周杰伦', '蔡依林', '惹了']，这样就全部拿到了

result4 = tree.xpath('/book/author/*/nick/text()')
print(result4) # return ['惹了', '惹了1']