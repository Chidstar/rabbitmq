#!/usr/bin/env python
import pika
import sys

credits = pika.PlainCredentials('admin', 'password')
params = pika.ConnectionParameters('35.190.163.110',5672,'/',credits)
connection = pika.BlockingConnection(parameters=params)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()
