// Uses the jQuery API to add a red class to header tag & turn it
// red when div#red_header tag is clicked

$('div#red_header').click(function () {
    $('header').addClass('red');
  });
