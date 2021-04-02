<template>
  <div id="box1" style="margin:0 auto;">
    <div style="text-align: center;">
      <br />
      <h2
        v-if="getSearchWordName"
        style="text-align: left; font-family: 'Hanna', sans-serif; color: black;"
      >
        {{ getSearchWordName }}의 검색결과입니다.
      </h2>
      <br />
      <div class="row" style="text-align: center;">
          <div v-for="(item, index) in SearchWordList" :key="index">
            <div class="col-md-3">
              <swiperBlock :item="item" style="width: 20rem; height:20rem; margin-bottom:2rem;" />
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import 'swiper/css/swiper.css';
import swiperBlock from '@/components/campsite/swiperBlock';
import { mapGetters } from 'vuex';
export default {
  components: {
    swiperBlock,
  },
  props: {
    SearchWordList: Array,
  },
  data: function() {
    return {
      swiperOption: {
        direction: 'vertical',
        pagination: {
          el: '.swiper-pagination',
          type: 'bullets',
        },
      },
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add('large');
    },
  },
  computed: {
    ...mapGetters({
      getSearchWordName: 'campStore/getSearchWordName',
    }),
  },
};
</script>

<style scoped>
.swiper-slide {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.swiper-container {
  height: 500px;
}
#box1 {
  display: block;
  width: 72%;
  position: absolute;
  left: 14%;
  margin-top: 0%;
  padding-bottom: 7%;
}
</style>
