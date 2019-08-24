# encoding/json 包

基本的 JSON 类型有数字（十进制或科学记数法）、布尔值（true 或 false）、字符串，其中字符串是以双引号包含的 Unicode 字符序列

结构体 slice 转为 JSON 的过程叫编组（marshaling）。编组通过调用 json.Marshal 函数。

为了生成便于阅读的格式，另一个 json.MarshalIndent 函数将产生整齐缩进的输出。该函数有两个额外的字符串参数用于表示每一行输出的前缀和每一个层级的缩进

编码的逆操作是解码，对应将 JSON 数据解码为 Go 语言的数据结构，Go 语言中一般叫 unmarshaling，通过 json.Unmarshal 函数完成。

## [html 转义处理](https://hacpai.com/article/1524558037151)

```golang
type Test struct {
	Content		string
}
func main() {
	t := new(Test)
	t.Content = "http://www.baidu.com?id=123&test=1"
	bf := bytes.NewBuffer([]byte{})
	jsonEncoder := json.NewEncoder(bf)
	jsonEncoder.SetEscapeHTML(false)
	jsonEncoder.Encode(t)
	fmt.Println(bf.String())
}
{"Content":"http://www.baidu.com?id=123&test=1"}
```
