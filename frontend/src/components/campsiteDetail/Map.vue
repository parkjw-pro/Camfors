<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script>
const KAKAO_API_KEY = process.env.VUE_APP_KAKAO_API_KEY;
export default {
  components: {
  },
  data: function() {
    return {
      
    };
  },
  mounted() {
    window.kakao && window.kakao.maps
      ? this.initMap()
      : this.addScript();
  },
  methods: {
    initMap() {
      let container = document.getElementById('map');
      let options = {
        center: new kakao.maps.LatLng(37.564343, 126.947613),
        level: 3,
      };
      var map = new kakao.maps.Map(container, options);
      
      //마커추가하려면 객체를 아래와 같이 하나 만든다. 
      var marker = new kakao.maps.Marker({ 
        position: map.getCenter() 
        }); 
        marker.setMap(map);
   
      let zoomControl = new kakao.maps.ZoomControl();
      map.addControl(zoomControl, kakao.maps.ControlPosition.BOTTOMRIGHT);
    
    },
    addScript() {
      const script = document.createElement('script');
      /* global kakao */

      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey='+KAKAO_API_KEY;
      document.head.appendChild(script);
    },
  },
};
</script>
<style scoped>

#map {
  width: 100%;
  height: 400px;
}


</style>
