<template>
  <div>

    <!-- 캠핑장 소개 컨텐츠 (이름, 태그) -->
    <div class="contentsBox">
      <h2 style="color:white;">캠핑장이름</h2>
      <div class="tag" v-for="(tag, idx) in tagList" :key="idx">
        {{ tag }}
      </div>
    </div>

    <!-- <div class="campsiteInfo">
      <div class="campsiteInfoImg">
        <b-img
          id="campsiteImg"
          src="https://gocamping.or.kr/img/2018/sub/camp/camp_typebg_02.jpg"
          alt="Responsive image"
        ></b-img>
      </div>

      <div class="campsiteInfoList">
        <b-list-group flush>
          <b-list-group-item>경북 예천군 보문면 옥천길 30</b-list-group-item>
          <b-list-group-item
            >새움정은 예천군에 위치한 폐교된 옥천분교를 리모델링하여 약용식물,
            곤충관찰, 자수체험 등 현장교육을 할 수 있는 교육농장이면서, 드넓은
            600여평의 잔디위에서 시골학교에서의 캠핑체험을 할 수 있는 소규모
            캠핑장입니다.</b-list-group-item
          >
          <b-list-group-item
            ><b-button variant="secondary">홈페이지</b-button>
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
// import Map from "@/components/campsiteDetail/Map";
export default {
  name: "CampsiteDetail",
  components: {
    // Map
  },
  created() {
  },
  data: function() {
    return {
      campDetail:[],
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
