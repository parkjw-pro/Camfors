<template>
  <div>
    <!-- 댓글 리스트 -->
    <!-- <b-list-group flush v-for="(item, index) in commentList" :key="index"> -->
    <b-list-group flush v-for="(comment, index) in commentList" :key="index">
      <b-list-group-item class="flex-column align-items-start">
        <div class="d-flex w-100 justify-content-between">
          <p class="mb-1">닉네임</p>
          <small> {{comment.created_at}} </small>
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
      </b-list-group-item>
    </b-list-group>
  </div>
</template>
<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";
import { mapGetters } from "vuex";
export default {
  data() {
    return {};
  },
  props: ["commentList"],
  methods: {
    removeReview(review_id) {
      console.log(review_id);
      axios({
        method: "delete",
        url: `${SERVER_URL}/camp/deletereview/${review_id}`
      })
        .then(res => {
          console.log(res.data);
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  computed: {
    ...mapGetters({
      getUserId: "userStore/getUserId"
    })
  }
};
</script>
<style scoped>
.comments {
  width: 90%;
  margin: 0 auto;
}
</style>
