# Aiven Homework
Aiven repo for the technical interview

### Assignment
Create a short tutorial which has to be 10 minutes or less leveraging Aiven for Kafka and Aiven for Flink.  My tutorial is on Youtube and here is the link: [Aiven Homework](https://youtu.be/EhROABt6zww). In addition to this it was suggested to deploy InfluxDB anf Grafana to display observability and monitoring metrics.  I could not find any service within Aiven console and when I submitted a support case, they said it is <u>no longer<u> supported.  I decided to use the PosgreSQL along with the Grafana service to create dashboards.

- Aiven for Kafka Service
    - Create a Kafka service within Aiven.
    - Write a Kafka producer that generates valid JSON.  I chose python.
    - My python code, when executed, creates the topics.
    - I also manually created topics within the Aiven console.
    - I chose not to autocreate topics simply because it was not the recommended best practive at my previous organization.

- Aiven for Flink Service.
    - Create Aiven Flink service.
    - Create integration with Kafka service and Flink.
    - Create a source and two sink tables.
    - Create a source and two source tables created within the Aiven console.
    - Using modulo 2, determine if total_calories is even or odd.
    - Bifurcate / Spit the events based upon the modulo calculation into the two separate sink tables.

- Posgres Service
    - Within the Kafka service, create a PosgreSQL integration service in order to consume metrics.

- Grafana 
    - Once Posgres is deployed, create a grafana service.
    - Used canned grafana dashboards to display metrics






**InfluxDB was not an option so I had to resort to using PostgrenDB
Additionally I was attempting to use InfluxDB as suggested in the assignment though support mentioned it was no logner supported.  My alternative 

