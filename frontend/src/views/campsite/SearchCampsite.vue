<template>
  <div>
    <!-- 태그 검색 -->
    
    <SearchCampsiteByTag @IsTag="parents" v-if="IsTag" />
<<<<<<< HEAD
    <SearchCampsiteByWord @IsTag="parents" v-else-if="!IsTag" />
 
    <CampsiteListByTag v-if="IsTag"/>
    <CampsiteListByWord v-else-if="!IsTag"/>
=======
    <SearchCampsiteByWord v-else-if="!IsTag" />
    {{ IsTag }}

    <CampsiteListByTag />
    <CampsiteListByWord />
>>>>>>> 88cfdcf79a570418e42c9b4b8f95772101810bba
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
