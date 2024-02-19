#!/usr/bin/node
const dict = require('./101-data').dict;
const dictcopy = dict;
const newdictionary = {};
for (const userID in dictcopy){
	    const occurance = dictcopy[userID];
	    if (!newdictionary[occurance]){
		            newdictionary[occurance] = [];

		        }
	    newdictionary[occurance].push(userID);
}
console.log(newdictionary);
