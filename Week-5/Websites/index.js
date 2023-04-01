let age = 0
let msg = "  "

function add_numbers(num1,num2)
{
    return num1 + num2
}

document.getElementById("confirm_btn").onclick=function(){
    console.log("You can drive");
    age = document.getElementById("age").innerHTML.valueOf
    if(age=18){
        msg = "You are not allowed"
        document.getElementById("get_in").innerHTML=msg
    }else
        msg = "welcome to the club"
        document.getElementById("get_in").innerHTML=msg
}
