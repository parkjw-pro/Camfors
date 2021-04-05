<template>
  <div>
    <!-- 캠핑장 소개 컨텐츠 (이름, 태그) -->
    <div class="contentsBox">
      <h2 style="color:white;">{{ getDetailInfo.campsite_name }}</h2>
      <div class="tag">
        {{ getDetailInfo.featureNmV }}
      </div>
    </div>

    <!-- gray bar -->
    <div class="bar"></div>

    <!-- 캠핑장 상세페이지 컨테이너 -->
    <b-container>
      <div class="row campsiteInfo">
        <div class="col-sm-7 col-md-7 campsiteInfoImg">
          <b-img
            v-if="getDetailInfo.firstImageUrlV"
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

        <div class="col-sm-5 col-md-5 campsiteInfoList">
          <table id="list">
            <tbody>
              <tr v-if="getDetailInfo.addr1"><th>상세주소</th><td>{{getDetailInfo.addr1}}</td></tr>
              <tr v-if="getDetailInfo.lineintro"><th>한줄소개</th><td>{{getDetailInfo.lineintro}}</td></tr>
              <tr v-if="getDetailInfo.lctCl"><th>입지구분</th><td>{{getDetailInfo.lctCl}}</td></tr>
              <tr v-if="getDetailInfo.tel"><th>문의처</th><td>{{getDetailInfo.tel}}</td></tr>
              <tr v-if="getDetailInfo.operPdCl"><th>운영기간</th><td>{{getDetailInfo.operPdCl}}</td></tr>
              <tr v-if="getDetailInfo.operDeCl"><th>운영일</th><td>{{getDetailInfo.operDeCl}}</td></tr>
              <tr v-if="getDetailInfo.posblFcltyCl"><th>주변시설</th><td>{{getDetailInfo.posblFcltyCl}}</td></tr>
              <tr v-if="getDetailInfo.themaEnvrnCl"><th>테마환경</th><td>{{getDetailInfo.themaEnvrnCl}}</td></tr>
              <tr v-if="getDetailInfo.exprnProgrm"><th>체험프로그램</th><td>{{getDetailInfo.exprnProgrm}}</td></tr>
              <tr v-if="getDetailInfo.glampInnerFclty"><th>글램핑<br>내부시설</th><td>{{getDetailInfo.glampInnerFclty}}</td></tr>
              <tr v-if="getDetailInfo.caravInnerFclty"><th>카라반<br>내부시설</th><td>{{getDetailInfo.caravInnerFclty}}</td></tr>
            </tbody>
          </table>

          <div class="pageBtn">
            <b-button
                variant="secondary"
                v-if="getDetailInfo.homepage"
                :href="getDetailInfo.homepage"
                target="_blank"
                style="margin-right:10px;"
                >홈페이지</b-button
              >
              <b-button
                variant="secondary"
                v-if="getDetailInfo.resveUrl"
                :href="getDetailInfo.resveUrl"
                target="_blank"
                style="margin-right:10px;"
                >예약하기</b-button
              >
              <b-button
                variant="outline-danger"
                v-if="liked"
                @click="unlikeCampsite(getDetailInfo.campsite_id)"
                ><i class="fas fa-heart"></i></b-button
              >
              <b-button
                variant="outline-secondary"
                v-if="!liked"
                @click="likeCampsite(getDetailInfo.campsite_id)"
                ><i class="fas fa-heart"></i></b-button
              >
          </div>
          
        </div>
      </div>

      <!-- 편의시설 -->
      <div class="facility">
        <h4 style="margin-top:20px; text-align:left;">
          <b-icon icon="caret-right-fill" font-scale="1"></b-icon>편의시설
        </h4>
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

      <!-- 캠핑장 소개 -->
      <div class="campsiteIntro">
        <h4 style="margin-top:20px; text-align:left;">
          <b-icon icon="caret-right-fill" font-scale="1"></b-icon>캠핑장 위치
        </h4>
        <Map
          v-if="getDetailInfo.mapX"
          :mapX="getDetailInfo.mapX"
          :mapY="getDetailInfo.mapY"
        />
        <!-- <div class="row">
          <div class="col-5">캠핑장 주요 시설 자세한 소개</div>
        </div> -->
      </div>

      <!-- 한 줄 리뷰 -->
      <div id="comment">
        <h4 style="margin-top:20px; text-align:left;">
          <b-icon icon="caret-right-fill" font-scale="1"></b-icon>한 줄 리뷰
        </h4>
        <!-- 댓글 남기기 -->
        <div class="row comments">
          <!-- 로그인 했을 때 -->
          <b-form-input
            size="lg"
            class="mr-sm-2"
            placeholder="댓글을 입력해주세요"
            v-if="getUserId"
            v-model="comment"
          ></b-form-input>
          <b-button
            size="lg"
            v-if="getUserId"
            class="my-2 my-sm-0"
            type="submit"
            @click="createReview"
            >등록</b-button
          >
          <!-- 로그인 안했을 시 -->
          <b-form-input
            size="lg"
            class="mr-sm-2"
            v-if="!getUserId"
            placeholder="로그인이 필요한 서비스입니다"
            disabled
            v-model="comment"
          ></b-form-input>
          <b-button
            size="lg"
            v-if="!getUserId"
            disabled
            class="my-2 my-sm-0"
            type="submit"
            @click="createReview"
            >등록</b-button
          >
        </div>
        <Comment v-if="this.commentList" :commentList="this.commentList" v-on:refresh="refresh"/>
      </div>

      <!-- 블로그 리뷰 -->
      <div class="blogReview">
        <h4 style="margin-top:20px; text-align:left;">
          <b-icon icon="caret-right-fill" font-scale="1"></b-icon>블로그 리뷰
        </h4>
        <BlogReview
          v-if="getDetailInfo.campsite_name"
          :name="getDetailInfo.campsite_name"
        />
      </div>
    </b-container>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";

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
    this.$store.state.campStore.detailInfo = [];
    this.$store.dispatch(
      "campStore/campsiteDetail",
      this.$route.params.campsiteId
    );

    const userId = localStorage.getItem("user_id");
    this.userId = userId;

    if (this.getUserId != "") this.getLikeInfo();

    axios({
      method: "get",
      url: `${SERVER_URL}/camp/readreview/${this.campsiteId}`
    })
      .then(res => {
        this.commentList = [];
        console.log(res.data);
        if (res.data !== "리뷰가 없습니다") this.commentList = res.data;
      })
      .catch(error => {
        console.log(error);
    });

    axios({
      method: "get",
      url: `${SERVER_URL}/camp/camprecommend/${this.campsiteId}`
    })
      .then(res => {
        console.log(res.data);
      })
      .catch(error => {
        console.log(error);
    });
      
  },
  computed: {
    ...mapGetters({
      getDetailInfo: "campStore/getDetailInfo",
      getUserId: "userStore/getUserId"
    })
  },
  data: function() {
    return {
      campDetail: [],
      campsiteId: this.$route.params.campsiteId,
      tagList: "",
      commentList: [],
      comment: "",
      userId: "",
      liked: null,
      likeCount: ""
    };
  },
  methods: {
    createReview() {
      console.log(
        Number(this.getUserId),
        Number(this.campsiteId),
        this.comment
      );
      axios
        .post(`${SERVER_URL}/camp/createreview`, {
          user_id: Number(this.getUserId),
          campsite_id: Number(this.campsiteId),
          review: this.comment
        })
        .then(response => {
          console.log(response);
        });

      this.$router.go();
    },
    likeCampsite(campsite_id) {
      axios
        .post(`${SERVER_URL}/camp/addlike`, {
          data: {
            campsite_id: campsite_id,
            user_id: this.getUserId
          }
        })
        .then(response => {
          console.log(response.data);
          this.liked = true;
        });
    },
    unlikeCampsite(campsite_id) {
      axios
        .post(`${SERVER_URL}/camp/unlike`, {
          data: {
            campsite_id: campsite_id,
            user_id: this.getUserId
          }
        })
        .then(response => {
          console.log(response.data);
          this.liked = false;
        });
    },
    getLikeInfo() {
      axios
        .get(`${SERVER_URL}/camp/getlikeinfo`, {
          params: {
            userId: this.getUserId,
            campsiteId: this.campsiteId
          }
        })
        .then(response => {
          console.log(response)
          if (response.data == 0) {
            this.liked = false;
          } else {
            this.liked = true;
          }
        });
    },
    refresh() {
    this.$router.go();
    }
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
  height: 500px;
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

#comment {
  margin-top: 40px;
  border-top: 1px solid rgba(77, 74, 74, 0.459);
}

.blogReview {
  margin-top: 40px;
  border-top: 1px solid rgba(77, 74, 74, 0.459);
}

.form-control {
  width: 90%;
  margin: 0 auto;
}

.row {
  margin-right: 0;
}

th {
  width: 120px;
  padding: 11px 10px;
  border-bottom: 1px solid #c8c8c8;
  text-align: left;
  color: #000;
  line-height: 25px;
}

td {
  width: 480px;
  padding: 11px 10px;
  border-bottom: 1px solid #c8c8c8;
  text-align: left;
  color: #000;
  line-height: 25px;
}

tbody tr:nth-child(1) th, tbody tr:nth-child(1) td {
    border-top: 2px solid #000;
}

.pageBtn {
  margin-top: 10px;
}

.iconBtn {
  margin-top: 10px;
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
