$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    console.log(this);
    $(this).keydown((e) => {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const url = 'https://hellosalut.stefanbohacek.dev/';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
