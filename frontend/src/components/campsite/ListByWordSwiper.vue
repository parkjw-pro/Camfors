<template>
  <div id="taglist">
    <br />
    <br />
    <h3
      style="text-align: left; font-family: 'Hanna', sans-serif; color: black;"
    >
      {{ tag[0][0].tag_name }}
    </h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide
        v-for="(item, index) in tag.slice(1, tag.length)"
        :key="index"
      >
        <b-card @click="goDetailList(item[0].campsite_id)">
          <b-card-img
            v-if="item[0].firstImageUrlV.length > 0"
            :src="item[0].firstImageUrlV"
            height="170px"
          ></b-card-img>
          <b-card-img
            v-else
            src="https://cdn.pixabay.com/photo/2019/07/25/17/09/camp-4363073_960_720.png"
            height="170px"
          ></b-card-img>
          <span class="my-2" style="font-size:18px">{{
            item[0].campsite_name
          }}</span>
          <b-card-text>{{ item[0].doNm }} {{ item[0].sigunguNm }}</b-card-text>
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
              <small class="ml-1"
                >{{ item[0].likeCount }}명이 좋아합니다.</small
              >
            </div>
          </b-row>
        </b-card>
      </swiper-slide>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  name: "swiper-example-loop-group",
  title: "Loop mode with multiple slides per group",
  props: {
    tag: Array
  },
  components: {
    Swiper,
    SwiperSlide
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 5,
        spaceBetween: 20,
        slidesPerGroup: 5,
        loop: false,
        loopFillGroupWithBlank: false,
        pagination: {
          el: ".swiper-pagination",
          clickable: true
        },

        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        }
      }
      // tagName : Array
    };
  },
  methods: {
    goDetailList: function(campsite_id) {
      // 리뷰 작성 페이지로 넘어가준다!!
      // console.log("보냅니다", this.store);
      console.log("디테일로 이동");
      console.log(campsite_id);
      this.$router.push({
        name: "CampsiteDetail",
        params: { campsiteId: campsite_id }
      });
    }
  }
  // created : {

  // }
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
  background-color: rgb(71, 64, 64);
  color: whitesmoke;
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
/* .card- {

} */
</style>
