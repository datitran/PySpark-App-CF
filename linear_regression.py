import numpy as np
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.regression import LinearRegression


def generate_data():
    np.random.seed(1)  # set the seed
    x = np.arange(100)
    error = np.random.normal(0, size=(100,))
    y = 0.5 + 0.3 * x + error
    return x, y


def convert_to_df(spark_session, input_data):
    x, y = input_data
    data = pd.DataFrame([(i, j) for i, j in zip(x, y)], columns=["x", "y"])
    data_spark = spark_session.createDataFrame(data)
    df = spark_session.createDataFrame((data_spark
                                        .rdd
                                        .map(lambda row: (row[1], 0.5, Vectors.dense(row[0])))
                                        ), ["label", "weight", "features"])
    return df


def fit_model(df):
    lr = LinearRegression(maxIter=5, regParam=0.0, solver="normal", weightCol="weight")
    model = lr.fit(df)
    return model


def save_model(model):
    model.write().overwrite().save("model")


if __name__ == "__main__":
    spark_session = SparkSession.builder.getOrCreate()

    input_data = generate_data()
    df = convert_to_df(spark_session, input_data)
    model = fit_model(df)
    save_model(model)
