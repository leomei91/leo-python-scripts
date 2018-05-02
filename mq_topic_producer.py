#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 获得信道
channel = connection.channel()
channel.exchange_declare(exchange='topic', exchange_type='topic')
# 发布消息
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'info'
body = input("请输入消息：")
channel.basic_publish(exchange='topic', routing_key=routing_key,
		body=body)
print("Sent {}.".format(body))

