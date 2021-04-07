<template>
    <div>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
        <div id="map">
        </div>
    </div>
</template>

<script>
    import * as L from 'leaflet'
    import icon from 'leaflet/dist/images/marker-icon.png';
    import iconShadow from 'leaflet/dist/images/marker-shadow.png';

    export default {
        name: "detail",
        data() {
            return {
                msg: 'Welcome to Your Vue.js App',
                id: '00'
            }
        },
        mounted() {
            this.initMap()
        },
        methods:{
            initMap(){
                const map = L.map('map', {
                });
                L.Marker.prototype.options.icon = L.icon({
                    iconUrl: icon,
                    shadowUrl: iconShadow
                });
                map.locate({setView: true, maxZoom: 16});
                L.tileLayer(
                    "http://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
                    {
                        subdomains: ["1", "2", "3", "4"],
                        attribution: "高德"
                    }
                ).addTo(map);
                function onLocationFound(e) {
                    console.log(e)
                    var radius = e.accuracy;
                    L.marker(e.latlng).addTo(map)
                        .bindPopup("You are within " + radius + " meters from this point").openPopup();

                    L.circle(e.latlng, radius).addTo(map);
                }

                map.on('locationfound', onLocationFound);

                // function onLocationError(e) {
                //     alert(e.message);
                // }
                //
                // map.on('locationerror', onLocationError);
            }
        }
    }
</script>

<style scoped>
    #map {
        width: 100%;
        height: calc(100vh);
    }
</style>
