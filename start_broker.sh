#!/bin/bash
# Update the paths based on your directory structure
cd ..
KAFKA_HOME="kafka-3.4.0-src"

# Start Kafka broker
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties