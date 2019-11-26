# [charset 编码](https://html.spec.whatwg.org/multipage/parsing.html#determining-the-character-encoding)

`golang.org/x/net/html/charset`

    DetermineEncoding(content []byte, contentType string) (e encoding.Encoding, name string, certain bool)
    // DetermineEncoding determines the encoding of an HTML document by examining
    // up to the first 1024 bytes of content and the declared Content-Type.
    //
    // See http://www.whatwg.org/specs/web-apps/current-work/multipage/parsing.html#determining-the-character-encoding

其实只是判断 UTF-8，其余返回默认值
