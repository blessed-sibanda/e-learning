$('#modules').sortable({
  stop: function (event, ui) {
    modules_order = {};
    $('#modules')
      .children()
      .each(function () {
        // update the order field
        $(this)
          .find('.order')
          .text($(this).index() + 1);
        modules_order[$(this).data('id')] = $(this).index();
      });
    $.ajax({
      type: 'POST',
      url: '{% url "module_order" %}',
      contentType: 'application/json; charset=utf8',
      dataType: 'json',
      data: JSON.stringify(modules_order),
    });
  },
});

$('#module-contents').sortable({
  stop: function (event, ui) {
    contents_order = {};
    $('#modules-contents')
      .children()
      .each(function () {
        // update the order field
        $(this)
          .find('.order')
          .text($(this).index() + 1);
        contents_order[$(this).data('id')] = $(this).index();
      });
    $.ajax({
      type: 'POST',
      url: '{% url "content_order" %}',
      contentType: 'application/json; charset=utf8',
      dataType: 'json',
      data: JSON.stringify(contents_order),
    });
  },
});
