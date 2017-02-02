import json
from . import basetests
from spark_app import app


class SparkApp(basetests.BaseTestClass):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_main_status_code(self):
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)

    def test_main_data(self):
        result = self.app.get("/")
        self.assertEqual(result.data.decode("UTF-8"), "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")

    def test_predict_status_code(self):
        result = self.app.get("/predict")
        self.assertEqual(result.status_code, 500)

    def test_predict_value_zero(self):
        output = '''
        {
          "features": [
            0.0
          ],
          "prediction": 0.3951605206669529
        }
        '''
        result = self.app.get("/predict?value=0")
        self.assertEqual(json.loads(result.data.decode("UTF-8")), json.loads(output))

    def test_predict_value_large(self):
        output = '''
        {
          "features": [
            1000.0
          ],
          "prediction": 303.7370258016517
        }
        '''
        result = self.app.get("/predict?value=1000")
        self.assertEqual(json.loads(result.data.decode("UTF-8")), json.loads(output))

    def test_predict_value_negative(self):
        output = '''
        {
          "features": [
            -10.0
          ],
          "prediction": -2.638258132142895
        }
        '''
        result = self.app.get("/predict?value=-10")
        self.assertEqual(json.loads(result.data.decode("UTF-8")), json.loads(output))

    def test_predict_value_invalid(self):
        result = self.app.get("/predict?value=abc")
        self.assertEqual(result.status_code, 500)
