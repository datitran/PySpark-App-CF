import os
import sys
from flask import Flask, request
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression, LinearRegressionModel
from pyspark.ml.linalg import Vectors

app = Flask(__name__)
spark_session = SparkSession.builder.getOrCreate()
sc = spark_session.sparkContext


def get_port():
    port = os.getenv("PORT")
    if type(port) == str:
        return port
    return 8080


@app.route("/")
def test_spark_context():
    data = sc.parallelize(range(10))
    return str(data.collect())


@app.route("/predict")
def prediction():
    """
    http://uri_cfapps.pez.pivotal.io/predict?value=0
    """
    value = int(request.args.get("value"))
    model_load = LinearRegressionModel.load("model")
    predict_df = spark_session.createDataFrame([(1, Vectors.dense(value))], ["index", "features"])
    return str(model_load.transform(predict_df).collect()[0])


@app.route("/version")
def version():
    return sys.version


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=get_port())
