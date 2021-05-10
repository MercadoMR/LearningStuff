// importing the whole module as a single variable
const whole = require("./module1.js");
whole.fun1();
whole.fun2();
console.log(new whole.class1());
const class2 = whole.class1;
console.log(new class2());

// or directly importing containers through object destructuring
const { fun1, str1, fun3  } = require("./module1");
console.log('Again fun1:');
fun1();
fun3();
console.log(str1);
