# 遍历

遍历以给定的节点为根。IE不支持DOM遍历

##NodeIterator

document.creatNodeIterator(root(搜索的起节点),whatToShow,filter,布尔值)
```
 var filter = function(node){
                    return (node.tagName.toLowerCase() == "li") ? 
                        NodeFilter.FILTER_ACCEPT : 
                        NodeFilter.FILTER_SKIP;
                };
                ```

nextNode()

previousNode()

##treeWalker
treeWalker是NodeIterator的升级版。
