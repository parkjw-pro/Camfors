<template>
  <div id="taglist">
    <h3 style="text-align: left; font-family: 'Hanna', sans-serif;">
      {{ tag }}
    </h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide v-for="(item, index) in campsiteList" :key="index">
        <b-card
          title="SSAFY 캠핑장"
          img-src="https://gocamping.or.kr/upload/camp/3/thumb/thumb_720_6791ufBTEV41l7kb7jgUuvkF.jpg"
          img-alt="Image"
          img-top
          tag="article"
          style=""
          class="shadow-sm"
          @click="goDetailList"
        >
          <b-card-text> 경기도 가평군 </b-card-text>
          <b-row class="ml-1 pl-1">
            <div style="text-align: left;">
              <span class="reviewLike mt-4">
                <!--좋아요 여부와 좋아요 수-->

                <b-icon
                  icon="suit-heart-fill"
                  variant="danger"
                  font-scale="1.5"
                  v-if="liked"
                  @click="likeReview()"
                ></b-icon>
                <b-icon
                  icon="suit-heart"
                  variant="danger"
                  font-scale="1.5"
                  v-else
                  @click="likeReview()"
                ></b-icon>
              </span>
              <small class="ml-1">n명이 좋아합니다.</small>
            </div>
          </b-row>
          <!-- <b-button href="#" variant="primary">구경하기!</b-button> -->
        </b-card>
        <!-- <img height="70%" width="100%" src="@/assets/mainpage/campsite1.jpg" /> -->
      </swiper-slide>
      <!-- <swiper-slide>Slide 2</swiper-slide>
    <swiper-slide>Slide 3</swiper-slide>
    <swiper-slide>Slide 4</swiper-slide>
    <swiper-slide>Slide 5</swiper-slide>
    <swiper-slide>Slide 6</swiper-slide>
    <swiper-slide>Slide 7</swiper-slide>
    <swiper-slide>Slide 8</swiper-slide>
    <swiper-slide>Slide 9</swiper-slide>
    <swiper-slide>Slide 10</swiper-slide> -->
      <!-- <div class="swiper-pagination" slot="pagination"></div> -->
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import { swiper, swiperSlide } from "vue-awesome-swiper";
import "swiper/swiper-bundle.css";

export default {
  name: "swiper-example-loop-group",
  title: "Loop mode with multiple slides per group",
  props: {},
  components: {
    swiper,
    swiperSlide
  },
  data() {
    return {
      campsiteList: [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19
      ],
      swiperOption: {
        slidesPerView: 2,
        spaceBetween: 20,
        slidesPerGroup: 2,
        loop: true,
        loopFillGroupWithBlank: false,
        pagination: {
          el: ".swiper-pagination",
          clickable: true
        },

        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        }
      },
      campsiteId: "1234"
    };
  },
  methods: {
    goDetailList: function() {
      // 리뷰 작성 페이지로 넘어가준다!!
      // console.log("보냅니다", this.store);
      console.log("디테일로 이동");
      console.log(this.campsiteId);
      this.$router.push({
        name: "CampsiteDetail",
        params: { campsiteId: this.campsiteId }
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.swiper {
  height: 100%;
  width: 100%;

  .swiper-slide {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-weight: bold;
    background-color: gray;
  }
}
</style>
<style scoped>
#taglist {
  margin-right: 20px;
  margin-left: 20px;
}
.card-body {
  margin-top: 0;
  padding: 0;
  background-color: #fffff0;
}
.card-text {
  margin-bottom: 5px;
}
.card-title {
  margin-bottom: 5px;
  margin-top: 5px;
}
.shadow-sm {
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075) !important;
}
.card {
  border: none;
}
</style>
