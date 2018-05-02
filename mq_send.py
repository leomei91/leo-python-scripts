#! /bin/bash
# -*- coding: utf-8 -*-
#
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 获得信道
channel = connection.channel()
# 声明队列，如果没有就创建
channel.queue_declare(queue='hello')
# 发布消息
body = input("请输入消息：")
channel.basic_publish(exchange='', routing_key='hello',
		body=body)
print("Sent {}.".format(body))
connection.close()

