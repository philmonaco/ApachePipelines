import logging
import logging.config
from pykafka import KafkaClient

logging.config.fileConfig('conf/logging_config.ini')
logger = logging.getLogger(__name__)

class StreamDataProducer:
    def __init__(self, hosts, topic_name):
        self.client = KafkaClient(hosts=hosts)
        self.topic = self.client.topics[topic_name]
        self.producer = self.topic.get_producer()

    def produce_data(self, data):
        self.producer.produce(data.encode())
        logger.info('Data produced: %s', data)

    def close(self):
        self.producer.stop()
        logger.info('Producer stopped')


if __name__ == '__main__':
    # Configuration
    kafka_hosts = 'localhost:9092'
    kafka_topic = 'my_topic'

    # Create an instance of the BatchDataProducer
    producer = StreamDataProducer(kafka_hosts, kafka_topic)

    # Produce data
    data = 'This is a sample message'
    producer.produce_data(data)

    # Close the producer
    producer.close()