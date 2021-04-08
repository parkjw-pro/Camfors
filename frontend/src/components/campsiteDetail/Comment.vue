<template>
  <div>
    <!-- 댓글 리스트 -->
    <!-- <b-list-group flush v-for="(item, index) in commentList" :key="index"> -->
    <b-list-group flush v-for="(comment, index) in paginatedData" :key="index">
      <b-list-group-item class="flex-column align-items-start">
        <div class="d-flex w-100 justify-content-between">
          <p class="mb-1">{{ comment.nickname }}</p>
          <small> {{ comment.created_at }} </small>
        </div>
        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1" style="text-align:left;">
            {{ comment.review }}
          </h5>
          <small
            ><font-awesome-icon
              icon="trash"
              v-if="getUserId == comment.user_id"
              class="fa-2x"
              style="color:gray"
              @click="removeReview(comment.review_id)"
          /></small>
        </div>
        <!-- <button v-if="(index%3)==0"></button> -->
      </b-list-group-item>
    </b-list-group>
    <div
      v-if="commentList.length > 4"
      class="btn-cover"
      style="text-align: center;"
    >
      <b-button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </b-button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
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
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      pageNum: 0
    };
  },
  props: {
    commentList: {
      type: Array,
      required: true
    },
    pageSize: {
      type: Number,
      required: false,
      default: 4
    }
  },
  methods: {
    removeReview(review_id) {
      axios({
        method: "delete",
        url: `${SERVER_URL}/camp/deletereview/${review_id}/`
      })
        .then(() => {
          this.$emit("refresh");
        })
        .catch(error => {
          console.log(error);
        });
    },
    nextPage() {
      this.pageNum += 1;
    },
    prevPage() {
      this.pageNum -= 1;
    }
  },
  computed: {
    ...mapGetters({
      getUserId: "userStore/getUserId"
    }),
    pageCount() {
      let listLeng = this.commentList.length,
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
      return this.commentList.slice(start, end);
    }
  }
};
</script>
<style scoped>
.comments {
  width: 90%;
  margin: 0 auto;
}

.btn-cover {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
</style>
