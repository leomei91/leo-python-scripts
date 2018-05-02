#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 获得信道
channel = connection.channel()
channel.exchange_declare(exchange='fanout', exchange_type='fanout')
# 发布消息
body = input("请输入消息：")
channel.basic_publish(exchange='fanout', routing_key='',
		body=body)
print("Sent {}.".format(body))

