# PySpark-App-CF

A simple example which uses the [PySpark buildpack](https://github.com/andreasf/pyspark-buildpack) to deploy an [Apache Spark](http://spark.apache.org/) application, particularly using its Python API, on Cloud Foundry.

### Getting Started

- Use `cf push` to deploy the application

### Testing
A local `apache-spark` instance and `nosetests` need to be installed before running the tests. For more information see [here](https://github.com/datitran/spark-tdd-example).

- Run tests with: `nosetests -vs tests/`

### CI/CD
[Concourse](https://concourse.ci/) is used as our CI tool due to its seamless integration with Cloud Foundry. The fastest way to use Concourse is with [Vagrant](https://www.vagrantup.com/):
 
- Install Vagrant and run `vagrant init concourse/lite && vagrant up`
- Connect to the CI: `fly -t pyspark-app-cf login -c http://192.168.100.4:8080`
- Fill in the credential details in `credentials.yml.example` and rename the file to `credentials.yml`
- Register the pipeline: `fly -t pyspark-app-cf set-pipeline -p pyspark-app-ci -c pipeline.yml -l credentials.yml`
- Unpause the pipeline: `fly -t pyspark-app-cf unpause-pipeline -p pyspark-app-ci`

## Dependencies
- [Apache Spark 2.1.0](http://spark.apache.org/)
- OpenJDK 1.8.0_91
- [Anaconda](https://www.continuum.io/downloads) Python 3.5.0
- Python conda environment (install with `conda env create --file environment.yml`)

## Copyright

See [LICENSE](LICENSE) for details.
Copyright (c) 2017 [Dat Tran](http://www.dat-tran.com/), [Andreas Fleig](https://github.com/andreasf).
