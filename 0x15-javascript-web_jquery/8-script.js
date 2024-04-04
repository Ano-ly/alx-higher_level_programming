$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (result) {
    const myDict = result;
    const seeList = myDict.results;
    const titleList = [];
    for (const movie of seeList) {
      titleList.push(movie.title);
    }
    for (const title of titleList) {
      $('UL#list_movies').append($('<li></li>').text(title));
    }
  }
});
