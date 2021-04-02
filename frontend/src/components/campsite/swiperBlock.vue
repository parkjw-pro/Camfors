<template>
  <b-card>
    <b-card-img
      v-if="item.firstImageUrlV.length > 0"
      @click="campsiteDetail"
      :src="item.firstImageUrlV"
      height="65%"
    ></b-card-img>
    <b-card-img
      v-else
      @click="campsiteDetail"
      src="https://cdn.pixabay.com/photo/2019/07/25/17/09/camp-4363073_960_720.png"
      height="65%"
    ></b-card-img>
    <span class="my-2" style="font-size:18px">{{ item.campsite_name }}</span>
    <b-card-text>{{ item.doNm }} {{ item.sigunguNm }}</b-card-text>
    <b-row class="ml-1 pl-1">
      <div style="text-align: left;">
        <span class="reviewLike mt-4">
          <!--좋아요 여부와 좋아요 수-->

          <b-icon
            icon="suit-heart-fill"
            variant="danger"
            font-scale="1.5"
            v-if="liked"
            @click="unlikeCampsite(item.campsite_id)"
          ></b-icon>
          <b-icon
            icon="suit-heart"
            variant="danger"
            font-scale="1.5"
            v-else
            @click="likeCampsite(item.campsite_id)"
          ></b-icon>
        </span>
        <small class="ml-1">{{ item.likeCount }}명이 좋아합니다.</small>
      </div>
    </b-row>
  </b-card>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "swiperBlock",
  title: "Loop mode with multiple slides per group",
  props: {
    item: Object
  },
  created() {
    this.getLikeInfo();
  },
  computed: {
    ...mapGetters({
      getUserId: "userStore/getUserId"
    })
  },
  data() {
    return {
      liked: false
    };
  },
  methods: {
    likeCampsite(campsite_id) {
      console.log(campsite_id, this.getUserId, "좋아요");
      axios
        .post(`${SERVER_URL}/campsite/like`, {
          userId: this.getUserId,
          campsiteId: campsite_id
        })
        .then(response => {
          this.liked = response.data;
          this.item.likeCount = this.item.likeCount * 1 + 1;
        });
    },
    unlikeCampsite(campsite_id) {
      console.log(campsite_id, this.getUserId, "좋아요취소");
      axios
        .post(`${SERVER_URL}/campsite/unlike`, {
          userId: this.getUserId,
          campsiteId: campsite_id
        })
        .then(response => {
          this.liked = response.data;
          this.item.likeCount = this.item.likeCount * 1 - 1;
        });
    },
    getLikeInfo() {
      axios
        .get(`${SERVER_URL}/campsite/like`, {
          params: {
            userId: this.getUserId,
            campsiteId: this.item.campsite_id
          }
        })
        .then(response => (this.liked = response.data));
    },
    campsiteDetail() {
      this.$router.push({
        name: "CampsiteDetail",
        params: { campsiteId: this.item.campsite_id }
      });
      // console.log('index : ' + index + ' : reallyIndex : ' + reallyIndex)
    }
  }
};
</script>

<style lang="scss" scoped>
.swiper {
  height: 100%;
  width: 100%;

  .swiper-slide {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-weight: bold;
    background-color: gray;
  }
}
</style>
<style scoped>
#taglist {
  margin-right: 20px;
  margin-left: 20px;
}
.card-body {
  margin-top: 0;
  padding: 0;
  background-color: rgb(71, 64, 64);
  color: whitesmoke;
}
.card-text {
  margin-bottom: 5px;
}
.card-title {
  margin-bottom: 5px;
  margin-top: 5px;
}
.shadow-sm {
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075) !important;
}
/* .card- {

} */
</style>
