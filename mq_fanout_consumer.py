#! /bin/bash
# -*- coding: utf-8 -*-
#
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='fanout', exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
channel.queue_bind(exchange='fanout', queue=result.method.queue)

def callback(exch, method, properties, body):
	print("Received {}".format(body.decode('utf-8')))

channel.basic_consume(callback, queue=result.method.queue, no_ack=True)
channel.start_consuming()

