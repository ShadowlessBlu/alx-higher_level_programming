#!/usr/bin/node

module.exports = {
  addMeMaybe: function (number, theFunction) {
    const newNumber = number + 1;
    theFunction(newNumber);
  },
};
