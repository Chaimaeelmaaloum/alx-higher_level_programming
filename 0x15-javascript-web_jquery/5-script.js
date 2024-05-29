$('DIV#add_item').click(() => {
  const list_elem = document.createElement('li');
  list_elem.innerText = 'item';
  $('UL.my_list').append(list_elem);
});
