# range
通过范围可以选择文档中的一个区域而不必考虑节点的界限。

document.createRange()

##实现简单的选择

selectNode():选择整个节点；

selectNodeContents()：选择节点的子节点。
##复杂选择

setStart()：接受两个参数：参数一，参照节点相当于startContainer()；参数二,偏移量值等同于startOffset();

setEnd()：参照节点等同于endContainer()，偏移量值变成endOffset().


