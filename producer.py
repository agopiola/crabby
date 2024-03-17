import time
import random
import uuid
import json
from datetime import datetime
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
 

# generate a unique uuid for each payload
def create_uuid():
    return str(uuid.uuid4())

# get current datetime and return ISO 8601 as string
def current_date_time():
    today = datetime.now()
    timestamp=today.isoformat()

    return timestamp

# define random ranges for number of steps, pulse, calories
def health_figures(i):
    num_steps = random.randint(1000,10000)
    pulse = random.randint(55,130)
    total_calories = round(num_steps * .005)

    event_data = {
        "timestamp": current_date_time(),
        "num_steps": num_steps,
        "pulse": pulse,
        "total_calories": total_calories,
    }
    return event_data
    
## Create connection to Aiven Kafka
TOPIC_NAME = "aiven-iot-events"
producer = KafkaProducer(
    bootstrap_servers=f"kafka-demo-tonytest-9cb4.a.aivencloud.com:11855",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

# perform while loop in order to generate i number of messages
i=1
json_data = {}
while i <= 10:
    json_data = {
        "uuid": create_uuid().replace("'", chr(34)),
        "message": health_figures(i)
    }
    json_string = json.dumps(json_data)
    producer.send(TOPIC_NAME, json_string.encode('utf-8'))
    print(json.dumps(json_data))
    i+=1
    time.sleep(1)

producer.close()