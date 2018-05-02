#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 获得信道
channel = connection.channel()
# 声明队列，如果没有就创建
channel.queue_declare(queue='task', durable=True) # 设置durable=True保证队列持久化
# 发布消息
body = input("请输入消息：")
channel.basic_publish(exchange='', routing_key='task',
		body=body, properties=pika.BasicProperties(
			delivery_mode=2, # 设置delivery_mode=2，保证消息持久化
		))
print("Sent {}.".format(body))

