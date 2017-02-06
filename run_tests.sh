#!/bin/bash

set -ex

SPARK_CONFIG_FILE="pyspark-app-ci/spark_runtime.txt"
SPARK_URL=http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
SPARK_FILENAME=spark-2.1.0-bin-hadoop2.7.tgz
SPARK_FOLDER=$HOME/spark

main () {
    install_jdk

    install_conda

    install_spark

    nosetests -vs pyspark-app-ci/tests/test_linear_regression.py

    exit 0
}

get_setting() {
    key=$1

    if [ -e "$SPARK_CONFIG_FILE" ]
    then
        value=$(grep -ie "^$key" $SPARK_CONFIG_FILE | tail -n1 | cut -f 2 -d= | grep -oE "\S+")
        if [ "$value" != "" ]
        then
            echo $value
            return 0
        fi
    fi

    echo $(eval "echo \$$key")
}

install_jdk() {
echo "Install OpenJDK"
apt-get update && \
    apt-get -y install wget curl software-properties-common bzip2 && \
    # install openjdk
    add-apt-repository -y ppa:openjdk-r/ppa && \
    apt-get update && \
    apt-get -y install openjdk-8-jdk
}

install_conda() {
echo "Install Miniconda"
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.1.11-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p /home/conda
    rm ~/miniconda.sh
    export PATH="/home/conda/bin:$PATH"
    conda install -y nose numpy pandas
}

install_spark() {
echo "Install Spark"
    mkdir $SPARK_FOLDER
    SPARK_URL=$(get_setting SPARK_URL)
    SPARK_FILENAME=$(get_setting SPARK_FILENAME)
    curl $SPARK_URL > $HOME/$SPARK_FILENAME
    tar -xzf $HOME/$SPARK_FILENAME --directory $SPARK_FOLDER --strip-components 1
    export SPARK_HOME="$SPARK_FOLDER"
}

main $*