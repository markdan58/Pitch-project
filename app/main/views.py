
from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from .. import db,photos
from ..models import User, Pitch, Comment
from flask_login import login_required
from flask_login import login_required, current_user
from .forms import CommentsForm,PitchForm
from .forms import UpdateProfile


# Views
@main.route('/',methods=['GET','POST'])
def index():
    '''
    View page function that returns the pitch titles on the index page
    '''
    form = PitchForm()

    if form.validate_on_submit():
        new_pitch = Pitch(actual_pitch=form.Pitch.data,category=form.Category.data, user_id=current_user.id)
        new_pitch.save_pitch()
        flash('successfully saved')
    pitch = Pitch.query.filter_by(category='product')
    
    pickuplines = Pitch.query.filter_by(category='pickuplines')
    return render_template('pitch.html',title = 'new_pitch', pitch_form=form, pitch=pitch,pickuplines=pickuplines)

    interview = Pitch.query.filter_by(category='interview')
    return render_template('pitch.html',title = 'new_pitch', pitch_form=form, pitch=pitch,interview=interview)

    promotion = Pitch.query.filter_by(category='promotion')
    return render_template('pitch.html',title = 'new_pitch', pitch_form=form, pitch=pitch,promotion=promotion)

@main.route('/pitch/comments/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    pitch = Comment.query.filter_by(pitch_id=id).all()
    if form.validate_on_submit():

       
        new_comment = Comment(pitch_id=id, comments=form.comments.data)

       
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.category'))
    title = ' comment'
    return render_template('new_comment.html',title = title, comment_form=form, pitchs=pitch)

@main.route('/comments/<int:id>', methods = ['GET','POST'])
@login_required
def comment(id):
    form = CommentsForm()
    pitch = Comment.query.filter_by(pitch_id=id).all()
    if form.validate_on_submit():

    
        new_comment = Comment(pitch_id=id, comments=form.comments.data)

        
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.index'))
    title = ' comment'
    return render_template('comments.html',title = title, comment_form=form, pitchs=pitch)


@main.route('/category', methods=['GET', 'POST'])
def category():
    '''
    Function that validates the Pitch form
    '''
    form = PitchForm()

    if form.validate_on_submit():
        new_pitch = Pitch(actual_pitch=form.Pitch.data,category=form.Category.data, user_id=current_user.id)
        new_pitch.save_pitch()
        flash('successfully saved')
    pitch = Pitch.query.filter_by(category='product')
    
    pickuplines = Pitch.query.filter_by(category='pickuplines')
    return render_template('pitch.html',title = 'new_pitch', pitch_form=form, pitch=pitch,pickuplines=pickuplines)

    interview = Pitch.query.filter_by(category='interview')
    return render_template('pitch.html',title = 'new_pitch', pitch_form=form, pitch=pitch,interview=interview)

    promotion = Pitch.query.filter_by(category='promotion')
    return render_template('pitch.html',title = 'new_pitch', pitch_form=form, pitch=pitch,promotion=promotion)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))