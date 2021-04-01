<template>
  <div class="BlogReview">
    <b-list-group flush v-for="(item, index) in items" :key="index">
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
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import axios from "axios";
export default {
  data() {
    return {
      items: []
    };
  },
  props: ["name"],
  computed: {
    ...mapGetters({
      getDetailInfo: "campStore/getDetailInfo"
    })
  },
  created() {
    // console.log(this.name);
    // 크롤링
    axios
      .get("http://www.camfors.shop:3000/search", {
        params: {
          // query: "새움정"
          query: this.name
        }
      })
      .then(response => {
        // console.log(response.data);
        this.items = response.data.items;
        // console.log(this.items);
        // console.log(this.items[0].description);
      })

      .catch(response => {
        console.log(response);
      });
  }
};
</script>
<style scoped>
.BlogReview {
  width: 95%;
  margin: 0 auto;
}
</style>
