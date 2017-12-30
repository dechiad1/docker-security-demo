from app import app, db, lm
from flask import render_template, flash, redirect, request, session, g, url_for
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, PostForm
from .models import Users, Posts
import psycopg2
import datetime

@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
	#posts = [{'author':{'username':'John'},'body':'and thats the way the cookie crumbles'}]
	posts = Posts.query.all()
	return render_template('index.html', title='Home',user=user, posts=posts)

@app.before_request
def before_request():
	g.user = current_user

@app.route('/login', methods=['GET','POST'])
def login():
	#is user logged in
	print g.user
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('index'))

	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		flash('login requested for user "%s"' % (form.user.data))
		after_login(form.user.data, form.passwd.data)
		print g.user
		return redirect(url_for('index'))
	
	if form.errors:
		for error in form.errors:
			flash('missing field: "%s"' % (error))
		return render_template('login.html', title='Sign In',form = form)
	else:
		return render_template('login.html', title='Sign In',form = form)

def after_login(user, passwd):
	u = Users.query.filter_by(username=user).first()
	print u
	if u is None:
		flash('user does not exist, please register')
		return False
	else:
		user_pass = u.passwd
		if user_pass != passwd:
			flash('incorrect password')
			return False
		login_user(u, remember=True)
		return True

@lm.user_loader
def load_user(id):
	return Users.query.get(int(id))

@login_required
@app.route('/create_post', methods=['GET','POST'])
def create_post():
	form = PostForm(request.form)
	if request.method == 'GET':
		return render_template('post.html', form = form)

	if request.method == 'POST' and form.validate():
		dt = datetime.datetime.utcnow()
		user_id = g.user.id
		p = Posts(body=form.body.data, timestamp=dt, user_id=user_id)
		db.session.add(p)
		db.session.commit()
	return redirect(url_for('index'))
	
	if form.errors:
		for error in form.errors:
			flash('missing field: "%s"' % (error))
		return render_template('login.html', title='Sign In',form = form)
	else:
		return render_template('login.html', title='Sign In',form = form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
