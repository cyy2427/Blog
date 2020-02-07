import os

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user, logout_user

from blog.extensions import db, icon
from blog.forms.user import IconForm

user = Blueprint('user', __name__)


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = IconForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            filename = icon.save(request.files['icon'], folder='icons')
            current_user._icon_path = os.path.split(filename)[-1]
            db.session.commit()
            flash('Icon uploaded.')
            return redirect(url_for('user.profile'))
    return render_template('profile.html', user=current_user, form=form)


@user.route('/logout')
def logout():
    logout_user()
    flash('You are successfully logged out', 'success')
    return redirect(url_for('main.home'))
