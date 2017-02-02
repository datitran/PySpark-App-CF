from . import basetests
import linear_regression


class LinearRegressionTraining(basetests.BaseTestClass):
    def setUp(self):
        self.input_data = linear_regression.generate_data()
        self.df = linear_regression.convert_to_df(self.spark_session, self.input_data)
        self.model = linear_regression.fit_model(self.df)

    def test_generate_data_x(self):
        self.assertEqual(sum(linear_regression.generate_data()[0]), 4950)

    def test_generate_data_y(self):
        self.assertAlmostEqual(sum(linear_regression.generate_data()[1]), 1541.0582852)

    def test_convert_to_df_columns(self):
        self.assertEqual(self.df.columns, ['label', 'weight', 'features'])

    def test_convert_to_df_count(self):
        self.assertEqual(self.df.count(), 100)

    def test_fit_model_coefficients(self):
        self.assertAlmostEqual(self.model.coefficients.values[0], 0.303341865)

    def test_fit_model_intercept(self):
        self.assertAlmostEqual(self.model.intercept, 0.39516052)
