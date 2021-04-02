<template>
  <div class="row" style="margin:0 auto; width:1300px;">
    <div v-for="(item, index) in SearchWordList" :key="index" style="margin:0 auto;">

      <div class="col-md-3">
        <swiperBlock :item = "item" style="width: 20rem; height:20rem; margin-bottom:2rem;"/>
      </div>
      
    </div>
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
