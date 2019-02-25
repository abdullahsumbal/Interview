### What is a MVT?
a standard for vector tile format

### tippecanno?
Mapbox tool that converts geojson files to mvt.

### .pdf format?
protocol buffer binary format. very fast. it is a gzip of the mvt.

### tileserver-gl vs tileserver-light-gl?
light does not support raster tiles.

### how to install tileserver-light-gl
`npm install -g tileserver-gl-light`

But this does not work.
Instead it is suggested to use the tileserver-gl using docker.

### how to install tileserver-gl?
I downloaded the the repo for opemmaptiles and used the following command

```
git clone git@github.com:openmaptiles/openmaptiles.git
cd openmaptiles

sudo make start-tileserver
```

### How to use tileserver-gl-light?
`docker run --rm -it -v $(pwd):/data -p 8080:80 klokantech/tileserver-gl <mvt file>`


### From where can I down data in mvt format?
```
curl -o portugal.mbtiles https://openmaptiles.os.zhdk.cloud.switch.ch/v3.3/extracts/portugal.mbtiles
```

###
