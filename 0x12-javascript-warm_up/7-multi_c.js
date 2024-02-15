#!/usr/bin/node
const c = parseInt(process.argv[2]);
if (isNaN(c)) {
	  console.log('Missing number of occurrences');
}
for (let i = 0; i < c; i++) {
	  console.log('C is fun');
}
