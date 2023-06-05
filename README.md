# Space Flight Pipeline

This project implements a data pipeline for space flight data using Apache Kafka, Apache Spark, and Apache Airflow.

## Installation

### Prerequisites

- Python 3.9.* or higher
- Apache Kafka 2.8.0
- Apache Spark 3.1.2
- Apache Airflow 2.2.0

### Steps

1. Clone the repository:
```
git clone <repository_url>
cd space-flight-pipeline
```

2. Install the required Python packages:
```
pip install -r requirements.txt
pip install -e .
```

3. Install and configure Apache Kafka. Follow the Kafka documentation for installation instructions.

4. Install and configure Apache Spark. Follow the Spark documentation for installation instructions.

5. Install and configure Apache Airflow. Follow the Airflow documentation for installation instructions.

## Usage

### Starting the Kafka Broker

1. Open a new terminal and start the ZooKeeper server:
```
sh start_zookeeper.sh
```
2. Start the Kafka broker:
```
sh start_broker.sh
```
### Running the Batch Processing Pipeline

1. Run the Spark batch processing job:

TBD
### Running the Streaming Pipeline

1. Start the streaming data producer:

```
spaceflight batch-data-producer
```

### Scheduling the Pipeline with Apache Airflow

1. Start the Airflow webserver:

TBD

2. Start the Airflow scheduler:

TBD

3. Access the Airflow web interface in your browser at `http://localhost:8080`.

4. Configure and schedule the Airflow DAGs for batch processing and streaming.

## Configuration

- Modify the configuration files in the `config/` directory to customize the pipeline settings.
- Update the Kafka broker and topic settings in `config/kafka.properties`.
- Adjust the Spark job configurations in `config/spark.properties`.
- Configure the Airflow DAGs in `config/airflow/dags.py`.