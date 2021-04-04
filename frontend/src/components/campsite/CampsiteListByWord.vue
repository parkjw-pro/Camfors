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
      <div class="row">
        <div v-for="(item, index) in paginatedData" :key="index">
          <div class="col-md-3">
            <swiperBlock
              :item="item"
              style="width: 20rem; height:20rem; margin-bottom:2rem;"
            />
          </div>
        </div>
      </div>
      <div class="btn-cover" style="text-align: center;">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>
    </div>
  </div>
</template>

<script>
import "swiper/css/swiper.css";
import swiperBlock from "@/components/campsite/swiperBlock";
import { mapGetters } from "vuex";
export default {
  components: {
    swiperBlock
  },
  props: {
   // SearchWordList: Array,
    SearchWordList: {
      type: Array,
      required: true
    },
    pageSize: {
      type: Number,
      required: false,
      default: 12
    }
  },
  data: function() {
    return {
      swiperOption: {
        direction: "vertical",
        pagination: {
          el: ".swiper-pagination",
          type: "bullets"
        }
      },
      pageNum: 0
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add("large");
    },
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    }

  },
  computed: {
    ...mapGetters({
      getSearchWordName: "campStore/getSearchWordName"
    }),
    pageCount () {
      let listLeng = this.SearchWordList.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.SearchWordList.slice(start, end);
    }
  }
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
