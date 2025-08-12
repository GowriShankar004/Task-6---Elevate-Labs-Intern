
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {"title": "E-Commerce Website", "desc": "HTML/CSS/JS project for a store front"},
        {"title": "Coffee Cafe Ordering System", "desc": "Frontend ordering UI built with JS"},
        {"title": "Connecting Game", "desc": "A small interactive game using jQuery"}
    ]
    return render_template('index.html', projects=projects)

@app.route('/contact', methods=['GET','POST'])
def contact():
    submitted = False
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Print submission to terminal (as requested)
        print(f"[Contact form submission] Name: {name} | Email: {email} | Message: {message}")
        submitted = True
    return render_template('contact.html', submitted=submitted)

if __name__ == '__main__':
    app.run(debug=True)
