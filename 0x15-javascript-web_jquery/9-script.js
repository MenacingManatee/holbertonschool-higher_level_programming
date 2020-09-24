$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr').done(function (data) {
    $('div#hello').text(data.hello);
  });
});
