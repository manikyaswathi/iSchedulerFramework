

# Intelligence Plane Spring Kafka message system

Spring Boot + Kafka project to demonstrate intelligence plane communication.

## Setup

 1. Clone the repository:<br/><br/> `git clone https://github.com/sandeepSbudhya/producer.git`<br/><br/>
 2. This project requires **Java 17** (openjdk version "17.0.10"), **docker version 25.0.3** and **Apache Maven 3.8.7**. Install these packages using any package manager.<br/><br/>Sample command for Arch Linux<br/><br/>`sudo pacman -Syu maven docker jdk17-openjdk`<br/><br/>
 3. Download and extract Apache kafka Version 3.7.0 binaries from: <br/><br/>https://downloads.apache.org/kafka/3.7.0/kafka_2.12-3.7.0.tgz<br/><br/> and extract it to a folder called **"kafka**" under the **root** folder.<br/><br/>Change the **kafka/config/server.properties** and **kafka/config/zookeeper.properties** to appropriate values (it runs on localhost by default). <br/><br/>The folder structure should look as follows:<br/><br/>
├── kafka<br/>
│   ├── bin<br/>
│   │   └── windows<br/>
│   ├── config<br/>
│   │   └── kraft<br/>
│   ├── libs<br/>
│   ├── licenses<br/>
│   ├── logs<br/>
│   └── site-docs<br/>
├── spring-kafka-producer<br/>
│   ├── src<br/>
│   │   ├── main<br/>
│   │   │   ├── java<br/>
│   │   │   │   └── com<br/>
│   │   │   │       └── springbootkafka<br/>
│   │   │   │           └── producer<br/>
│   │   │   │               ├── controllers<br/>
│   │   │   │               ├── services<br/>
│   │   │   │               └── types<br/>
│   │   │   └── resources<br/>
│   │   └── test<br/>
│   │       └── java<br/>
│   │           └── com<br/>
│   │               └── springbootkafka<br/>
│   │                   └── producer<br/>
│   └── wrapper<br/>
└── target<br/>
    ├── classes<br/>
    ├── generated-sources<br/>
    │   └── annotations<br/>
    ├── generated-test-sources<br/>
    │   └── test-annotations<br/>
    └── test-classes<br/>
    
 Change the kafka broker url in the appropriate lines in: <br/><br/> **root**/spring-kafka-producer/src/main/resources/application.yml<br/><br/>and<br/><br/>**root**/spring-kafka-producer/src/main/java/com/springbootkafka/producer/services/KafkaAdminConfig<br/><br/>
 4. From **root** directory change directory to **"spring-kafka-producer"**:<br/><br/>`cd spring-kafka-producer`<br/><br/>and run:<br/><br/>`mvn clean package`<br/><br/>This will generate a jar package in the **target** tolder.<br/><br/>
 5. From the **root** directory run<br/>`sudo docker build -t producer:latest`<br/>to build a **container image** of the app.<br/><br/>
 6. From the **root** directory run:<br/><br/>`sudo docker run --rm --net=host -t producer:latest`<br/><br/>This will **run** the containerized application locally.<br/><br/>
## APIs available
### Ports (when running on localhost)
Ports exposed when the containerized application is running on localhost:
http://localhost:8080 This is the port that the spring boot applications controllers receives requests on.
http://localhost:9092 This is the port for the Apache Kafka broker.
http://localhost:2181 This is the port for Zookeeper.
### Endpoints (when running on localhost)
http://localhost:8080/create-topic<br/>

 7. Send a **POST** message to  this endpoint  with json body:<br/>{<br/>&emsp;"topic":"performance-messages"<br/>}<br/>To create the performance message topic<br/>with json body:<br/>
{<br/>&emsp;"topic":"progress-messages"<br/>}<br/>To create the progress message topic<br/>with json body:<br/>{<br/>&emsp;"topic":"utilization-messages"<br/>}<br/>to create utilization messages topic.<br/>

8. Send **POST** message to the following urls with json bodies similar to the sample to push a message into the respective topics in kafka.<br/>http://localhost:8080/producemessage/performance<br/>{<br/>&emsp;"accuracy"  :  0.579,<br/>&emsp;"fmeasure"  :  0.67,<br/>&emsp;"precision"  :  0.55,<br/>&emsp;"recall"  :  0.67,<br/>&emsp;"jobId"  :  "1"<br/>}<br/>
http://localhost:8080/producemessage/progress<br/>{<br/>&emsp;"epochsCompleted"  :  1,<br/>&emsp;"totalEpochs"  :  2,<br/>&emsp;"days"  :  1,<br/>&emsp;"hours"  :  2,<br/>&emsp;"minutes"  :  3,<br/>&emsp;"jobId"  :  1<br/>}<br/><br/>
http://localhost:8080/producemessage/cpu-mem-utilization<br/>
{<br/>&emsp;"cpu":{<br/>&emsp;&emsp;"us":11.2,<br/>&emsp;&emsp;"sy":3.4,<br/>&emsp;&emsp;"ni":0.0,<br/>&emsp;&emsp;"id":83.1,<br/>&emsp;&emsp;"wa":0.0,<br/>&emsp;&emsp;"hi":1.1,<br/>&emsp;&emsp;"si":1.1,<br/>&emsp;&emsp;"st":0.0<br/>&emsp;},<br/>&emsp;"memory":{<br/>&emsp;&emsp;"total":7730.8,<br/>&emsp;&emsp;"free":1413.2,<br/>&emsp;&emsp;"used":4211.2,<br/>&emsp;&emsp;"cache":3064.8<br/>&emsp;},<br/>&emsp;"swap":{<br/>&emsp;&emsp;"total":9011.2,<br/>&emsp;&emsp;"free":7923.9,<br/>&emsp;&emsp;"used":1087.2,<br/>&emsp;&emsp;"avail":3519.5<br/>&emsp;},<br/>&emsp;"jobId":"someTapisJobID"<br/>}<br/>
