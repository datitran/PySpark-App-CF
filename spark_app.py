import os
import sys
from flask import Flask, request, jsonify
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegressionModel
from pyspark.ml.linalg import Vectors

app = Flask(__name__)


def create_spark_connection():
    conf = SparkConf()
    conf.set("spark.executor.memory", "512mb")
    conf.set("spark.cores.max", "1")
    spark_session = SparkSession.builder.config(conf=conf).getOrCreate()
    spark_context = spark_session.sparkContext
    return spark_session, spark_context


def get_port():
    port = os.getenv("PORT")
    if type(port) == str:
        return port
    return 8080


@app.route("/")
def test_spark_context():
    _, spark_context = create_spark_connection()
    data = spark_context.parallelize(range(10))
    return str(data.collect())


@app.route("/predict", methods=["GET"])
def predict():
    """
    https://app.host/predict?value=0
    """
    value = int(request.args.get("value"))
    spark_session, _ = create_spark_connection()
    model_load = LinearRegressionModel.load("model")
    predict_df = spark_session.createDataFrame([(1, Vectors.dense(value))], ["index", "features"])

    predict_collected = model_load.transform(predict_df).collect()[0]

    features = predict_collected.features.values.tolist()
    prediction = predict_collected.prediction
    output = {"features": features, "prediction": prediction}
    return jsonify(output)


@app.route("/version")
def version():
    return sys.version


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=get_port())
