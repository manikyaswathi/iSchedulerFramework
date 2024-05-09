package com.springbootkafka.producer.services;

import org.apache.kafka.clients.admin.AdminClient;
import org.apache.kafka.clients.admin.NewTopic;
import org.apache.kafka.common.config.TopicConfig;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaAdmin;
import org.springframework.stereotype.Service;
import java.util.Map;
import java.util.concurrent.ExecutionException;
import java.util.HashMap;
import java.util.Collections;

/**
 * Service to create a topic
 */
@Service
public class CreateNewTopic {

    //Use the autoconfigured admin object
    //This can be manually configured
    @Autowired
    KafkaAdmin kafkaAdmin;

    /**
     * 
     * @param topic The name of the topic
     * @throws InterruptedException
     * @throws Exception
     */
    public void createTopic(String topic) throws InterruptedException, Exception {

        Map<String, String> topicConfig = new HashMap<>();
        topicConfig.put(TopicConfig.RETENTION_MS_CONFIG, String.valueOf(24 * 60 * 60 * 1000)); // 24 hours retention
        NewTopic newTopic = new NewTopic(topic, 1, (short) 1).configs(topicConfig);
        
        try (AdminClient adminClient = AdminClient.create(kafkaAdmin.getConfigurationProperties())) {
          adminClient.createTopics(Collections.singletonList(newTopic)).all().get();
        } catch(InterruptedException | ExecutionException exception) {
            throw new Exception("Could not create topic: "+exception);
        }
    }
}
