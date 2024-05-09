package com.springbootkafka.producer.types;

public class CreateTopic {
    String topic;

    public void setTopic(String topic) {
        this.topic = topic;
    }

    public String getTopic() {
        return this.topic;
    }
}
