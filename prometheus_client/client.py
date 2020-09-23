#!/usr/bin/python
# -*- coding: UTF-8 -*-

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
registry = CollectorRegistry()
g = Gauge('ping', 'max response time',['dst_ip','city'], registry=registry) #Guage(metric_name,HELP,labels_name,registry=registry)
g.labels('192.168.1.10','shenzhen').set(42.2) #set设定值
g.labels('192.168.1.11','shenzhen').dec(2)  #dec递减2
g.labels('192.168.1.12','shenzhen').inc()  #inc递增，默认增1
push_to_gateway('10.217.61.103:9091', job='ping_status', registry=registry)