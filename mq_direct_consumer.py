#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct', exchange_type='direct')
result = channel.queue_declare(exclusive=True)
severities = sys.argv[1:]
for s in  severities:
	channel.queue_bind(exchange='direct', queue=result.method.queue, 
			routing_key=s)

def callback(exch, method, properties, body):
	print("Received {}".format(body.decode('utf-8')))

channel.basic_consume(callback, queue=result.method.queue, no_ack=True)
channel.start_consuming()

