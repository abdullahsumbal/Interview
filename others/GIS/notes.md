### What is a MVT?
a standard for vector tile format

### tippecanno?
Mapbox tool that converts geojson files to mvt.

### .pdf format?
protocol buffer binary format. very fast. it is a gzip of the mvt.

### tileserver-gl vs tileserver-light-gl?
light does not support raster tiles.

### how to install tileserver-light-gl
`
npm install -g tileserver-gl-light
`

But this does not work.
Instead it is suggested to use the tileserver-gl using docker.

then I found this. this make npm works

```
sudo apt-get install -y software-properties-common protobuf-compiler pkg-config libcairo2-dev libjpeg-dev libgif-dev git libgl1-mesa-glx build-essential g++ curl

curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
sudo apt-get install -y nodejs xvfb

sudo mkdir /var/cache/npm
sudo npm config set cache /var/cache/npm --global

cd /tmp
git clone https://github.com/klokantech/tileserver-gl.git
cd tileserver-gl/

sudo npm install -g --unsafe-perm
```

### how to install tileserver-gl?
I downloaded the the repo for opemmaptiles and used the following command

```
git clone git@github.com:openmaptiles/openmaptiles.git
cd openmaptiles

sudo make start-tileserver
```

### How to use tileserver-gl-light?
`docker run --rm -it -v $(pwd):/data -p 8080:80 klokantech/tileserver-gl <mvt file>
`

or

`tileserver-gl <mt file>`


### From where can I down data in mvt format?
```
curl -o portugal.mbtiles https://openmaptiles.os.zhdk.cloud.switch.ch/v3.3/extracts/portugal.mbtiles
```

when downloading the data from openmaptiles, they dont have labels. thats why you need to clone openmaptiles repo and generate the tiles with names.  

### How to edit the config file tileserver-gl.

Use verbose when running tileserver-gl and copy the config file automatically created. then put it in the config.json file. use the tag ``-c config.json `` when tileserver-gl.
 more option and tag can be found here
 https://tileserver.readthedocs.io/en/latest/usage.html.


### Some commands for docker

 ```
sudo docker volume ls

sudo docker volume prune

sudo docker container ls --all

sudo docker rm af950dbdac72

sudo docker ps
 ```


### What is mbutil?

This is a mapbox which helps create .pbf

this used this command `mb-util --image_format=pbf portugal.mbtiles portugal`

can read more about it [here](https://github.com/mapbox/mbutil)


### how to start a local server?
`python -m SimpleHTTPServer`


### how to curl data
`curl -o zurich_switzerland.mbtiles https://openmaptiles.os.zhdk.cloud.switch.ch/v3.3/extracts/zurich_switzerland.mbtiles
`


### What is ogr2ogr?
provides an easy way to convert data between common storage formats: GeoJSON, Shapefile, PostGIS and others.
Read more [here](https://morphocode.com/using-ogr2ogr-convert-data-formats-geojson-postgis-esri-geodatabase-shapefiles/)
