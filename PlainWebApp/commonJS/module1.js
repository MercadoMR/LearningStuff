function fun1(args){
    console.log('Named function fun1 imported!');
}

const fun2 = (args) => {
    console.log('Anonymous function (fun2) imported!');
};

class class1 {
    constructor(){
        console.log('The class is constructing!');
    }
}

module.exports = {
    fun1,
    fun2,
    class1,
};

module.exports.str1 = 'This string is being exported';
module.exports.fun3 = () => { console.log('Named function fun3 imported!') };

/*
As an alternative we could user something like:
exports.anExportedFunc = () => {};
exports.anExportedString = "this string is exported";
*/