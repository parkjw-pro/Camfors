<template>
  <div class="BlogReview">
    <b-list-group flush v-for="(item, index) in paginatedData" :key="index">
      <b-list-group-item
        class="flex-column align-items-start"
        v-bind:href="item.link"
        target="_blank"
      >
        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1">{{ item.title }}</h5>
        </div>
        <div class="d-flex w-100 justify-content-between">
          <p class="mb-1" style="text-align:left;">
            {{ item.description }}
          </p>
        </div>
        <div class="d-flex w-100">
          <img
            class="align-self-center"
            height="30px"
            width="30px"
            src="@/assets/naver_icon.jpg"
          />
          <p class="p-2 align-self-center" style="margin:0">
            {{ item.bloggername }}
          </p>
          <p class="p-2 align-self-center" style="margin:0; color:gray;">
            {{ item.postdate }}
          </p>
        </div>
      </b-list-group-item>
    </b-list-group>
    <div v-if="items.length > 5" class="btn-cover" style="text-align: center;">
      <b-button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </b-button>
      <span class="page-count">
        {{ pageNum + 1 }} / {{ pageCount }} 페이지
      </span>
      <b-button
        :disabled="pageNum >= pageCount - 1"
        @click="nextPage"
        class="page-btn"
      >
        다음
      </b-button>
    </div>
  </div>
</template>
<script>
const C_SERVER_URL = process.env.VUE_APP_SERVER_URL_C;
import { mapGetters } from "vuex";
import axios from "axios";

export default {
  data() {
    return {
      items: [],
      pageNum: 0
    };
  },
  props: {
    name: String,
    pageSize: {
      type: Number,
      required: false,
      default: 5
    }
  },
  methods: {
    nextPage() {
      this.pageNum += 1;
    },
    prevPage() {
      this.pageNum -= 1;
    }
  },
  computed: {
    ...mapGetters({
      getDetailInfo: "campStore/getDetailInfo"
    }),
    pageCount() {
      let listLeng = this.items.length,
        listSize = this.pageSize,
        page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;

      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData() {
      const start = this.pageNum * this.pageSize,
        end = start + this.pageSize;
      return this.items.slice(start, end);
    }
  },
  created() {
    // console.log(this.name);
    // 네이버 블로그 리뷰 api
    axios
      .get(`${C_SERVER_URL}`, {
        params: {
          // query: "새움정"
          query: this.name
        }
      })
      .then(response => {
        this.items = response.data.items;

        // html 태그 제거
        for (let i = 0; i < this.items.length; i++) {
          this.items[i].title = this.items[i].title.replace(
            /(<([^>]+)>)/gi,
            ""
          );
          this.items[i].description = this.items[i].description.replace(
            /(<([^>]+)>)/gi,
            ""
          );

          this.items[i].title = this.items[i].title.replace(/&quot;/g, "");

          this.items[i].description = this.items[i].description.replace(
            /&quot;/g,
            ""
          );
        }
      })

      .catch(response => {
        console.log(response);
      });
  }
};
</script>
<style scoped>
.BlogReview {
  width: 80%;
  margin-left: 3%;
}
</style>
