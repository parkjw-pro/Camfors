<template>
  <div id="taglist">
    <br />
    <br />
    <h3
      style="text-align: left; font-family: 'Hanna', sans-serif; color: white;"
    >
      {{ tag.tag_name }}
    </h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide v-for="(item, index) in campsiteList" :key="index">
        <campsiteBlock :item="item" />
        <div v-if="index === campsiteList.length - 1">{{ endLoading() }}}</div>
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
import axios from "axios";
import { mapGetters } from "vuex";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "swiper-example-loop-group",
  title: "Loop mode with multiple slides per group",
  props: {
    tag: Object
  },
  components: {
    Swiper,
    SwiperSlide,
    campsiteBlock
  },
  created() {
    axios({
      method: "get",
      url: `${SERVER_URL}/camp/camptaglist/${this.tag.tag_id}`
    })
      .then(res => {
        // console.log(res.data);
        this.campsiteList = res.data;
      })
      .catch(error => {
        console.log(error);
      });
  },
  computed: {
    ...mapGetters({
      getUserId: "userStore/userId"
    })
  },
  data() {
    return {
      campsiteList: [],
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
      campsiteId: "1234"
    };
  },
  methods: {
    endLoading() {
      this.$emit("endLoading");
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
