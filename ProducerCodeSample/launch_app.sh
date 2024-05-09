#!/bin/bash

nohup kafka/bin/zookeeper-server-start.sh kafka/config/zookeeper.properties &
nohup kafka/bin/kafka-server-start.sh kafka/config/server.properties &
java -jar ./producer-0.0.1.jar