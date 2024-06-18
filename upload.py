from flask import Flask, render_template

app = Flask(__name__,template_folder='templates',static_folder = 'static',static_url_path='/')

@app.route('/')
def home():
    table_data = [
        'images/1.jpg' ,
        'images/2.jpg' ,
        'images/3.jpg' ,
        'images/4.jpg' ,
        'images/5.png' ,
        'images/6.jpg' ,
        'images/7.jpeg' ,
    ]

    return render_template('upload.html', table_data=table_data)

@app.route('/upload')
def hello():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()