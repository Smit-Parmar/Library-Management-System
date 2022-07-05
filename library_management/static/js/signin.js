$(() => {
    console.log("Boom!");
    const token = window.localStorage.getItem("Authorization");
    if(token) {
        alert("User is already logged in!");
        window.location.href = "/";
    }
});

$("#btn-login").on('click', loginUser);

function loginUser() {
    console.log("Login Clicked!");

    const sEmailID = $("#email").val();
    const sPassword = $("#password").val();

    console.log({ sEmailID });
    console.log({ sPassword });

    if (!sEmailID) {
        alert("Please enter email ID!")
        return;
    }

    if (!sPassword) {
        alert("Please enter Password!")
        return;
    }

    // TODO: validate the data

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/api/token/",
        data: {
            email: sEmailID,
            password: sPassword
        },
        dataType: 'json',
        success: function (result, status, xhr) {
            alert("Admin Logged In Successfully");
            console.log(result);
            console.log(status);
            console.log(xhr);

            window.localStorage.setItem("Authorization", xhr.responseJSON.access)

            window.location.href = '/';

        },
        error: function (xhr, status, error) {
            console.log(xhr);
            console.log(status);
            console.log(error);
            alert(xhr.responseJSON.detail);
        }
    })

}