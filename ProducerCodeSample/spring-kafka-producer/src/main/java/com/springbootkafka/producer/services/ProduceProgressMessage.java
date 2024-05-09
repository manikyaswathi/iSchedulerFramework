package com.springbootkafka.producer.services;

import java.util.concurrent.CompletableFuture;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.SendResult;
import org.springframework.stereotype.Service;
import com.springbootkafka.producer.types.ProgressMessage;

/**
 * Service to produce a message to progress-messages topic
 */
@Service
public class ProduceProgressMessage {
    @Autowired
    private KafkaTemplate<String, Object> template;

    /**
     * 
     * @param topic Topic to which the message needs to be pushed
     * @param message   The message
     */
    public void sendToProgressMessagesTopic(ProgressMessage progressMessage) {

        CompletableFuture<SendResult<String, Object>> futureMessage = template.send("progress-messages", progressMessage);
        futureMessage.whenComplete((result, exception)->{
            if(exception == null) {
                System.out.println("sent progress message successfully");
                return;
            }
            System.out.println("failed to send progress message");
        });
    }
}
