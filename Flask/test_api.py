# test_app.py

from main import app
import unittest


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_1(self):
        response = self.app.get('/login/pdeb/2433')
        self.assertEqual(response.status_code,200)
        
    def test_2(self):
        response = self.app.get('/api/retrive')
        self.assertEqual(response.status_code,200)

        
    def test_3(self):
        response = self.app.get('/api/insert/Id/1223456/native_english_speaker/Soham/course_instructor/Rounak/course/Eng/semester/sem2/class_size/200/performance_score/300')
        self.assertEqual(response.status_code,200)

    def test_4(self):
        response = self.app.get('/api/update/1223456/native_english_speaker/rounak454')
        self.assertEqual(response.status_code,200)

    def test_5(self):
        response = self.app.get('/api/delete/1223456')
        self.assertEqual(response.status_code,200)
    
        
if __name__=='__main__':
    unittest.main()
     
