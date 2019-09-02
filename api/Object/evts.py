import requests
import os
import time

#docker = "/mnt/c/Program\ Files/Docker/Docker/resources/bin/docker.exe"#docker
#dc = "/mnt/c/Program\ Files/Docker/Docker/resources/bin/docker-compose.exe"#"docker-compose"
#path = ".."

class evts:
    def run(x, login):
        commands = [
        "docker run -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=wordpress --name "+login+"-"+str(x)+"_db -v /srv/isginnovation/"+login+"/"+str(x)+"/database:/var/lib/mysql --restart always -d mariadb:latest",
        "docker run -e WORDPRESS_DB_PASSWORD=password -e VIRTUAL_HOST="+login+"-"+str(x)+".isginnovation.fr -e LETSENCRYPT_HOST="+login+"-"+str(x)+".isginnovation.fr --restart always --name "+login+"-"+str(x)+"_wp --link "+login+"-"+str(x)+"_db:mysql -v /srv/isginnovation/"+login+"/"+str(x)+"/wordpress:/var/www/html -d wordpress"]
        globalcom = ""
        for i in commands:
            globalcom += str(i) + " ; "
        os.system(globalcom)
        return [True, {"url": login+"-"+str(x)+".isginnovation.fr"}, 200]

if __name__ == '__main__':
    path = "../.."
    print(evts.run(1, "courte_e")[1])
