# [pkg/errors](https://github.com/pkg/errors)

Simple error handling primitives

## 追加上下文

```go
_, err := ioutil.ReadAll(r)
if err != nil {
        return errors.Wrap(err, "read failed")
}
```
