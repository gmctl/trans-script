# ˵��

```
��װ python3 python3-pip 
��װ nodejs `bash install_node.sh`
```


## ���� 
- `python3 run.py` ���ɡ�ע������޸� time.sleep ��ʱ�䣬�������Ϊ0�Ļ���Լ����465�������ˡ��ҵ�ǰ���õ�2����1000�������ܡ�
- ��̨���� `nohup python3 run.py`




# ʹ�ô����

# �������ط����
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