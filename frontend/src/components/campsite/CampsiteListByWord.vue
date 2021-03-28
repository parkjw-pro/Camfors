<template>
  <div>
    <div v-for="(item, index) in tagList" :key="index">
      <swipertest :tag="item" />
    </div>
  </div>
</template>

<script>
import "swiper/swiper-bundle.css";
import swipertest from "@/components/campsite/swipertest";
import { mapGetters } from "vuex";
export default {
  components: {
    swipertest
  },
  data: function() {
    return {
      tagList: [
        "야경이 좋은 곳",
        "아이들이랑 가고 싶은 곳",
        "산책하기 좋은 곳"
      ],
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
  created: async function() {
    console.log(this.tagList[0]);
  },
  computed:{
    ...mapGetters({
      getSearchWordList: "campStore/getSearchWordList"
      
    })
  }
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
