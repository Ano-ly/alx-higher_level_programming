#!/usr/bin/node

const Company = {
  inWork (name, job) {
    console.log(name + 'has been given the post of' + job);
  }
};

function Person (name) {
  this.name = name;
  this.age = 18;
  this.introduceself = function () {
    console.log(this.name + this.age);
  };
}

function Worker (name) {
  this.workState = 'Worker';
  this.ShowOff = function () {
    console.log('I am a worker!');
  };
}

Object.assign(Person.prototype, Company);
Object.assign(Worker.prototype, Company);

const Amarachi = new Person('Amarachi');
const Franca = new Worker('Franca');
console.log(Amarachi.age);
Amarachi.inWork('Amarachi', 'engineer');
Franca.inWork('Franca', 'engineer');
Franca.ShowOff();

class Human {
  name;
  age;

  constructor (name, age) {
    this.name = name;
    this.age = age;
  }

  whoAmI () {
    console.log('My name is ' + this.name);
  }
}

const Human = class {

}

const Amie = new Human('Amarachi', 12);
console.log(Amie.age);
Amie.whoAmI();

class Student extends Human {
  classNo;

  constructor (name, age, classNo) {
    super(name, age);
    this.classNo = classNo;
  }
}

const amieEng = new Student('Amarachi', 16, 'SSS 2');
amieEng.whoAmI();
console.log(amieEng.classNo);
