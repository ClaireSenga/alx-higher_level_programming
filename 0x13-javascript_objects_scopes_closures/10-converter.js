#!/usr/bin/node

exports.converter = function (base) {
  const convert = (num) => {
    if (num < base) {
      return num.toString();
    } else {
      return convert(Math.floor(num / base)) + (num % base).toString();
    }
  };

  return (num) => convert(num);
};
