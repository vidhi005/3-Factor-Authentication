function generateOTP() {
    return Math.floor(1000 + Math.random() * 9000); // Generate a 4-digit OTP
}

function validateOTP() {
    const enteredOTP = document.getElementById("otpInput").value;
    const generatedOTP = localStorage.getItem("OTP");

    if (enteredOTP === generatedOTP) {
        document.getElementById("message").innerHTML = "OTP Verified!";
    } else {
        document.getElementById("message").innerHTML = "OTP Verification Failed!";
    }
}

const OTP = generateOTP();
localStorage.setItem("OTP", OTP);
alert("Your OTP is: " + OTP);