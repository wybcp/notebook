# [strconv](https://golang.org/pkg/strconv/)

The most common numeric conversions are Atoi (string to int) and Itoa (int to string)


```golang
//string到int  
int,err := strconv.Atoi(string)  

//string到int64  
int64, err := strconv.ParseInt(string, 10, 64)  
//第二个参数为基数（2~36），
//第三个参数位大小表示期望转换的结果类型，其值可以为0, 8, 16, 32和64，
//分别对应 int, int8, int16, int32和int64

//int到string  
string := strconv.Itoa(int) 
//等价于
string := strconv.FormatInt(int64(int),10)
 
//int64到string  
string := strconv.FormatInt(int64,10)  
//第二个参数为基数，可选2~36
//对于无符号整形，可以使用FormatUint(i uint64, base int)

//float到string
string := strconv.FormatFloat(float32,'E',-1,32)
string := strconv.FormatFloat(float64,'E',-1,64)
// 'b' (-ddddp±ddd，二进制指数)
// 'e' (-d.dddde±dd，十进制指数)
// 'E' (-d.ddddE±dd，十进制指数)
// 'f' (-ddd.dddd，没有指数)
// 'g' ('e':大指数，'f':其它情况)
// 'G' ('E':大指数，'f':其它情况)

//string到float64
float,err := strconv.ParseFloat(string,64)

//string到float32
float,err := strconv.ParseFloat(string,32)

//int到int64
int64_ := int64(1234)
```