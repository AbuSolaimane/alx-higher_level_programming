#!/usr/bin/node

exports.converter = function (base) {
  function theConverter (n) {
    return n.toString(base);
  }
  return theConverter;
};
