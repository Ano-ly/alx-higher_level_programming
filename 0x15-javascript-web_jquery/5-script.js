$('DIV#add_item').on('click', function (event) {
  $('UL.my_list').append($('<li></li>').text('item'));
});
