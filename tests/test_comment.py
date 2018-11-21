
import unittest
from app.models import Comment,User
from app import db

class TestComment(unittest.TestCase):

    '''
    Test cases to check that a Comment object can be created, saved, and queried
    '''

    def setUp(self):
        self.user_sam = User(username = 'Sam',password = 'samsam', email = 'sam@gmail.com')
        self.new_comment = Comment(pitch_id=9,pitch_title='i love codes',comment='This pitch is dope',user = self.user_sam )


    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id,9)
        self.assertEquals(self.new_comment.pitch_title,'Review for movies')
        self.assertEquals(self.new_comment.comment,'Not a bad pitch')
        self.assertEquals(self.new_comment.user,self.user_sam)


    def test_save_comment(self):
        self.new_comment.save_review()
        self.assertTrue(len(Comment.query.all())>0)


    def test_get_comments_by_id(self):
        self.new_comment.save_review()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)