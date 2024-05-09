package com.springbootkafka.producer.controllers;

import org.springframework.web.bind.annotation.RestController;
import com.springbootkafka.producer.services.CreateNewTopic;
import com.springbootkafka.producer.types.CreateTopic;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;


/**
 * Controller to process requests for creating a topic
 */
@RestController
@RequestMapping("/")
public class CreateTopicController {

    @Autowired
    private CreateNewTopic createNewTopic;

    /**
     * 
     * @param createTopicMessage type of object to convert the incoming JSON to a java object
     * @return Returns an HTTP response with a message (success or failure)
     * @throws InterruptedException
     * @throws Exception
     */
    @PostMapping("/create-topic")
    public ResponseEntity<String> postMethodName(@RequestBody CreateTopic createTopicMessage) throws InterruptedException, Exception{
        try{
            createNewTopic.createTopic(createTopicMessage.getTopic());
            return ResponseEntity.ok("successfully created topic: "+createTopicMessage.getTopic());
        } catch(Exception exception) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }
    
}
