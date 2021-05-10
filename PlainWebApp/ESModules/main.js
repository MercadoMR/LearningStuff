/* 
https://www.freecodecamp.org/news/node-module-exports-explained-with-javascript-export-function-examples/
*/
const Bars = require('./Bars');
Bars.f1b1();
console.log(new Bars.c1b1());
/*
import {fun1bar2 as f1b2} from './Bars';
f1b2();
import {class1bar2} from './Bars';
console.log(new class1bar2);
*/