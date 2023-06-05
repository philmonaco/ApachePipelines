import click
from .online.kafka_producer.streaming_data_producer import StreamDataProducer


@click.group()
def cli():
    pass

@cli.command()
@click.option('--hosts', default='localhost:9092', help='Kafka bootstrap servers')
@click.option('--topic', default='my_topic', help='Kafka topic name')
def stream_data_producer(hosts, topic):
    producer = StreamDataProducer(hosts, topic)
    producer.produce_data('This is a sample message')
    producer.close()

if __name__ == '__main__':
    cli()