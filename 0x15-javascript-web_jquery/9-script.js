$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (result) {
      const greetDict = result;
      $('DIV#hello').text(greetDict.hello);
    }
  });
});
