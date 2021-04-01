<template>
  <div>
    <!-- 캠핑장 소개 컨텐츠 (이름, 태그) -->
    <div class="contentsBox">
      <h2 style="color:white;">{{ getDetailInfo.campsite_name }}</h2>
      <div class="tag" v-for="(tag, idx) in tagList" :key="idx">
        {{ tag }}
      </div>
    </div>

    <!-- gray bar -->
    <div class="bar"></div>

    <!-- 캠핑장 상세페이지 컨테이너 -->
    <b-container>
      <div class="row campsiteInfo">
        <div class="col-sm-6 col-md-6 campsiteInfoImg">
          <b-img
          v-if="getDetailInfo.firstImageUrlV.length>0"
            id="campsiteImg"
            :src="getDetailInfo.firstImageUrlV"
            alt="Responsive image"
          ></b-img>
            <b-img
            v-else
            id="campsiteImg"
            src="https://cdn.pixabay.com/photo/2019/07/25/17/09/camp-4363073_960_720.png"
            alt="Responsive image"
          ></b-img>
        </div>

        <div class="col-sm-6 col-md-6 campsiteInfoList">
          <b-list-group flush>
            <b-list-group-item>{{ getDetailInfo.indutyV }}</b-list-group-item>
            <b-list-group-item>{{ getDetailInfo.addr1 }}</b-list-group-item>
            <b-list-group-item>{{ getDetailInfo.intro }}</b-list-group-item>
            <b-list-group-item>{{ getDetailInfo.tel }}</b-list-group-item>
            <b-list-group-item
              ><b-button variant="secondary" :href="getDetailInfo.homepage"
                >홈페이지</b-button
              >
              <b-button variant="secondary"
                >예약하기</b-button
              ></b-list-group-item
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

      <!-- 캠핑장 소개 -->
      <div class="campsiteIntro">
        <h3 style="margin-top:20px; text-align:left;">
          <b-icon icon="caret-right-fill" font-scale="1"></b-icon>캠핑장소개
        </h3>
        <div class="row">
          <div class="col-5">캠핑장 주요 시설 자세한 소개</div>
          <div class="col-1"></div>
          <div class="col-5">
            <Map v-if="getDetailInfo.mapX" :mapX="getDetailInfo.mapX" :mapY="getDetailInfo.mapY" />
          </div>
        </div>
      </div>

      <!-- 편의시설 -->
      <div class="facility">
        <h3 style="margin-top:20px; text-align:left;">
          <b-icon icon="caret-right-fill" font-scale="1"></b-icon>편의시설
        </h3>
        <div class="row facilityIcon">
          <div style="text-align:center; padding-right:50px; padding-top:10px;">
            <font-awesome-icon icon="volleyball-ball" class="fa-3x" />
            <p>운동시설</p>
          </div>
          <div style="text-align:center; padding-right:50px; padding-top:10px;">
            <font-awesome-icon icon="water" class="fa-3x" />
            <p>물놀이/강</p>
          </div>
          <div style="text-align:center; padding-right:50px; padding-top:10px;">
            <font-awesome-icon icon="fish" class="fa-3x" />
            <p>낚시</p>
          </div>
          <div style="text-align:center; padding-right:50px; padding-top:10px;">
            <font-awesome-icon icon="circle" class="fa-3x" />
            <p>운동장</p>
          </div>
          <div style="text-align:center; padding-right:50px; padding-top:10px;">
            <font-awesome-icon icon="paw" class="fa-3x" />
            <p>반려견 동반</p>
          </div>
        </div>
      </div>

      <!-- 한 줄 리뷰 -->
      <div class="comment">
        <h3 style="margin-top:20px; text-align:left;">
          <b-icon icon="caret-right-fill" font-scale="1"></b-icon>한 줄 리뷰
        </h3>

        <Comment />
      </div>

      <!-- 블로그 리뷰 -->
      <div class="blogReview">
        <h3 style="margin-top:20px; text-align:left;">
          <b-icon icon="caret-right-fill" font-scale="1"></b-icon>블로그 리뷰
        </h3>
        <BlogReview v-if="getDetailInfo.campsite_name" :name="getDetailInfo.campsite_name" />
      </div>
    </b-container>

  </div>
</template>

<script>
import Map from "@/components/campsiteDetail/Map";
import Comment from "@/components/campsiteDetail/Comment";
import BlogReview from "@/components/campsiteDetail/BlogReview";
import { mapGetters } from "vuex";
export default {
  name: "CampsiteDetail",
  components: {
    Map,
    Comment,
    BlogReview
  },
  created() {
    this.$store.dispatch(
      "campStore/campsiteDetail",
      this.$route.params.campsiteId
    );
  },
  computed: {
    ...mapGetters({
      getDetailInfo: "campStore/getDetailInfo",
    })
  },
  data: function() {
    // console.log(this.$route.params.campsiteId)
    return {
      campDetail: [],
      campsiteId: "",
      tagList: [
        "#가족들과 가기 좋은",
        "#물놀이 하기 좋은",
        "#봄",
        "#바다가 보이는"
      ]
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
.campsiteInfoList {
  text-align: left;
}

.map {
  width: 30%;
  float: left;
}

.campsiteIntro {
  margin-top: 40px;
  width: 100%;
  border-top: 1px solid rgba(77, 74, 74, 0.459);
}

.facility {
  margin-top: 40px;
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
  margin-top: 40px;
  border-top: 1px solid rgba(77, 74, 74, 0.459);
}

.blogReview {
  margin-top: 40px;
  border-top: 1px solid rgba(77, 74, 74, 0.459);
}

@media (min-width: 1281px) {
  .container,
  .container-sm,
  .container-md,
  .container-lg,
  .container-xl {
    max-width: 90%;
  }
}
</style>
