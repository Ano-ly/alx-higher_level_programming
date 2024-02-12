#!/usr/bin/node
const animalMe = {
  name: 'Amarachi',
  age: 13,
  info: function () {
    console.log(this.name + '----' + this.age);
  }
};

animalMe.info();
