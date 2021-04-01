<template>
  <div >
    <b-row v-for="(item, index) in SearchWordList" :key="index">

<div class="col-6">
  <swiperBlock :item = "item"/>
  <swiperBlock :item = "item"/>
  <swiperBlock :item = "item"/>
</div>
      
    </b-row>
  </div>
</template>

<script>
import "swiper/css/swiper.css";
import swiperBlock from "@/components/campsite/swiperBlock";
export default {
  components: {
    swiperBlock
  },
  props: {
    SearchWordList: Array
  },
  data: function() {
    return {
      swiperOption: {
        direction: "vertical",
        pagination: {
          el: ".swiper-pagination",
          type: "bullets"
        }
      }
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add("large");
    }
  },
  
};
</script>

<style></style>
<style scoped>
.swiper-slide {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.swiper-container {
  height: 500px;
}
</style>
