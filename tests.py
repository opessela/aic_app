import app
import unittest
import aic_api

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_correct_http_response(self):
        resp = self.app.get('/')
        self.assertEquals(resp.status_code, 200)

    def test_correct_content(self):
        resp = self.app.get('/')
        self.assertEquals(resp.data, 'Automated Infrastrucutre Configuration Framework v1.0')

    def test_correct_api_status_response(self):
        resp = self.app.get('/aic/api/v1.0/status')
        self.assertEquals(resp.status_code, 200)

    def test_correct_api_status_content(self):
        resp = self.app.get('/aic/api/v1.0/status')
        self.assertEquals(resp.data, '{\n  "Status": "Up"\n}\n')
#        self.assertEquals(resp.data, dict(Status='Up'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()