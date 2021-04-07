<template>
  <div id="taglist">
    <br />
    <br />
    <h3
      style="text-align: left; font-family: 'Hanna', sans-serif; color: white;"
    >
      가장 인기 많은 캠핑장
    </h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide v-for="(item, index) in list" :key="index">
        <campsiteBlock :item="item" />
      </swiper-slide>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import campsiteBlock from "@/components/campsite/campsiteBlock";
import "swiper/css/swiper.css";
import { mapGetters } from "vuex";


export default {
  name: "swiper-example-loop-group",
  title: "Loop mode with multiple slides per group",
  props: {
    list: Array
  },
  components: {
    Swiper,
    SwiperSlide,
    campsiteBlock
  },
  computed: {
    ...mapGetters({
      getUserId: "userStore/userId"
    })
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
      },
    };
  },
  methods: {}
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
