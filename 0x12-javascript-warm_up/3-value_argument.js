#!/usr/bin/node

// Get the first argument passed to the script
const arg1 = process.argv[2];

// Print the first argument or "No argument" if none is passed
console.log(arg1 || 'No argument');