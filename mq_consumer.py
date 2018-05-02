#! /bin/bash
# -*- coding: utf-8 -*-
#
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task', durable=True)

def callback(exch, method, properties, body):
	print("Received {}".format(body.decode('utf-8')))
	time.sleep(10)
	print("等待结束")
	exch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1) # 保证一个消息执行完成，才去获取下一个消息
channel.basic_consume(callback, queue='task')
channel.start_consuming()

