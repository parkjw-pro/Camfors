<template>
  <div>
    <div v-if="SearchTagList[0].length > 0">
      <div v-for="(item, index) in SearchTagList" :key="index">
        <br />
        <br />
        <h3
          style="text-align: left; font-family: 'Hanna', sans-serif; color: black; margin-left: 20px;"
        >
          {{ getSearchTagListName[index] }}
        </h3>
        <ListByTagSwiper :tag="item" :tagName="getSearchTagListName[item]" />
      </div>
    </div>

    <div v-else class="mt-5 pt-5 minibox" style="margin:0 auto;">
      <img alt="Vue logo" src="@/assets/udonge.png" style="width: 10%" />
      <br />
      <div class="mb-2">
        검색을 원하는 태그를 눌러보세요!
      </div>
    </div>
  </div>
</template>
<script>
import ListByTagSwiper from "@/components/campsiteSearch/ListByTagSwiper";
import { mapGetters } from "vuex";
export default {
  components: {
    ListByTagSwiper
  },
  name: "CampsiteListByTag",
  props: {
    SearchTagList: Array
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters({
      getSearchTagListName: "campStore/getSearchTagListName"
    })
  }
};
</script>
<style scoped>
.campsiteList {
  margin: 0 auto;
}
.minibox {
  display: block;
  width: 72%;
  /* position: absolute; */
  left: 14%;
  margin-top: 0%;
  padding-bottom: 7%;
}
</style>
