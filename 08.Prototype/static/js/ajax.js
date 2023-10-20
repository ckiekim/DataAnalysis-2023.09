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

function getProfile() {
    $('#profileModal').modal('show');
    $.ajax({
        type: 'GET',
        url: '/changeProfile',
        data: ' ',
        success: function(result) {
            let profile = JSON.parse(result);
            $('#hiddenEmail').val(profile[0]);
            $('#modalEmail').val(profile[0]);
            $('#modalImage').val(profile[1]);
            $('#modalStateMsg').val(profile[2]);
            $('#modalGithub').val(profile[3]);
            $('#modalInsta').val(profile[4]);
            $('#modalAddr').val(profile[5]);
        } 
    })
}

function changeProfile() {
    $('#profileModal').modal('hide');
    let email = $('#hiddenEmail').val();
    let imageInputVal = $('#modalImage')[0];
    let stateMsg = $('#modalStateMsg').val();
    let github = $('#modalGithub').val();
    let insta = $('#modalInsta').val();
    let addr = $('#modalAddr').val();
    let formData = new FormData();
    formData.append('email', email);
    formData.append('image', imageInputVal.files[0]);
    formData.append('stateMsg', stateMsg);
    formData.append('github', github);
    formData.append('insta', insta);
    formData.append('addr', addr);
    $.ajax({
        type: 'POST',
        url: '/changeProfile',
        data: formData,
        processData: false,
        contentType: false,
        success: function(result) {
            
        }
    });
}