$(function() {
    $('#btnSb').click(function() {
        username = $('#username').val()
        number = $('#number').val()
        topicName = $('#topicName').val()
        difficulty = $('#difficulty').val()
        $.ajax({
            'url': '/homework',
            'type': 'post',
            'data': { 'username': username, 'number': number, 'topicName': topicName, "difficulty": difficulty },
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