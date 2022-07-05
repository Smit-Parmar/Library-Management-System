$(() => {
    console.log("Boom!");
    const token = window.localStorage.getItem("Authorization");
    if(token) {
        alert("Admin is already logged in!");
        window.location.href = "/";
    }
});

$("#btn-signup").on('click', signupAdmin);

function signupAdmin() {
    console.log("Signup Clicked!");

    const sEmailID = $("#email1").val();
    const sPassword1 = $("#password1").val();
    const sPassword2 = $("#password2").val();
    const crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    console.log(crf_token);
    console.log({ sEmailID });
    console.log({ sPassword1 });
    if (!sEmailID) {
        alert("Please enter email ID!")
        return;
    }

    if (sPassword1!=sPassword2) {
        alert("Password does not match")
        return;

    }else{
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/api/admin/signup/",
            headers:{"X-CSRFToken":crf_token},
            data: {
                email: sEmailID,
                password: sPassword1
            },
            dataType: 'json',
            success: function (result, status, xhr) {
                alert("Admin Signup Successfully");
                console.log(result);
                console.log(status);
                console.log(xhr);
    
                window.location.href = '/login-signup';
    
            },
            error: function (xhr, status, error) {
                console.log(xhr);
                console.log(status);
                console.log(error);
                alert(xhr.responseJSON.detail);
            }
        })
    }

    // TODO: validate the data

}