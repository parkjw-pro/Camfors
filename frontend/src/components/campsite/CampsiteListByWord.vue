<template>
  <div>
    <div v-for="(item, index) in SearchWordList" :key="index">
      <ListByWordSwiper :tag="item" />
    </div>
  </div>
</template>

<script>
import "swiper/swiper-bundle.css";
import ListByWordSwiper from "@/components/campsite/ListByWordSwiper";
export default {
  components: {
    ListByWordSwiper
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
