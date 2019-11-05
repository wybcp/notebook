# Markdown

- 分割线三个星号(`***`、`---`、`____`)
- `*斜体强调*`
- `**粗体强调**`
- `~~删除线~~`
- 表格对齐方式`|:--------|---------:|:-------:|`
- 插入引用`>`
- Reference-style links

  Reference-style links allow you to refer to your links by names, which you define elsewhere in your document:

    <pre>
    I get 10 times more traffic from [Google][1] than from [Yahoo][2] or [MSN][3].
  
    [1]: http://google.com/        "Google"
    [2]: http://search.yahoo.com/  "Yahoo Search"
    [3]: http://search.msn.com/    "MSN Search"
    </pre>

- 任务列表需要在 Markdown 列表项的段落部分用`[ ]`开头，也可以用`[x]`开头表示一个已选择的任务项。

- 生成目录的地方是用`[toc]`标签，会自动在此处生成目录

- 流程图

  ```flow
  st=>start: Start:>https://www.zybuluo.com
  io=>inputoutput: verification
  op=>operation: Your Operation
  cond=>condition: Yes or No?
  sub=>subroutine: Your Subroutine
  e=>end

  st->io->op->cond
  cond(yes)->e
  cond(no)->sub->io
  ```

  更多语法参考：[流程图语法参考](http://adrai.github.io/flowchart.js/)

- 序列图

  示例 1

  ```seq
  Alice->Bob: Hello Bob, how are you?
  Note right of Bob: Bob thinks
  Bob-->Alice: I am good thanks!
  ```

  示例 2

  ```seq

  Title: Here is a title
  A->B: Normal line
  B-->C: Dashed line
  C->>D: Open arrow
  D-->>A: Dashed open arrow
  ```
