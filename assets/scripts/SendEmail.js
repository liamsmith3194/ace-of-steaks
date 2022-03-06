function sendMail(bookingForm) {
    emailjs.send("service_hc7jbil", "template_kh3yzfz", {
        "location": bookingForm.location.value,
        "date": bookingForm.date_time.value,
        "guests": bookingForm.guests.value,
        "to_fname": bookingForm.fname.value,
        "to_lname": bookingForm.lname.value,
        "to_email": bookingForm.email.value,
        "company_email": "bookings@aceofsteaks.co.uk"
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
