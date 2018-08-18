# debug

##抛出错误

大型应用程序，自定义错误使用assert()函数抛出
```
function assert(condition, message){
            if (!condition){
                throw new Error(message);
            }
        }
    
        function divide(num1, num2){
            assert(typeof num1 == "number" && typeof num2 == "number", 
                   "divide(): Both arguments must be numbers.");
            return num1 / num2;
        }
 ```