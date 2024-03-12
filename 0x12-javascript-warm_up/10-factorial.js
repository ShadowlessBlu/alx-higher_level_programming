#!/usr/bin/node

const factorial = (n) => {
    if (isNaN(n) || !Number.isInteger(parseFloat(n))) {
      return 1;
    }
  
    if (n <= 1) {
      return 1;
    }
  
    return n * factorial(n - 1);
  };
  
  const input = process.argv[2];
  const result = factorial(input);
  
  console.log(result);
  