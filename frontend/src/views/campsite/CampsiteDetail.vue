<template>
  <div>
    <div class="contentsBox">
      <h2 style="color:white;">캠핑장이름</h2>
      <div class="tags"> 
        <div class="tag" v-for="(tag, idx) in tagList" :key="idx">
        {{ tag }}
        </div>
      </div>
    </div>

    <div class="campsiteInfo">
      <div class="campsiteInfoImg">
        <b-img id="campsiteImg" src="https://gocamping.or.kr/img/2018/sub/camp/camp_typebg_02.jpg" alt="Responsive image"></b-img>
      </div>

      <div class="campsiteInfoList">
        <b-list-group> 
          <b-list-group-item>경북 예천군 보문면 옥천길 30</b-list-group-item>
          <b-list-group-item>새움정은 예천군에 위치한 폐교된 옥천분교를 리모델링하여 약용식물, 곤충관찰, 자수체험 등 현장교육을 할 수 있는 교육농장이면서, 드넓은 600여평의 잔디위에서 시골학교에서의 캠핑체험을 할 수 있는 소규모 캠핑장입니다.</b-list-group-item>
          <b-list-group-item>https://gocamping.or.kr/img/2018/sub/camp/camp_typebg_02.jpg</b-list-group-item>
          <b-list-group-item>https://gocamping.or.kr/img/2018/sub/camp/camp_typebg_02.jpg</b-list-group-item>
        </b-list-group>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CampsiteDetail",
  components: {},
  data: function() {
    return {
      campsiteId: "",
      tagList: ["#가족들과 가기 좋은", "#물놀이 하기 좋은", "#봄", "#바다가 보이는"],
    };
  }
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

/* .tags {
  position:flex;
  
}

.tag {
  margin: 0 auto;
  float: left;
  color:white;
} */

.tag {
  float: left;
  color:white;
}

#campsiteImg {
  width: 450px;
  height: 300px;
}

.campsiteInfo {
  padding: 15px 0 95px 0
}

.campsiteInfoImg {
  float: left;
  width: 40%;
}

.campsiteInfoList {
  float: right;
  width: 50%;
}

</style>
