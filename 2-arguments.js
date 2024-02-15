#!/usr/bin/node
let k;

if (process.argv.length < 3){
    k = 'No argument';
}
else if (process.argv.length === 3){
    k = 'Argument found';
}
else{
    k = 'Argument found';
}
console.log(k);