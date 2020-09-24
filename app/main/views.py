from flask import (render_template, url_for, abort, make_response,
    redirect, flash, current_app as app)
from flask_login import login_required, current_user
import pdfkit
from app.main import main
from app.auth import auth
from app.models import User

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/help')
def help():
    return render_template('steps.html')

@main.route('/template/<template>')
@login_required
def resume_template(template):
    if not current_user.is_authenticated:
        return redirect(url_for('app.auth.login'))
    if template == 'gemheart':
        pdf = render_template('user-gemheart.html')
    elif template == 'empire':
        pdf = render_template('user-empire.html')
    elif template == 'adolfa':
        pdf = render_template('user-adolfa.html')
    elif template == 'pixel':
        pdf = render_template('user-pixel.html')
    else:
        return abort(404)
    pdf=pdfkit.from_string(pdf, False, 
                configuration=app.config['PDF_TO_HTML'])
    response = make_response(pdf)
    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition']='inline; filename.pdf'

    return response

@main.route('/resume')
@login_required
def resume():
    if not current_user.is_authenticated: 
        return redirect(url_for('app.auth.login'))
    return {'message': 'In progress'}

@main.route('/templates')
def templates():
    if not current_user.is_authenticated:
        return redirect(url_for('app.auth.login'))
    return render_template('templates.html')