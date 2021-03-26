<template>
  <div>
    <!-- <div>
      <h3>{{ tag }}</h3>
    </div> -->
    <div class="mt-2" style="text-align: left">
      <span class="font-weight-bold" style="font-size: large;">{{ tag }}</span>
    </div>
    <b-row>
      <div
        class="card mb-4 "
        style="width: 18rem;"
        v-for="(item, index) in campsiteList"
        :key="index"
      >
        <!-- <b-card
        header-tag="header"
        header-bg-variant="white"
        footer-tag="footer"
        footer-bg-variant="white"
        style="width: 18rem;"
        v-for="(item, index) in campsiteList" :key="index"
      >  -->
        <!-- <template #header style="padding: 0, 0;">
          <img height="100%" width="100%" src="@/assets/mainpage/campsite1.jpg" />
      </template> -->
        <img height="70%" width="100%" src="@/assets/mainpage/campsite1.jpg" />
        <!-- 2. 본문 부분 -->
        <!-- 2.2 별점 -->
        <!-- 2.3 리뷰 내용 -->
        <!-- 2.4 리뷰 생성일자 -->
        <!-- <b-row class="ml-2 pl-2" > -->
        <h6 class="card-title">A캠핑장</h6>
        <p class="card-text">강원도 춘천시</p>
        <!-- </b-row> -->

        <!-- 3. footer 부분 -->
        <b-row class="ml-1 pl-1">
          <div style="text-align: left;">
            <span class="reviewLike mt-4">
              <!--좋아요 여부와 좋아요 수-->

              <b-icon
                icon="suit-heart-fill"
                variant="danger"
                font-scale="1.5"
                v-if="liked"
                @click="likeReview()"
              ></b-icon>
              <b-icon
                icon="suit-heart"
                variant="danger"
                font-scale="1.5"
                v-else
                @click="likeReview()"
              ></b-icon>
            </span>
            <small class="ml-1">n명이 좋아합니다.</small>
          </div>
        </b-row>
      </div>
      <!-- </b-card> -->
    </b-row>
  </div>
</template>

<script>
export default {
  name: "CampsiteList",
  props: {
    tag: String
  },
  data: function() {
    return {
      campsiteList: [1, 2, 3, 4, 5, 6]
    };
  }
};
</script>
<style>
card-header {
  padding: 1.75rem 1.25rem;
}
p {
  margin-bottom: 0 !important;
}
</style>
