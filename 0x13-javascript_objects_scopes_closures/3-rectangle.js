#!/usr/bin/node
class Rectangle{
    constructor (w, h){
        if ((h > 0) && (w > 0)){
            this.width = w;
            this.height = h;
        }
    }

    print(){
        for (let i = 0; i < this.height; i++){
            let s = '';
            for (let j =0; j < this.width; j++){
                s += 'X';
            }
            console.log(s);
        }
    }

}
mod.exports = Rectangle;
