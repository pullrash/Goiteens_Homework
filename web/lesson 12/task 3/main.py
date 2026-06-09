from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

participants_list = []

# ДОДАНО: автоматичний редірект з головної сторінки на сторінку реєстрації
@app.route('/')
def index():
    return redirect(url_for('event_register'))

@app.route('/event_register', methods=['GET', 'POST'])
def event_register():
    error = None
    name = ""
    email = ""
    time = "Ранок"

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        time = request.form.get('time')

        if not name or not email:
            error = "Будь ласка, заповніть усі поля!"
            return render_template('register.html', error=error, name=name, email=email, time=time)
        
        participants_list.append({
            "name": name,
            "email": email,
            "time": time
        })
        return redirect(url_for('participants'))

    return render_template('register.html', error=error, name=name, email=email, time=time)

@app.route('/participants')
def participants():
    return render_template('participants.html', participants=participants_list)

if __name__ == '__main__':
    app.run(debug=True)