$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json').done(function (data) {
  $.each(data.results, function (ind) {
    $('ul#list_movies').append('<li>' + data.results[ind].title + '</li>');
  });
});
