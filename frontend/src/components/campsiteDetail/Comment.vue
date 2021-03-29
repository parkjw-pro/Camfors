<template>
  <div>
    <!-- 댓글 남기기 -->
    <div class="row comments">
      <b-form-input
        size="lg"
        class="mr-sm-2"
        placeholder="로그인이 필요한 서비스입니다"
      ></b-form-input>
      <b-button size="lg" class="my-2 my-sm-0" type="submit">등록</b-button>
    </div>

    <!-- 댓글 리스트 -->
    <!-- <b-list-group flush v-for="(item, index) in commentList" :key="index"> -->
    <b-list-group flush>
      <b-list-group-item class="flex-column align-items-start">
        <div class="d-flex w-100 justify-content-between">
          <p class="mb-1">캠핑조아</p>
          <small>2021.03.28</small>
        </div>

        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1" style="text-align:left;">
            사장님이 친절하고 좋아요
          </h5>
          <small
            ><font-awesome-icon icon="trash" class="fa-2x" style="color:gray"
          /></small>
        </div>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>
<script>
export default {
  data() {
    return {
      commentList: []
    };
  }
};
</script>
<style scoped>
.form-control {
  width: 90%;
}

.comments {
  width: 90%;
  margin: 0 auto;
}
</style>
