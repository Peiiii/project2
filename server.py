from wsgiref.simple_server import make_server
from hello import application

def test1():
    ##wsgi#########
    httpd=make_server('',8000,application)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()
def test2():
    from flask import Flask
    from flask import request,render_template

    app=Flask(__name__)

    @app.route('/',methods=['GET','POST'])
    def home():
        return render_template('home.html')
    @app.route('/signin',methods=['GET'])
    def signin_form():
        return render_template('form.html')
    @app.route('/signin',methods=['POST'])
    def signin():
        username=request.form['username']
        password=request.form['password']
        if username=='admin' and password=='password':
            return render_template('signin-ok.html',username=username)
        return render_template('form.html',message='Bad username or password',username=username)
    if __name__=="__main__":
        app.run(host='207.148.94.195',port=80)


if __name__=='__main__':
    test2()