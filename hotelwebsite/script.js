
function bookNow() {
    alert("Thank you for booking with us! We will get back to you shortly.");
}


function submitForm(event) {
    event.preventDefault(); 

    
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;

    
    alert("Message Sent! \nName: " + name + "\nEmail: " + email + "\nMessage: " + message);
    
    
    document.getElementById("contact-form").reset();
}
