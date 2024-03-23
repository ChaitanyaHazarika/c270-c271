# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'AC4eb1ff2cfc2148e76532e45162266bfc'
        auth_token = 'baac1792bd2c32c2dce775a2338638c2'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('MG01d3d5a683b68b92b5f799f184f69ae2') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods = ['POST'])
def get_otp():
    print('PROCESSSINGGGG')
    recievedOTP = request.form['recieved_otp']
    mobileNumber = request.form['number']
    accountSID = 'AC4eb1ff2cfc2148e76532e45162266bfc'
    authToken = 'baac1792bd2c32c2dce775a2338638c2'
    client = Client(accountSID, authToken)
    

    verification_check = client.verify \
        .services('Enter your service ID') \
        .verification_checks \
        .create(to=mobileNumber, code=recievedOTP)
    
    print("STATUS", verification_check.status)
    if verification_check.status == 'pending': 
        return 'ENTERED OTP IS WRONG????!!!!!'
    else: 
        return redirect('http://project-c272.onrender.com')










    

   







if __name__ == "__main__":
    app.run()

