#!/usr/bin/env python
import pika
import time

credits = pika.PlainCredentials('admin', 'password')
params = pika.ConnectionParameters('35.190.163.110',5672,'/',credits)
connection = pika.BlockingConnection(parameters=params)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
