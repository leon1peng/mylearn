$(function () {
    $('#btnSb').click(function () {
        name = $('#heroname').val()
        gender = $('#herogender').val()
        skill = $('#heroskill').val()
        $.ajax({
            'url': '/add_ajax_check',
            'type': 'post',
            'data': {'name': name, 'gender': gender, 'skill': skill},
            'dataType': 'json',
            success : function (data) {
                if (data.res == 1){
                    location.href = '/index'
                    <!--$('#errmsg').show().html('Added Successful!')-->
                }
                else{
                  $('#errmsg').show().html('Error: Incorrect input!')
                }
            }
        });
    })
})

$(function () {
    $('#return').click(function () {
        $.ajax({
            'url': '/add_return',
            'dataType': 'json',
            success: function (data) {
                if (data.res == 1){
                    location.href = '/index'
                }
            }
        });
    })
})