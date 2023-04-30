# from main import app
# from website import db
# from website.models import User, Question, Answer, Category
# from flask import url_for
# from flask_login import current_user
# import unittest
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask.testing import FlaskClient
# from io import BytesIO

# class cicd(unittest.TestCase):

#     def test_login(self):
#         tester = app.test_client(self)
#         response = tester.get("/login")
#         statuscode = response.status_code
#         self.assertAlmostEqual(statuscode,200)

#     def test_login_success(self):
#         tester = app.test_client(self)
#         response = tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         self.assertEqual(response.status_code, 200)
#         with app.app_context():
#             user = User.query.filter_by(email='suchith@gmail.com').first()
#             self.assertEqual(response.request.path, '/')

#     def test_login_failure(self):
#         tester = app.test_client(self)
#         response = tester.post('/login', data=dict(email='suchith@gmail.com', password='wrongpwd'), follow_redirects=True)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b'Incorrect password, try again.', response.data)
#         self.assertEqual(response.request.path, '/login')
#         response = tester.post('/login', data=dict(email='cs1210568@iitd.ac.in', password='password123'), follow_redirects=True)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b'Email does not exist.', response.data)
#         self.assertEqual(response.request.path, '/login')

#     def test_signup(self):
#         tester = app.test_client(self)
#         response = tester.get("/signup")
#         statuscode = response.status_code
#         self.assertAlmostEqual(statuscode,200)

#     def test_signup_success(self):
#         tester = app.test_client(self)
#         response = tester.post('/signup', data=dict(email='hitesh@gmail.com', Username='testuser3', password1='hitesh@23', password2='hitesh@23'), follow_redirects=True)
#         self.assertEqual(response.status_code, 200)
#         with app.app_context():  # create an application context
#             user = User.query.filter_by(email='hitesh@gmail.com').first()
#             self.assertEqual(response.request.path, '/')
#             self.assertIsNotNone(user)
#             User.query.filter_by(email='hitesh@gmail.com').delete()
#             db.session.commit()

#     # def test_signup_failure(self):
#         # tester = app.test_client(self)
#         # response = tester.post('/signup', data=dict(email='suchith@gmail.com', Username='Hitesh', password1='hit', password2='hit'), follow_redirects=True)
#         # self.assertEqual(response.status_code, 200)
#         # self.assertIn(b'Email already exists', response.data)
#         # self.assertEqual(response.request.path, '/signup')
#         # response = tester.post('/signup', data=dict(email='test@gmail.com', Username='t', password1='pwd', password2='pwd'), follow_redirects=True)
#         # self.assertEqual(response.status_code, 200)
#         # self.assertIn(b'User name must be greater than 1 character', response.data)
#         # self.assertEqual(response.request.path, '/signup')
#         # response = tester.post('/signup', data=dict(email='test@gmail.com', Username='testuser', password1='pwd', password2='pwd'), follow_redirects=True)
#         # self.assertEqual(response.status_code, 200)
#         # self.assertIn(b'Password must be at least 7 characters', response.data)
#         # self.assertEqual(response.request.path, '/signup')
#         # response = tester.post('/signup', data=dict(email='suchith@gmail.com', Username='1234567', password1='password', password2='password'), follow_redirects=True)
#         # self.assertEqual(response.status_code, 200)
#         # self.assertIn(b'Email already exists', response.data)
#         # self.assertEqual(response.request.path, '/signup')
#         # response = tester.post('/signup', data=dict(email='user1@gmail.com', Username='user1', password='password', password2='password'), follow_redirects=True)
#         # self.assertEqual(response.status_code, 200)
#         # self.assertIn(b'Username already exists', response.data)
#         # self.assertEqual(response.request.path, '/signup')


#     def test_logout(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         response = tester.get('/logout')
#         statuscode = response.status_code
#         self.assertAlmostEqual(statuscode,302)
#         # self.assertEqual(response.request.path, '/logout')

#     def test_explorepage(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         response = tester.get('/category')
#         self.assertEqual(response.status_code, 200)
    
#     def test_categorypage(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         response = tester.get('/category/Music')
#         self.assertEqual(response.status_code, 200)

#     def test_answeraquepage(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         response = tester.get('/answer')
#         self.assertEqual(response.status_code, 200)        

#     def test_myprofile(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         with app.app_context():
#             user = User.query.filter_by(email='suchith@gmail.com').first()
#             username = user.username
#         response = tester.get('/profile/'+username)
#         self.assertEqual(response.status_code, 200)
#         response = tester.get('/profile/'+username+'/questions')
#         self.assertEqual(response.status_code, 200)
#         response = tester.get('/profile/'+username+'/questions/Sports')
#         self.assertEqual(response.status_code, 200)
#         response = tester.get('/profile/'+username+'/followers')
#         self.assertEqual(response.status_code, 200)
#         response = tester.get('/profile/'+username+'/following')
#         self.assertEqual(response.status_code, 200)

#     def test_createquestion(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         tester.get('/')
#         response = tester.post("/create-question",data=dict(question="What is your name?",category="Technology"), follow_redirects=True)
#         statuscode = response.status_code
#         self.assertEqual(statuscode,200)
#         self.assertEqual(response.request.path, "/profile/suchith/questions")

#     def test_deletequestion(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         with app.app_context():
#             user = User.query.filter_by(email='suchith@gmail.com').first()
#             username = user.username
#             question = Question.query.filter_by(question="What is your name?").first()
#             if question != None:
#                 queid = question.id
#                 url = '/profile/'+ str(username) +'/questions/' + str(queid)
#                 response = tester.delete(url, follow_redirects=True)
#                 self.assertEqual(response.status_code, 200)

#     def test_questionpage(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         response = tester.get("/Music/6")
#         self.assertEqual(response.status_code,200)

#     def test_addanswer(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         with open('./website/static/images/naruto.jpeg', 'rb') as f:
#             response = tester.post("/Music/6",data=dict(answer="Yes, it was.",photo=(BytesIO(f.read()), './website/static/images/naruto.jpeg')),follow_redirects=True)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.request.path, "/Music/6")

#     def test_deleteanswer(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         with app.app_context():
#             user = User.query.filter_by(email='suchith@gmail.com').first()
#             userid = user.id
#             username = user.username
#             answer = Answer.query.filter_by(answer='Yes, it was.').first()
#             if (answer!=None):
#                 answerid = answer.id
#                 answererid = answer.user_id
#                 if answererid == userid:
#                     url = '/profile/'+str(userid)+'/answers/'+str(answerid)
#                     response = tester.delete(url, follow_redirects=True)
#                     self.assertEqual(response.status_code, 500)
#                     # self.assertEqual(response.request.path, '/profile/'+username)

#     def test_follow(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         with app.app_context():
#             user = User.query.filter_by(email='suchith@gmail.com').first()
#             username = user.username
#             otheruser = User.query.filter_by(email='charan@gmail.com').first()
#             otheruserid = otheruser.id
#             otherusername = otheruser.username
#             url = '/follow/'+str(otheruserid)
#             response = tester.post(url, follow_redirects=True)
#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response.request.path, "/profile/"+otherusername+"/following")

#     def test_unfollow(self):
#         tester = app.test_client(self)
#         tester.post('/login', data=dict(email='suchith@gmail.com', password='1234567'), follow_redirects=True)
#         with app.app_context():
#             user = User.query.filter_by(email='suchith@gmail.com').first()
#             username = user.username
#             otheruser = User.query.filter_by(email='charan@gmail.com').first()
#             otheruserid = otheruser.id
#             otherusername = otheruser.username
#             url = '/unfollow/'+str(otheruserid)
#             response = tester.post(url, follow_redirects=True)
#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response.request.path, "/profile/"+username+"/following")

# #     def test_home_with_authenticated_user(self):
# #         tester = app.test_client(self)
# #         tester.post('/', data=dict(email='u1@gmail.com', password='user123'), follow_redirects=True)
# #         response = tester.get('/home/1')
# #         self.assertEqual(response.status_code, 200)
# #     def test_home_with_unauthenticated_user(self):
# #         tester = app.test_client(self)
# #         response = tester.get('/home/1')
# #         self.assertEqual(response.status_code, 401)
# #     def test_view_own_profile(self):
# #         tester = app.test_client(self)
# #         tester.post('/', data=dict(email='u1@gmail.com', password='user123'), follow_redirects=True)
# #         response = tester.get('/profile/1')
# #         self.assertEqual(response.status_code, 200)
# #         self.assertIn(b'user1', response.data)    
# #     def test_view_other_profile(self):
# #         tester = app.test_client(self)
# #         user2 = User(username='testuser2', email='testuser2@example.com',password_hash = generate_password_hash('password'))
# #         with app.app_context():
# #          db.session.add(user2)
# #          tester.post('/', data=dict(email='u1@gmail.com', password='user123'), follow_redirects=True)
# #          response = tester.get('/profile/2')
# #          self.assertEqual(response.status_code, 200)
# #          self.assertIn(b'testuser2', response.data)  
# #     def test_view_unautorised(self):
# #         tester = app.test_client(self)
# #         response = tester.get('/profile/1')
# #         self.assertEqual(response.status_code, 401)
# #     def test_profile_update(self):
# #         tester = app.test_client(self)
# #         tester.post('/', data=dict(email='u1@gmail.com', password='user123'), follow_redirects=True)
# #         response = tester.post('/profile/1',data= {'form_type': 'profile_update', 'username': 'user1', 'email': 'u1@gmail.com','password':'user123','bio':'artist','profession':'photography'})
# #         self.assertEqual(response.status_code, 200)
# #         self.assertIn(b'Profile updated successfully', response.data)
# #     def test_profile_photo_update(self):
# #         tester = app.test_client(self)
# #         tester.post('/', data=dict(email='u1@gmail.com', password='user123'), follow_redirects=True)
# #         with open('test.jpg', 'rb') as f:
# #             response = tester.post('/profile/1', data={'form_type':'photo_update','profile_pic': (BytesIO(f.read()), 'test.jpg')})
# #         self.assertEqual(response.status_code, 200)
# #         self.assertIn(b'Profile picture updated successfully', response.data)
# #         with app.app_context():
# #             updated_user = User.query.filter_by(id=1).first()
# #             self.assertNotEqual(updated_user.profile_pic, 'public/unknown.jpg')
# #     def test_profile_pic_delete(self):
# #         tester = app.test_client(self)
# #         tester.post('/', data=dict(email='u1@gmail.com', password='user123'), follow_redirects=True)
# #         response = tester.post('/profile/1', data=dict(form_type='photo_update', delete_profile_pic='yes'))
# #         self.assertEqual(response.status_code, 200)
# #         self.assertIn(b'Profile picture deleted successfully', response.data)
# #         with app.app_context():
# #             updated_user = User.query.filter_by(id=1).first()
# #             self.assertEqual(updated_user.profile_pic, 'public/unknown.png')
# #     def test_followers(self):
# #         tester = app.test_client(self)
# #         tester.post('/', data=dict(email='u1@gmail.com', password='user123'), follow_redirects=True)
# #         response = tester.get('/followers/1')
# #         self.assertEqual(response.status_code, 200)
# #         self.assertIn(b'user1', response.data)
# #     def test_followers_others(self):
# #         tester = app.test_client(self)
# #         user2 = User(username='testuser2', email='testuser2@example.com',password_hash = generate_password_hash('password'))
# #         with app.app_context():
# #             db.session.add(user2)
# #             tester.post('/', data=dict(email='u1@gmail.com', password='user123'), follow_redirects=True)
# #             response = tester.get('/followers/2')
# #             self.assertEqual(response.status_code, 200)
# #             self.assertIn(b'testuser2', response.data)
# #     def test_following(self):
# #         tester = app.test_client(self)
# #         tester.post('/', data=dict(email='u1@gmail.com', password='user123'), follow_redirects=True)
# #         response = tester.get('/following/1')
# #         self.assertEqual(response.status_code, 200)
# #         self.assertIn(b'user1', response.data)
# #     def test_following_others(self):
# #         tester = app.test_client(self)
# #         user2 = User(username='testuser2', email='testuser2@example.com',password_hash = generate_password_hash('password'))
# #         with app.app_context():
# #             db.session.add(user2)
# #             tester.post('/', data=dict(email='u1@gmail.com', password='user123'), follow_redirects=True)
# #             response = tester.get('/following/2')
# #             self.assertEqual(response.status_code, 200)
# #             self.assertIn(b'testuser2', response.data)
    
        
    
       
      

# # if __name__ == "__main__" :
# #     unittest.main()
    