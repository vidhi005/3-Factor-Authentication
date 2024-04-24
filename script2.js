const fs = require('fs');
const http = require('http');
const url = require('url');

const server = http.createServer((req, res) => {
    const q = url.parse(req.url, true).query;
    const phone = q.phone;
    const otp = generateOTP();

    if (req.url === '/') {
        res.setHeader('Content-Type', 'text/html');
        res.write('<h2>Welcome to OTP Verification</h2>');
        res.write('<form action="/verify" method="get">');
        res.write('<input type="text" name="phone" placeholder="Enter Phone Number" required><br>');
        res.write(`<input type="text" name="otp" placeholder="Enter OTP (OTP: ${otp})" required><br>`);
        res.write('<input type="submit" value="Verify OTP">');
        res.write('</form>');
        res.end();
    } else if (req.url === '/verify') {
        if (verifyOTP(phone, otp)) {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.write('OTP Verification Successful');
        } else {
            res.writeHead(403, { 'Content-Type': 'text/html' });
            res.write('OTP Verification Failed');
        }
        res.end();
    } else {
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.write('Page Not Found');
        res.end();
    }
});

server.listen(3000, () => {
    console.log('Server is running on port 3000');
});

function generateOTP() {
    // Generate a random 4-digit OTP
    return Math.floor(1000 + Math.random() * 9000);
}

function verifyOTP(phone, otp) {
    // Read user data from a CSV file
    const data = fs.readFileSync('user_data.csv', 'utf8').split('\n');
    for (let i = 0; i < data.length; i++) {
        const [savedPhone, savedOTP] = data[i].split(',');
        if (savedPhone === phone && parseInt(savedOTP) === otp) {
            return true;
        }
    }
    return false;
}
