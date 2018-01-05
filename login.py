from flask import Flask, redirect, url_for, escape, request
from flask import make_response
from flask import render_template
from db_manage import User
from flask import jsonify,abort
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'

users = [ ]

#wjw的函数
def add_token():
#get_users()
#增加id
    return None

def delete_token():
#get_users()
#删掉id
    return None


#tokenid
def generate_auth_token(self, expiration=3600):
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'id': 2 })

#登陆
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        user=User()
        user.name= request.form['username']
        password=user.login()
        passwd = request.form['password']
    
        if password == "mei you zhe ren":
            return 'user not exist'
        if passwd == password:                                  #密码正确
            tokenid = str(generate_auth_token(3600))
            
            user = {
                'username': user.name,
                'id': 1,
                'password': password,
                'tokenid': tokenid
            }
            
            
            users.append(user)
            add_token()#wjw

            return 'success'
        return 'Password is wrong!'
    return render_template('login.html')#get和其它请求


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


#注销
@app.route('/logout')
def logout():
    delete_token()#wjw

    return 'user logout.'
#

if __name__ == '__main__':
    app.run()
