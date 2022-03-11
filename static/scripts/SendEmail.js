function sendMail(bookingForm) {
    emailjs.send("service_hc7jbil", "template_kh3yzfz", {
        "location": bookingForm.location.value,
        "date": bookingForm.date_time.value,
        "guests": bookingForm.guests.value,
        "fname": bookingForm.fname.value,
        "lname": bookingForm.lname.value,
        "email": bookingForm.email.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}

