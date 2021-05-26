import pika
import time
import dbds

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.128.0.5'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
cim
def callback(ch, method, properties, body):
    db_response = dbds.insert_db(str(body.decode()))
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
