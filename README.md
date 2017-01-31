# PySpark-App-CF

A simple example which uses the [PySpark buildpack](https://github.com/andreasf/pyspark-buildpack) to deploy an [Apache Spark](http://spark.apache.org/) application, particularly using its Python API, on Cloud Foundry.

## Getting Started

- Use `cf push` to deploy the application

## Dependencies
- [Apache Spark 2.1.0](http://spark.apache.org/)
- OpenJDK 1.8.0_91
- [Anaconda](https://www.continuum.io/downloads) Python 3.5.0
- Python conda environment (install with `conda env create --file environment.yml`)

## Copyright

See [LICENSE](LICENSE) for details.
Copyright (c) 2017 [Dat Tran](http://www.dat-tran.com/), [Andreas Fleig](https://github.com/andreasf).
