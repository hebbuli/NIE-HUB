from flask import Flask, render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def index():
	return render_template('python.html')

@app.route('/home',methods=["post","get"])
def home():
	#fruits={'apple','mango','banana'}
	if request.method == 'POST':
		return redirect('/login')
	return render_template('python.html')
	


@app.route('/login',methods=["post","get"])
def login():
		error = None
		if request.method == 'POST':
			if request.form['email'] != 'aishwarya@gmail.com' or request.form['password']!='csvicechair':
				error = 'Email or password does not match'
			else:
				#return render_template('python.html')
				return redirect('/home')
			return render_template('login.html',error=error)
		return render_template('login.html')


if __name__=='__main__':
	app.jinja_env.globals.update(chr=chr)
	app.run(host="localhost",port=7000,debug=True,threaded=True)
