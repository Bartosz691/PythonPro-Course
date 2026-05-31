from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        
        name = request.form.get('name')
        email = request.form.get('email')
        
    registration = Registration(
        name=name
        email=email
    )
    
    db.session.add(registration)
    db.session.commit()
    
    return redirect(url_for('thanks'))

    if request.method == 'GET':
        return render_template('register.html')
    
    if __name__ == "__main__":
       app.run(debug=True)