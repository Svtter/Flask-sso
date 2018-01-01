from flask import Flask, session, redirect, url_for, escape, request
from flask import make_response
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

#登陆
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        passwd = request.form['password']
        user_file = open('account.txt','r')                             #打开帐号文件
        user_list = user_file.readlines()
        for user_line in user_list:                                     #对帐号文件进行遍历
            (user,password) = user_line.strip('\n').split()             #分别获取帐号和密码信息
            if name == user:                                            #如用户名正常匹配
                if passwd == password:                                  #密码正确
                    user_file.close()                                   #关闭帐号文件
                    session['username'] = request.form['username']
                    resp = make_response(render_template('login.html'))
                    resp.set_cookie('username',name)#设置cookies
                    return resp
                return 'Password is wrong!'
        return 'User not exist!'
    return render_template('login.html')#get和其它请求

#
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)

    return redirect(url_for("delete_cookie"))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


#删除cookie
@app.route("/delete_cookies")
def delete_cookie():
    resp = make_response("delete cookie ok")
    resp.delete_cookie('username')
    return resp

#获取cookie
@app.route('/get_cookies')
def test_cookies():
    if request.method == 'GET':
        username = request.cookies.get('username',None)
    if username:
        return 'welcome {0}'.format(username)
    else:
        return 'Please login first.'



if __name__ == '__main__':
    app.run()
