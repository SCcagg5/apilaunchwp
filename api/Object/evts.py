import requests
import os
import time

#docker = "/mnt/c/Program\ Files/Docker/Docker/resources/bin/docker.exe"#docker
#dc = "/mnt/c/Program\ Files/Docker/Docker/resources/bin/docker-compose.exe"#"docker-compose"
#path = ".."

class evts:
    def run(x, login):
        name = str(login) + "-" +str(x)
        commands = [
        "docker run -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=wordpress --name "+name+"_db -v /srv/isginnovation/"+login+"/"+str(x)+"/database:/var/lib/mysql --restart always -d mariadb:latest",
        "docker run -e WORDPRESS_DB_PASSWORD=password -e VIRTUAL_HOST="+name+".isginnovation.fr -e LETSENCRYPT_HOST="+name+".isginnovation.fr --restart always --name "+name+"_wp --link "+login+"-"+str(x)+"_db:mysql -v /srv/isginnovation/"+login+"/"+str(x)+"/wordpress:/var/www/html -d wordpress",
        "sleep 10",
        "docker exec "+name+"_wp curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar",
        "docker exec "+name+"_wp chmod +x wp-cli.phar",
        "docker exec "+name+"_wp mv wp-cli.phar /usr/local/bin/wp-cli",
        "docker exec "+name+"_wp wp-cli --allow-root core install --url="+name+".isginnovation.fr --title='"+name+"' --admin_user="+login+" --admin_password=1q2W3e --admin_email=eliot.courtel@gmail.com"]
        globalcom = ""
        for i in commands:
            globalcom += str(i) + " ; "
        os.system(globalcom)
        return [True, {"url": login+"-"+str(x)+".isginnovation.fr"}, 200]

if __name__ == '__main__':
    path = "../.."
    print(evts.run(1, "courte_e")[1])
