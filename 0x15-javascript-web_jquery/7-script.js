$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: function (content) {
    const myDict = content;
    const nameHtml = myDict.name;
    $('DIV#character').text(nameHtml);
  }
});
