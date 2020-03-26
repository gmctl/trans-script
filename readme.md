# 说明

```
安装 python3 python3-pip 
安装 nodejs `bash install_node.sh`
```


## 运行 
- `python3 run.py` 即可。注意可以修改 time.sleep 的时间，如果设置为0的话大约翻译465条被封了。我当前设置的2到了1000条还在跑。
- 后台运行 `nohup python3 run.py`




# 使用代理池

# 部署代理池服务端
> 

```
version: "2"

services:
   proxy_pool:
      container_name: proxy_pool
      restart: always
      image: 'registry.cn-shenzhen.aliyuncs.com/actanble/proxy_pool'
      ports:
        - "5010:5010"
      volumes:
        - /etc/localtime:/etc/localtime:ro
      environment:
        - db_type=REDIS
        - db_port=6379
        - db_password=sqsjywl123
        - db_host=192.168.112.79
      networks:
         customize_net:
           ipv4_address: 192.168.112.110

   redis:
     container_name: redis
     image: 'registry.cn-hangzhou.aliyuncs.com/xxzhang/redis:4.0.9'
     volumes:
       - /srv/docker/redis_data3:/var/lib/redis
       - /etc/localtime:/etc/localtime:ro
     restart: always
     expose:
       - 6379
     environment:
       - REDIS_PASSWORD=sqsjywl123
     networks:
       customize_net:
         ipv4_address: 192.168.112.79

networks:
  customize_net:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 192.168.112.0/24
```