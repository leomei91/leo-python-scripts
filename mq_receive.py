#! /bin/bash
# -*- coding: utf-8 -*-
#
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(exch, method, properties, body):
	print("Received {}".format(body.decode('utf-8')))

channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()

