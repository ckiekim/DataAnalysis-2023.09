// AJAX(Asynchronous Javascript and XML)
// Web page의 일부분만 변경하는 방법
function changeWeather() {
    let addr = $('#addr').text();
    $.ajax({
        type: 'GET',
        url: '/weather',
        data: {addr: addr},
        success: function(result) {
            $('#weather').html(result);
        }
    });
}

function changeProfile() {
    $('#imageInput').attr('class', 'mt-2');
}
function imageSubmit() {
    let imageInputVal = $('#image')[0];
    let formData = new FormData();
    formData.append('image', imageInputVal.files[0]);
    $.ajax({
        type: 'POST',
        url: '/change_profile',
        data: formData,
        processData: false,
        contentType: false,
        success: function(result) {
            $('#imageInput').attr('class', 'mt-2 d-none');
            let fname = '/static/data/profile.png?q=' + result;
            $('#profile').attr('src', fname);
        }
    });
}