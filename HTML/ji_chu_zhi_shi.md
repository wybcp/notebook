# 基础知识

`<input>`和`<button>`用于定义按钮，其type值设为“submit”即可，图像按钮其type值为image。

##提交表单
单击提交按钮，提交表单，这种方式浏览器会在将请求发送给服务器之前触发submit事件，可以通过submit进行表单验证。

通过编程的方式调用submit()方法提交表单，无需按钮。

对于重复提交表单的问题，通常采用以下两种方法：
+ 在第一次提交后禁用提交按钮；
```
EventUtil.addHandler(form, "submit", function(event){
                event = EventUtil.getEvent(event);
                var target = EventUtil.getTarget(event);
            
                //get the submit button
                var btn = target.elements["submit-btn"];
            
                //disable it
                btn.disabled = true;
                
            });
```
+ 利用onsubmit事件处理程序取消后续的提交操作。

##重置表单

使用type值为reset。很少使用。


