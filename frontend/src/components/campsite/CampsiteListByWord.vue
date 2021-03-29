<template>
  <div>
    <div v-for="(item, index) in tagList" :key="index">
      <ListByWordSwiper :tag="item" />
    </div>
  </div>
</template>

<script>
import "swiper/swiper-bundle.css";
import ListByWordSwiper from "@/components/campsite/ListByWordSwiper";
import { mapGetters } from "vuex";
export default {
  components: {
    ListByWordSwiper
  },
  data: function() {
    return {
      tagList: {
        tag : 
        {
          data : []
        }
      },
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
