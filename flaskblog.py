from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c637300bb59271eb97d968c59086b5b0'

posts = [
	{
		'author': 'Ron Hu',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'October 27, 2000'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'October 27, 2001'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html',title='About')

@app.route("/register", methods=['GET','POST'])
def register():
	form  = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html',title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
	form  = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "socrates@greece.com" and form.password.data == "phaedo":
			flash(f'Login Successful!','success')
			return redirect(url_for('home'))
		else:
			flash(f'Login Failed. Try again.','danger')
	return render_template('login.html',title='Login',form=form)

if __name__== '__main__':
	app.run(debug=True)