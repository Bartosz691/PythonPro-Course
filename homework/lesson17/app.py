from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = ['Adam', 'Ewa', 'Karol']
    
   return render_template(
       'index.html'
       title='Strona główna'
       users =users
   )
   
@app.route('/users/<name>')
def user_page(name):
    return render_template(
        'user.html'
        username=name
    
 )
    
if __name__ == "__main__":
    app.run(debug=True)