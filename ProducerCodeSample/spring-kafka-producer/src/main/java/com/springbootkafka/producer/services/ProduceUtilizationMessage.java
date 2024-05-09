package com.springbootkafka.producer.services;

import java.util.concurrent.CompletableFuture;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.SendResult;
import org.springframework.stereotype.Service;
import com.springbootkafka.producer.types.UtilizationMessage;

/**
 * Service to produce a message to utilization-messages topic
 */
@Service
public class ProduceUtilizationMessage {
    @Autowired
    private KafkaTemplate<String, Object> template;

    /**
     * 
     * @param topic Topic to which the message needs to be pushed
     * @param message   The message
     */
    public void sendToUtilizationMessagesTopic(UtilizationMessage utilizationMessage) {

        CompletableFuture<SendResult<String, Object>> futureMessage = template.send("utilization-messages", utilizationMessage);
        futureMessage.whenComplete((result, exception)->{
            if(exception == null) {
                System.out.println("sent utilization message successfully");
                return;
            }
            System.out.println("failed to send utilzation message");
        });
    }
}
