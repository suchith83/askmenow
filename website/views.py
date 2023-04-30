from flask import Blueprint,render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
from .models import Question, Category, Answer
from PIL import Image
from werkzeug.utils import secure_filename
import os


views = Blueprint('views', __name__)

# with open('path/to/image.png', 'rb') as f:
#     img_data = f.read()


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    answers = Answer.query.all()
    return render_template('home.html', user=current_user, answers=answers)


@views.route('/answer', methods=['GET', 'POST'])
@login_required
def answer():
    questions = Question.query.all()

    return render_template('answer.html', user=current_user, questions=questions)


@views.route('/category', methods=['GET', 'POST'])
@login_required
def category():
    categories = Category.query.all()
    questions = Question.query.all()
    return render_template('category.html', user=current_user, questions=questions)

@views.route('/category/<category>', methods=['GET', 'POST'])
@login_required
def category_answers(category):
    category = Category.query.filter_by(name=category).first()
    category_id = category.id
    questions = Question.query.filter_by(category_id=category_id).all()
    return render_template('category.html', user=current_user, questions=questions)


@views.route('/profile/<username>/questions/<int:question_id>', methods=['DELETE'])
@login_required
def delete_question(username, question_id):
    question = Question.query.filter_by(id=question_id, user=current_user).first()
    if question:
        db.session.delete(question)
        db.session.commit()
        flash('Your question has been deleted!', 'success')
    return jsonify({'success': True})




@views.route('/create-question', methods=['GET', 'POST'])
@login_required
def create_question():
    if request.method == 'POST':
        question = request.form.get('question')
        category = request.form.get('category')

        if len(question) < 1:
            flash('Question is too short.', category='error')
        else:
            category = Category.query.filter_by(name=category).first()
            if category:
                category_id = category.id
                new_question = Question(question=question, category_id=category_id, user_id=current_user.id)
                db.session.add(new_question)
                db.session.commit()
                flash('Question created!', category='success')
                return redirect(url_for('auth.show_questions', username=current_user.username))
            else:
                flash('Category does not exist.', category='error')
        return redirect(url_for('auth.show_questions', username=current_user.username))




ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@views.route('/<category>/<int:question_id>', methods=['GET', 'POST'])
@login_required
def question(category,question_id):
    question = Question.query.filter_by(id=question_id).first()
    category = Category.query.filter_by(name=category).first()
    from main import app
    if request.method == 'POST':

        answer = request.form.get('answer')
        file = request.files['photo']
        # print(file)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = None
        question_id = question_id
        question = Question.query.filter_by(id=question_id).first()
        new_answer = Answer(answer=answer, question_id=question_id, user_id=current_user.id, photo=filename)
        db.session.add(new_answer)
        db.session.commit()
        flash('Answer created!', category='success')
        return render_template('question.html', user=current_user, question=question, category=category)

    return render_template('question.html', user=current_user, question=question, category=category)


@views.route('/following', methods=['GET', 'POST'])
@login_required
def following():
    following = current_user.following

    return render_template('following_page.html', user=current_user, following=following)

@views.route('/profile/delete-profile-picture', methods=['POST'])
@login_required
def delete_profile_picture():
    if request.method == 'POST':
        user = current_user
        user.photo = 'default.jpeg'
        db.session.commit()
        return redirect('/profile/'+str(current_user.username))

@views.route('/profile/change-profile-picture', methods=['POST'])
@login_required
def change_profile_picture():
    from main import app
    if request.method == 'POST':
        file = request.files['photo']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            i = 1
        else:
            filename = current_user.photo
            i = 0
        current_user.photo = filename
        db.session.commit()
        if i == 1:  flash('Profile Photo Changed!', category='success')
        return redirect('/profile/'+str(current_user.username))
    # question = Question.query.filter_by(id=question_id).first()
    # category = Category.query.filter_by(name=category).first()
    # from main import app
    # if request.method == 'POST':

    #     answer = request.form.get('answer')
    #     file = request.files['photo']
    #     # print(file)
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # else:
        #     filename = None
    #     question_id = question_id
    #     question = Question.query.filter_by(id=question_id).first()
    #     new_answer = Answer(answer=answer, question_id=question_id, user_id=current_user.id, photo=filename)
    #     db.session.add(new_answer)
    #     db.session.commit()
    #     flash('Answer created!', category='success')
    #     return render_template('question.html', user=current_user, question=question, category=category)

    # return render_template('question.html', user=current_user, question=question, category=category)


@views.route('/edit-profile', methods=['POST'])
@login_required
def edit_profile():
    if request.method == "POST":
        current_user.username = request.form.get("username")
        current_user.email = request.form.get("email")
        current_user.about = request.form.get("about")
        db.session.commit()
    flash('Profile Changed Succesfully!', category='success')
    return redirect('/profile/'+current_user.username)

# @views.route('/cat')
# @login_required
# def cat():
#     newcategory = Category(name="Technology")
#     db.session.add(newcategory)
#     db.session.commit()
#     return redirect('/')