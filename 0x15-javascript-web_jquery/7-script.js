$(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    (data, statusText) => {
      const name = data.name;
      $('DIV#character').text(name);
    });
});
