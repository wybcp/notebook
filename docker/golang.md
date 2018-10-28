# [golang](https://hub.docker.com/_/golang/)

<https://www.zhihu.com/pub/reader/119570839/chapter/1035129531052568576>

```bash
root@iZwz97tbgo9lk6rm6lxu2wZ:~# mkdir golang
root@iZwz97tbgo9lk6rm6lxu2wZ:~# cd golang/
root@iZwz97tbgo9lk6rm6lxu2wZ:~/golang# vim Dockerfile
root@iZwz97tbgo9lk6rm6lxu2wZ:~/golang# vim main.go
root@iZwz97tbgo9lk6rm6lxu2wZ:~/golang# docker build -t my-golang-app .
root@iZwz97tbgo9lk6rm6lxu2wZ:~/golang# docker run -it --rm --name my-running-app my-golang-app
Hello,世界
```

`Dockerfile`

```Dockerfile
FROM golang:1.11
RUN mkdir -p /go/src/app
WORKDIR /go/src/app
COPY . .

RUN go get -d -v ./...
RUN go install -v ./...

CMD ["app"]
```

`main.go`

```golang
package main
import "fmt"
func main() {
    fmt.Println("Hello, 世界")
}
```
