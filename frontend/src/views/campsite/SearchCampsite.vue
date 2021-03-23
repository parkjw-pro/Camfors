<template>
  <div>
    <!-- 태그 검색 -->

    <SearchCampsiteByTag @IsTag="parents" v-if="(IsTag = true)" />
    <SearchCampsiteByWord v-else-if="(IsTag = false)" />
    {{ IsTag }}

    <CampsiteListByTag />
    <CampsiteListByWord />
  </div>
</template>
<script>
import SearchCampsiteByTag from "@/components/campsite/SearchCampsiteByTag";
import SearchCampsiteByWord from "@/components/campsite/SearchCampsiteByWord";
import CampsiteListByTag from "@/components/campsite/CampsiteListByTag";
import CampsiteListByWord from "@/components/campsite/CampsiteListByWord";
export default {
  name: "SearchCampsite",
  components: {
    CampsiteListByTag,
    SearchCampsiteByTag,
    CampsiteListByWord,
    SearchCampsiteByWord
  },
  data() {
    return {
      value: [],
      IsTag: true
    };
  },
  methods: {
    parents(data) {
      this.IsTag = data;
      console.log(this.IsTag);
    }
  }
};
</script>
<style scoped></style>
