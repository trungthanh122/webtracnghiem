from flask import Flask, render_template, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Minh Trieu Python-Flask Web App'
@app.route('/')
def main():
	todolist = [
		{
			'name':'Buy milk',
			'description': 'Buy 2 liters of milk in Coopmart'
		},
		{
			'name': 'Get money',
			'description': 'Get 500k from ATM'
		}
	]
	return render_template('index.html',todolist = todolist)

@app.route('/signUp', methods=['GET', 'POST'])
def SignUp():
	form = SignUpForm()
	if form.is_submitted():
		_name = form.inputName.data
		_email = form.inputEmail.data
		_password = form.inputPassword.data

		user = {'name':_name, 'email':_email, 'password':_password}
		return render_template('signUpSuccess.html', user = user)

	#return render_template('signup.html')
	return render_template('signup.html', form = form)

if __name__ == '__main__':
	app.run(host ='127.0.0.1', port='8080', debug=True)