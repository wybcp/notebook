# nginx 日志

## access.log

PV：指网站的访问请求数。包含同一来源 IP 的多次请求。

UV：指网站的独立访客数。同一来源 IP 的多次请求只计算一次。

一行 access.log 的信息，以空格为分隔符：
`205.205.150.16 - - [21/Sep/2018:14:21:12 +0800] "GET / HTTP/1.1" 301 185 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"`

网站的出错比例是很重要的一份数据。要统计用户访问出错的比例，可以通过统计每个请求的 HTTP CODE 得到。 在 HTTP 协议 中，如果 HTTP CODE 为 2xx 或 3xx 则视为访问正确，如 果 HTTP CODE 为 4xx 或 5xx, 则视为访问出错。

t3协议
`185.165.169.146 - - [21/Sep/2018:13:51:04 +0800] "t3 12.2.1" 400 173 "-" "-"`
