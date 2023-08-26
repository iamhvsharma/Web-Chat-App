from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated user data for demonstration purposes
users = {
    "Harsh": "p1",
    "Aditi": "p2",
    "user3": "p3",
    # Add more usernames and passwords here...
}

# Simulated database for received messages
messages = {}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/options', methods=['POST'])
def options():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return render_template('options.html', username=username)
    else:
        return "Invalid login credentials"

@app.route('/send', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        recipient = request.form['recipient']
        message = request.form['message']

        # Initialize an empty list if recipient doesn't have messages yet
        if recipient not in messages:
            messages[recipient] = []

        # Append the new message to the list of messages for the recipient
        messages[recipient].append(message)
        
        return redirect(url_for('send_message'))
    return render_template('send_message.html')

@app.route('/receive/<username>')
def receive_message(username):
    received_messages = messages.get(username, [])
    return render_template('receive_message.html', messages=received_messages)


if __name__ == '__main__':
    app.run(debug=True)
