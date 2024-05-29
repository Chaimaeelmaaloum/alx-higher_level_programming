$(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json',
    (data, statusText) => {
      const name = data.results.map(element => element.title);
      name.forEach((element) => {
        $('UL#list_movies').append(`<li>${element}</li>`);
      });
    });
});
