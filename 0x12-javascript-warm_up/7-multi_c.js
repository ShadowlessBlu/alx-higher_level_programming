#!/usr/bin/node

// Check if the first argument exists and can be converted to an integer
if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(process.argv[2]);
  // Check if the first argument can be converted to an integer
  if (isNaN(x)) {
    console.log('Missing number of occurrences');
  } else {
    // Print "C is fun" x times using a loop
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
}
