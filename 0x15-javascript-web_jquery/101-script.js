$(document).ready(function () {
  $('DIV#add_item').on('click', function (event) {
    $('UL.my_list').append($('<li></li>').text('Item'));
  });
  $('DIV#remove_item').on('click', function (event) {
    $('UL.my_list').remove();
  });
  $('DIV#clear_list').on('click', function (event) {
    $('UL.my_list').empty();
  });
});
