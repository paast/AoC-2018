 
const fs = require('fs');

// load dataset
flist = fs.readFileSync('1.txt')
	.toString()
	.split('\r\n')
	.map(x => parseInt(x));

// day 1.1
const sum = flist.reduce((a, b) => a + b);
console.log(sum);

// day 1.2
const l = flist.length;
let count = 0;
let fsum = 0;
let fset = new Set();
let dupe = null;

while (true) {
	fsum += flist[count];
	if (fset.has(fsum)) {
		break;
	}
	fset.add(fsum);
	count++;
	if (count >= l) count %= l;
}


