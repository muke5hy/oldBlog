Title: Installing and configuring ELK Stack
Date: 2015-11-18 00:10:12 +05:30
Slug: installing-and-configuring-ELK-stack
Authors: Mukesh
Summary:
Tag: postgres 
Status: draft

https://www.digitalocean.com/community/tutorials/how-to-use-logstash-and-kibana-to-centralize-logs-on-centos-6	


yum install elasticsearch-2.0.0.rpm

### NOT starting on installation, please execute the following statements to configure elasticsearch service to start automatically using chkconfig
 sudo chkconfig --add elasticsearch
### You can start elasticsearch service by executing
 sudo service elasticsearch start

mkdir /data/elastic
chown elasticsearch.elasticsearch /data/elastic

Change network.host to localhost as kibana will use it from localhost 	

network.host: localhost

path.data: /data/elastic


Install Log Stash 	
yum install logstash-2.0.0-1.noarch.rpm


Generate SSL Certificates

vim /etc/pki/tls/openssl.cnf

Find the [ v3_ca ] section in the file, and add this line under it (substituting in the Logstash Server's private IP address):

subjectAltName = IP: <	logstash_server_private_ip>







sudo groupadd -g 1005 kibana
sudo useradd -u 1005 -g 1005 kibana

sudo mkdir -p /opt/kibana

cd /etc/init.d && sudo curl -o kibana https://gist.githubusercontent.com/thisismitch/8b15ac909aed214ad04a/raw/fc5025c3fc499ad8262aff34ba7fde8c87ead7c0/kibana-4.x-init

If you getting env: /etc/init.d/kibana: Permission denied
chmod +x /etc/init.d/kibana /etc/default/kibana

You can visit the http://192.168.0.1:5601/ 



We can use nginx for port forwarding, and use port 80


Install Nginx 
sudo yum -y install nginx httpd-tools

Add htpassword 
sudo htpasswd -c /etc/nginx/htpasswd.users kibanaadmin/ipinfra
ipinfra@123


Create 
/etc/nginx/conf.d/kibana.conf
    server {
        listen 80;

        server_name example.com;

        auth_basic "Restricted Access";
        auth_basic_user_file /etc/nginx/htpasswd.users;

        location / {
            proxy_pass http://localhost:5601;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;        
        }
    }





Installing and running forwarder

wget https://download.elastic.co/logstash-forwarder/binaries/logstash-forwarder-0.4.0-1.x86_64.rpm

cd /etc/init.d/; sudo curl -o logstash-forwarder http://logstashbook.com/code/4/logstash_forwarder_redhat_init
sudo chmod +x logstash-forwarder


Dependency 
sudo curl -o /etc/sysconfig/logstash-forwarder http://logstashbook.com/code/4/logstash_forwarder_redhat_sysconfig


