# Update the paths based on your directory structure
cd ..
KAFKA_HOME="kafka-3.4.0-src"

# Start ZooKeeper
$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties