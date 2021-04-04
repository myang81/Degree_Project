<template>
  <div style="display: flex;height: 100%;flex-direction: column">
    <P class="center-title">Choose your home address</P>
    <el-row style="height: 100%" :gutter=20>
      <el-col :span=12>
        <div class="form-block">
          <el-form label-position="right" label-width="80px" :model="form">
          <el-row>
            <el-col  :span=12>
              <el-form-item label="region">
                <el-autocomplete v-model="form.region" :fetch-suggestions="querySearchRegion"></el-autocomplete>
              </el-form-item>
            </el-col>
            <el-col :span=12>
              <el-form-item label="district">
                <el-autocomplete v-model="form.district" :fetch-suggestions="querySearchDistrict"></el-autocomplete>
              </el-form-item>
            </el-col>
          </el-row>
            <el-row>
              <el-col :span=12>
                <el-form-item label="longitude">
                  <el-input v-model="form.coordinate[0]"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span=12>
                <el-form-item label="latitude">
                  <el-input v-model="form.coordinate[1]"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row style="text-align: end;">
              <el-form-item>
                <el-button type="primary" @click="onSubmit" style="margin-right: 20px">N E X T</el-button>
              </el-form-item>
            </el-row>
          </el-form>
        </div>
      </el-col>
      <el-col :span=12 style="height: 100%;">
        <div id="map" style="height: 100%;">
        </div>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import global from '@/assets/global'
import * as L from 'leaflet'
import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';
/**
 * 未做表单验证
 * */
export default {
name: "address",
  data(){
    return {
      form:{
        region:"",
        district:"",
        coordinate:[]
      }
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

      function onLocationError(e) {
          alert(e.message);
      }

      map.on('locationerror', onLocationError);
    },
    onSubmit(){
      this.$router.push({ name: 'HouseNum', params: { form: this.form }})
    },
    querySearchRegion(queryString, cb) {
      let regions = [global.region];
      console.log(regions)
      let results = queryString ? regions.filter(this.createFilter(queryString)) : regions;
      // 调用 callback 返回建议列表的数据
      cb(results);
    },
    querySearchDistrict(queryString, cb) {
      let districts = [global.district];
      let results = queryString ? districts.filter(this.createFilter(queryString)) : districts;
      // 调用 callback 返回建议列表的数据
      cb(results);
    },
    createFilter(queryString) {
      return (res) => {
        console.log('res-----------',res)
        return (res.key.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
      };
    },
  }
}
</script>

<style scoped>
  .center-title{
    font-size: 2rem;
    padding: 30px;
    text-align: right;
    position: relative;
    overflow: hidden;

  }
  .center-title:after {
    content: "";
    display: block;
    position: absolute;
    bottom: 10%;
    left: 0;
    height: 5px;
    width: 200%;
    background-color: #caa;
    background-image: linear-gradient(to right, #cc7575, #ffd544 50%, #cc7575);
    animation:colorLine 1s alternate infinite;
  }
  @keyframes colorLine
  {
    from {left:-100%;}
    to {left: 0}
  }
</style>