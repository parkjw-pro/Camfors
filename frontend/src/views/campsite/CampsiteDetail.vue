<template>
  <div>

    <!-- 캠핑장 소개 컨텐츠 (이름, 태그) -->
    <div class="contentsBox">
      <h2 style="color:white;">{{ getDetailInfo.campsite_name }}</h2>
      <div class="tag" v-for="(tag, idx) in tagList" :key="idx">
        {{ tag }}
      </div>
    </div>

    <!-- <div class="campsiteInfo">
      <div class="campsiteInfoImg">
        <b-img
          id="campsiteImg"
          :src="getDetailInfo.firstImageUrlV"
          alt="Responsive image"
        ></b-img>
      </div>

      <div class="campsiteInfoList">
        <b-list-group flush>
          <b-list-group-item>{{ getDetailInfo.addr1 }}</b-list-group-item>
          <b-list-group-item>{{ getDetailInfo.intro }}</b-list-group-item>
          <b-list-group-item
            ><b-button variant="secondary" :href="getDetailInfo.homepage"
              >홈페이지</b-button
            >
            <b-button variant="secondary">예약하기</b-button></b-list-group-item
          >
          <b-list-group-item
            ><b-icon
              icon="heart"
              font-scale="1.5"
              style="margin-top: 1%; margin-right: 3%;"
            ></b-icon>
            <b-icon icon="chat-left-dots" font-scale="1.5"></b-icon
          ></b-list-group-item>
        </b-list-group>
      </div>
    </div>

    <div class="campsiteIntro">
      <h2>캠핑장소개</h2>
      <div class="map">
        <Map />
      </div>
    </div> -->
  </div>
</template>

<script>
import Map from "@/components/campsiteDetail/Map";
import { mapGetters } from "vuex";
export default {
  name: "CampsiteDetail",
  components: {
    Map,
  },
  created() {
    this.$store.dispatch("campsiteDetail", this.$route.params.campsiteId);
  },
  computed: {
    ...mapGetters(["getDetailInfo"]),
  },
  data: function() {
    return {
      campDetail: [],
      campsiteId: "",
      tagList: [
        "#가족들과 가기 좋은",
        "#물놀이 하기 좋은",
        "#봄",
        "#바다가 보이는",
      ],
    };
  },
};
</script>
<style scoped>
.contentsBox {
  width: 100%;
  height: 30vh;
  background-image: url("https://gocamping.or.kr/img/2018/sub/camp/camp_typebg_03.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  padding: 10%;
}


.bar {
  width: 100%;
  height: auto;
  padding: 9px 0;
  background: #eff0f4;
  position: relative;
}

.container {
  padding-top: 2%;
}

.tag {
  color: white;
  display: inline-block;
  padding-right: 10px;
}

#campsiteImg {
  width: 100%;
  height: 400px;
}

/* .campsiteInfo {
  display: inline-block;
} */

/* .campsiteInfoImg {
  float: left;
  width: 50%;
} */

.campsiteInfoList {
  /* float: left; */
  /* width: 50%; */
  text-align: left;
}

.map {
  width: 30%;
  float:left;
}

.campsiteIntro {
  margin-top:40px;
  width: 100%;
  border-top: 1px solid rgba(77, 74, 74, 0.459);
}

.facility {
  margin-top:40px;
  border-top: 1px solid rgba(77, 74, 74, 0.459);
}
.facilityIcon {
    width: 90%;
    height: auto;
    overflow: hidden;
    padding: 30px 3%;
    background: #f9f9f9;
    border-radius: 5px;
    margin: 0 auto;
}

.comment {
  margin-top:40px;
  border-top: 1px solid rgba(77, 74, 74, 0.459);
}

@media (min-width: 1281px) {
  .container, .container-sm, .container-md, .container-lg, .container-xl {
    max-width: 1250px;
  }
}


</style>
