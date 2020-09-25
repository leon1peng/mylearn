$(function() {
    $('#btnUp').click(function() {
        times = $('#times').val();
        comment = $('#comment').val();
        hId = $('#homeNum').html().trim();

        $.ajax({
            'url': 'detail/new',
            'type': 'post',
            'data': { 'homeworkId': hId, 'times': times, 'comment': comment },
            'dataType': 'json',
            success: function(data) {
                if (data.res == 1) {
                    location.href = '/index'
                } else {
                    $('#errmsg').show().html('Error: Incorrect input!')
                }
            }
        });
    })
})