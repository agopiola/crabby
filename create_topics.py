from kafka.admin import KafkaAdminClient, NewTopic

## Create connection to Aiven Kafka for topic generation
admin_client = KafkaAdminClient(
    bootstrap_servers="kafka-demo-tonytest-9cb4.a.aivencloud.com:11855", 
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

topic_list = []
# Commenting aiven_iot_events topic.  It will be the initial topic created when deploying Aiven Kafka service
#topic_list.append(NewTopic(name="aiven-iot-events", num_partitions=1, replication_factor=2,))
topic_list.append(NewTopic(name="aiven-iot-even", num_partitions=1, replication_factor=2))
topic_list.append(NewTopic(name="aiven-iot-odd", num_partitions=1, replication_factor=2))
admin_client.create_topics(new_topics=topic_list, validate_only=False)