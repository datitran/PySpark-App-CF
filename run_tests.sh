#!/bin/bash

SPARK_URL=http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
SPARK_FILENAME=spark-2.1.0-bin-hadoop2.7.tgz

set -ex

apt-get update && \
    apt-get -y install wget curl software-properties-common bzip2 && \
    # install openjdk
    add-apt-repository -y ppa:openjdk-r/ppa && \
    apt-get update && \
    apt-get -y install openjdk-8-jdk

echo "Install Miniconda"
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.1.11-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p /home/conda
    rm ~/miniconda.sh
    export PATH="/home/conda/bin:$PATH"
    conda install -y nose numpy pandas

# Install Spark
echo "Install Spark"
    curl $SPARK_URL > $HOME/$SPARK_FILENAME
    tar -xzf $HOME/$SPARK_FILENAME -C $HOME/
    export SPARK_HOME="$HOME/spark-2.1.0-bin-hadoop2.7/"

nosetests -vs pyspark-app-ci/tests/test_linear_regression.py

# show folders
find .

exit 0