# [httprouter](https://github.com/julienschmidt/httprouter)

HttpRouter is a lightweight high performance HTTP request router 。

httprouter 是一个高性能，低内存占用的路由，它使用 radix tree 实现存储和匹配查找，所以效率非常高，内存占用也很低。

## 路由匹配

### Named parameters 单一匹配 `:`

单一匹配注意是否有其他注册的路由和命名参数的路由，匹配同一个路径，比如`/user/new` 这个路由和`/user/:name` 就是冲突的，不能同时注册。

### Catch-All parameters 通配符模式`*`

通配符模式，匹配所有的模式，不常用。

只要`*`前面的路径匹配，就是匹配的，不管路径多长，有几层，都匹配。

## Multi-domain / Sub-domains

```go
// We need an object that implements the http.Handler interface.
// Therefore we need a type for which we implement the ServeHTTP method.
// We just use a map here, in which we map host names (with port) to http.Handlers
type HostSwitch map[string]http.Handler

// Implement the ServeHTTP method on our new type
func (hs HostSwitch) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	// Check if a http.Handler is registered for the given host.
	// If yes, use it to handle the request.
	if handler := hs[r.Host]; handler != nil {
		handler.ServeHTTP(w, r)
	} else {
		// Handle host names for which no handler is registered
		http.Error(w, "Forbidden", 403) // Or Redirect?
	}
}

func main() {
	// Initialize a router as usual
	router := httprouter.New()
	router.GET("/", Index)
	router.GET("/hello/:name", Hello)

	// Make a new HostSwitch and insert the router (our http handler)
	// for example.com and port 12345
	hs := make(HostSwitch)
	hs["example.com:12345"] = router

	// Use the HostSwitch to listen and serve on port 12345
	log.Fatal(http.ListenAndServe(":12345", hs))
}
```

## httprouter 静态文件服务

httprouter 提供了很方便的静态文件服务，可以把一个目录托管在服务器上，以供访问。

```go
router.ServeFiles("/static/*filepath",http.Dir("./"))
```

只需要这一句核心代码即可，这个就是把当前目录托管在服务器上，以供访问，访问路径是/static。

使用 ServeFiles 需要注意的是，第一个参数路径，必须要以`/*filepath`，因为要获取我们要访问的路径信息。

## httprouter 异常捕获

```go
router.PanicHandler = func(w http.ResponseWriter, r *http.Request, v interface{}) {
		w.WriteHeader(http.StatusInternalServerError)
		fmt.Fprintf(w, "error:%s",v)
	}
```
