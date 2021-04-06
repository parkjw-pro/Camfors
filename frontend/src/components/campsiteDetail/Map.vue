<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script>
const KAKAO_API_KEY = process.env.VUE_APP_KAKAO_API_KEY;
import { mapGetters } from "vuex";
export default {
  components: {},
  props: ["mapX", "mapY"],
  data: function() {
    return {};
  },
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
  },
  computed: {
    ...mapGetters({
      getDetailInfo: "campStore/getDetailInfo"
    })
  },
  methods: {
    initMap() {
      let container = document.getElementById("map");
      let options = {
        center: new kakao.maps.LatLng(this.mapY, this.mapX),
        level: 6
      };
      var map = new kakao.maps.Map(container, options);

      // 마커 이미지 변경
      let imageSrc = "https://ifh.cc/g/ZpX0DY.png";
      let imageSize = new kakao.maps.Size(42, 43);
      let imageOption = { offset: new kakao.maps.Point(27, 69) };

      let markerImage = new kakao.maps.MarkerImage(
        imageSrc,
        imageSize,
        imageOption
      );

      //마커추가하려면 객체를 아래와 같이 하나 만든다.
      var marker = new kakao.maps.Marker({
        position: map.getCenter(),
        image: markerImage
      });

      marker.setMap(map);

      let content =
        '<div class="overlay_info" style="background-color:#fff; border-radius: 6px; margin-bottom: 12px; float:left;position: relative; border: 1px solid #ccc; border-bottom: 2px solid #ddd;">' +
        "<strong>" +
        this.getDetailInfo.campsite_name +
        "</div>";

      // 커스텀 오버레이가 표시될 위치입니다
      let position = new kakao.maps.LatLng(this.mapY, this.mapX);

      let customOverlay = new kakao.maps.CustomOverlay({
        content: content,
        position: position
      });

      // 커스텀 오버레이를 지도에 표시합니다
      customOverlay.setMap(map);

      let zoomControl = new kakao.maps.ZoomControl();
      map.addControl(zoomControl, kakao.maps.ControlPosition.BOTTOMRIGHT);
    },
    addScript() {
      const script = document.createElement("script");
      /* global kakao */

      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=" +
        KAKAO_API_KEY;
      document.head.appendChild(script);
    }
  }
};
</script>
<style scoped>
#map {
  width: 100%;
  height: 400px;
}
</style>
