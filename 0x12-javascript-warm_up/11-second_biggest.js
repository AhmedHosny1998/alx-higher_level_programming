#!/usr/bin/node
const args = [];
if(process.argv.length < 4){
	console.log(0);
}

for (let i = 2; i < process.argv.length; i++){
	const arg = parseInt(process.argv[i]);
	args.push(arg);
}
const sor = args.sort((a, b) => a - b);
if(sor[sor.length - 2]){
	console.log(sor[sor.length - 2]);
}

