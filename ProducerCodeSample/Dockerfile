FROM amazoncorretto:17-alpine-jdk
WORKDIR kafkaproducer
ENV PATH="$PATH:/kafkaproducer:/kafkaproducer/kafka:/kafkaproducer/kafka/bin"
COPY spring-kafka-producer/target/producer-0.0.1-SNAPSHOT.jar producer-0.0.1.jar
COPY kafka kafka
COPY launch_app.sh launch_app.sh
RUN chmod +x launch_app.sh
RUN chmod +x kafka
RUN chmod +x producer-0.0.1.jar
RUN chmod +x kafka/bin
RUN apk add --no-cache bash
ENTRYPOINT ["launch_app.sh"]
