#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const simList = list.filter(function (n) {
    return n === searchElement;
  });
  return (simList.length);
};
