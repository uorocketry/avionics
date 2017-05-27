import sensor_observer
from threading import Timer
import sensor_producer

paul = sensor_observer.subscriber("paul")

producer = sensor_observer.publisher()
producer.register(paul)

def distribute():
    Timer(0.2, distribute).start()
    producer.dispatch(sensor_producer.poll_sensors())


distribute()
