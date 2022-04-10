// console.log('hi')

// function sendMail() {
//     var username = "{{ user.id }}";
//     document.getElementById("user_id").value = username;

//     var email = "{{ user.email }}";
//     document.getElementById("user_email").value = email;

//     var fname = "{{ user.first_name }}";
//     document.getElementById("user_first_name").value = fname;

//     var lname = "{{ user.last_name }}";
//     document.getElementById("user_last_name").value = lname;

//     var templateParams = {
//         fname: fname,
//         email: email,
//         location: location,
//         // date: date,
//         guests: guests,

//     }

//     console.log('SUCCESS!', fname, lname, email);

//     emailjs.send("service_hc7jbil", "template_kh3yzfz", templateParams)
//     .then(function (response) {
//         console.log('SUCCESS!', response.status, response.text, fname, lname, email);
//     }, function (error) {
//         console.log('FAILED...', error);
//     });
// }