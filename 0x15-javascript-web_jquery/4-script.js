#!/usr/bin/node
$('DIV#red_header').on('click', function (event) {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').addClass('green');
  }
});
