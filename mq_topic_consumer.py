#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic', exchange_type='topic')
result = channel.queue_declare(exclusive=True)
binding_keys = sys.argv[1:]
for k in binding_keys:
	channel.queue_bind(exchange='topic', queue=result.method.queue, 
			routing_key=k)

def callback(exch, method, properties, body):
	print("Received {}".format(body.decode('utf-8')))

channel.basic_consume(callback, queue=result.method.queue, no_ack=True)
channel.start_consuming()

