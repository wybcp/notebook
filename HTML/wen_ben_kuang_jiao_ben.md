# 文本框脚本

文本框：
```
<input type="text" name="tel3" id="txtTel3" size="4" maxlength="8" value="init" >
```

size显示字符；maxlengh容纳的字符数。

textarea使用rows和cols代替size，同时不能指定其最大字符数。

两者都将输入的内容保存在value属性中。
##选择文本

select()

取得选择的文本：
```
function getSelectedText(textbox){
                if (typeof textbox.selectionStart == "number"){
                    return textbox.value.substring(textbox.selectionStart, 
                            textbox.selectionEnd);                
                } else if (document.selection){
                    return document.selection.createRange().text;
                }//IE8-
            }
```

##过滤输入

选择性屏蔽字符输入：
```
EventUtil.addHandler(textbox, "keypress", function(event){
                event = EventUtil.getEvent(event);
                var target = EventUtil.getTarget(event);
                var charCode = EventUtil.getCharCode(event);
                
                if (!/\d/.test(String.fromCharCode(charCode)) && charCode > 9 && !event.ctrlKey){
                    EventUtil.preventDefault(event);
                }
                
            });
```            
##自动切换焦点

```
<input type="text" name="tel1" id="txtTel1" size="3" maxlength="3" >
            <input type="text" name="tel2" id="txtTel2" size="3" maxlength="3" >
            <input type="text" name="tel3" id="txtTel3" size="4" maxlength="4" >
            

 (function(){
       
            function tabForward(event){            
                event = EventUtil.getEvent(event);
                var target = EventUtil.getTarget(event);
                
                if (target.value.length == target.maxLength){
                    var form = target.form;
                    
                    for (var i=0, len=form.elements.length; i < len; i++) {
                        if (form.elements[i] == target) {
                            if (form.elements[i+1]){
                                form.elements[i+1].focus();
                            }
                            return;
                        }
                    }
                }
            }
                        
            var textbox1 = document.getElementById("txtTel1"),
                textbox2 = document.getElementById("txtTel2"),
                textbox3 = document.getElementById("txtTel3");
            
            EventUtil.addHandler(textbox1, "keyup", tabForward);        
            EventUtil.addHandler(textbox2, "keyup", tabForward);        
            EventUtil.addHandler(textbox3, "keyup", tabForward);        
                
        })();
```
##HTML5约束验证

required属性；email；url
