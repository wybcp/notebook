# 洗牌算法

洗牌算法是我们常见的随机问题，在玩游戏、随机排序时经常会碰到。它可以抽象成这样：得到一个 M 以内的所有自然数的随机顺序数组。

##方法一
该文里的第一种方法，可以简单描述成：随机抽牌，放在另一组；再次抽取，抽到空牌则重复抽。“抽到空牌则重复抽”这会导致后面抽到空牌的机会越来越大，显然是不合理的。可以优化一步成：牌抽走后，原牌变少。（而不是留下空牌）代码如下：

```
function shuffle_pick_1(m) //洗牌 //抽牌法
{
    //生成m张牌
    var arr = new Array(m);
    for (var i=0; i<m; i++) {
        arr[i] = i;
    }

    //每次抽出一张牌，放在另一堆。因为要在数组里抽出元素，把后面的所有元素向前拉一位，所以很耗时。
    var arr2 = new Array();
    for (var i=m; i>0; i--) {
        var rnd = Math.floor(Math.random()*i);
        arr2.push(arr[rnd]);
        arr.splice(rnd,1);
    }
    return arr2;
}
```

这个也明显有问题，因为数组如果很大的话，删除中间的某个元素，会导致后面的排队向前走一步，这是一个很耗时的动作。
回想一下“我们为什么要删除那个元素？”目的就是为了不产生空牌。除了删除那个元素之外，我们是不是还有其它方式来去除空牌？
有的，我们把最后一张未抽的牌放在那个抽走的位置上就可以了。所以，这个思路我们可以优化成这样：

```
function shuffle_pick(m) //洗牌 //抽牌法优化牌
{
    //生成m张牌
    var arr = new Array(m);
    for (var i=0; i<m; i++) {
        arr[i] = i;
    }

    //每次抽出一张牌，放在另一堆。把最后一张未抽的牌放在空位子上。
    var arr2 = new Array();
    for (var i=m; i>0;) {
        var rnd = Math.floor(Math.random()*i);
        arr2.push(arr[rnd]);
        arr[rnd] = arr[--i];
    }
    return arr2;
}
```

除了抽牌思路，我们还可以用换牌思路。
《百度文库-洗牌算法》提到一种换牌思路：“随机交换两个位置，共交换 n 次，n 越大，越接近随机”。这个做法是不对的，就算 n 很大（例如 10 张牌，进行 10 次调换），也还存在很大可能“有的牌根本没换位置”。
顺着这个思路，做一点小调整就可以了：第 i 张与任意一张牌换位子，换完一轮即可。代码如下：

```
function shuffle_swap(m) //洗牌 //换牌法
{
    //生成m张牌
    var arr = new Array(m);
    for (var i=0; i<m; i++) {
        arr[i] = i;
    }

    //第i张与任意一张牌换位子，换完一轮即可
    for (var i=0; i<m; i++) {
        var rnd = Math.floor(Math.random()*(i+1)),
            temp = arr[rnd];
        arr[rnd] = arr[i];
        arr[i]=temp;
    }
    return arr;
}
```

除了抽牌与换牌的思路，我们还可以用插牌的思路：先有一张牌，第二张牌有两个位置可随机插入（第一张牌前，或后），第三张牌有三个位置可随机插入（放在后面，或插在第一位，或插在第二位），依此类推。代码如下：

```
function shuffle_insert_1(m) //洗牌 //插牌法
{
    //每次生成一张最大的牌，插在随机的某张牌前。因为要在数组里插入元素，把后面的所有元素向后挤一位，所以很耗时。
    var arr = [0];
    for (var i=1; i<m; i++) {
        arr.splice(Math.floor(Math.random()*(i+1)),0,i);
    }
    return arr;
}
```

以上的代码也会有一些问题：就是随着牌数的增多，插牌变得越来越困难，因为插牌会导致后面的很多牌都往后推一步。
当然，我们也可以适当的优化一下：先有 n-1 张牌，第 n 张牌放在最后，然后与任意一张牌互换位置。代码如下：

```
function shuffle_insert(m) //洗牌 //插牌法优化版，可以用数学归纳法证明，这种洗牌是均匀的。
{
    //每次生成一张最大的牌，与随机的某张牌换位子
    var arr = new Array(m);
    arr[0] = 0;
    for (var i=1; i<m; i++) {
        var rnd = Math.floor(Math.random()*(i+1));
        arr[i] = arr[rnd];
        arr[rnd] = i;
    }
    return arr;
}
```

好的，全部的代码如下，有兴趣的同学可以在自己的机器上试下，看下他们各自的执行效率、以及最后的结果是否是理论随机。

```
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=gb2312">
        <title>JK：javascript 洗牌算法 </title>

    </head>
    <body>
        <script type="text/javascript">

            function shuffle_pick_1(m) //洗牌 //抽牌法
            {
                //生成m张牌
                var arr = new Array(m);
                for (var i=0; i<m; i++) {
                    arr[i] = i;
                }

                //每次抽出一张牌，放在另一堆。因为要在数组里抽出元素，把后面的所有元素向前拉一位，所以很耗时。
                var arr2 = new Array();
                for (var i=m; i>0; i--) {
                    var rnd = Math.floor(Math.random()*i);
                    arr2.push(arr[rnd]);
                    arr.splice(rnd,1);
                }
                return arr2;
            }


            function shuffle_pick(m) //洗牌 //抽牌法优化牌
            {
                //生成m张牌
                var arr = new Array(m);
                for (var i=0; i<m; i++) {
                    arr[i] = i;
                }

                //每次抽出一张牌，放在另一堆。把最后一张未抽的牌放在空位子上。
                var arr2 = new Array();
                for (var i=m; i>0;) {
                    var rnd = Math.floor(Math.random()*i);
                    arr2.push(arr[rnd]);
                    arr[rnd] = arr[--i];
                }
                return arr2;
            }


            function shuffle_swap(m) //洗牌 //换牌法
            {
                //生成m张牌
                var arr = new Array(m);
                for (var i=0; i<m; i++) {
                    arr[i] = i;
                }

                //第i张与任意一张牌换位子，换完一轮即可
                for (var i=0; i<m; i++) {
                    var rnd = Math.floor(Math.random()*(i+1)),
                        temp = arr[rnd];
                    arr[rnd] = arr[i];
                    arr[i]=temp;
                }
                return arr;
            }

            function shuffle_insert_1(m) //洗牌 //插牌法
            {
                //每次生成一张最大的牌，插在随机的某张牌前。因为要在数组里插入元素，把后面的所有元素向后挤一位，所以很耗时。
                var arr = [0];
                for (var i=1; i<m; i++) {
                    arr.splice(Math.floor(Math.random()*(i+1)),0,i);
                }
                return arr;
            }

            function shuffle_insert(m) //洗牌 //插牌法优化版，可以用数学归纳法证明，这种洗牌是均匀的。
            {
                //每次生成一张最大的牌，与随机的某张牌换位子
                var arr = new Array(m);
                arr[0] = 0;
                for (var i=1; i<m; i++) {
                    var rnd = Math.floor(Math.random()*(i+1));
                    arr[i] = arr[rnd];
                    arr[rnd] = i;
                }
                return arr;
            }


            //alert(shuffle_pick(10))


            var funcs = [shuffle_pick_1, shuffle_pick, shuffle_swap, shuffle_insert_1, shuffle_insert],
                funcNames = ["抽牌", "抽牌优化", "换牌", "插牌", "插牌优化"]
                m = 10000,
                times=[];
            for(var i = 0; i < funcs.length; i++){
                var d0= new Date();
                funcs[i](m);
                funcNames[i] = (new Date() - d0) + '\t' + funcNames[i];
            }

            alert(funcNames.join('\n'));

        </script>
    </body>
</html>
```
