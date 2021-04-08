<template>
  <div>
    <!-- 태그 검색 -->
    <SearchCampsiteByTag @IsTag="parents" v-if="!IsTag" />
    <SearchCampsiteByWord @IsTag="parents" v-else-if="IsTag" />

    <CampsiteListByTag :SearchTagList="getSearchTagList" v-if="!IsTag" />
    <CampsiteListByWord :SearchWordList="getSearchWordList" v-else-if="IsTag" />

    <Footer />
  </div>
</template>
<script>
import SearchCampsiteByTag from "@/components/campsiteSearch/SearchCampsiteByTag";
import SearchCampsiteByWord from "@/components/campsiteSearch/SearchCampsiteByWord";
import CampsiteListByTag from "@/components/campsite/CampsiteListByTag";
import CampsiteListByWord from "@/components/campsite/CampsiteListByWord";
import Footer from "@/components/app/Footer";
import { mapGetters } from "vuex";
export default {
  name: "SearchCampsite",
  components: {
    CampsiteListByTag,
    SearchCampsiteByTag,
    CampsiteListByWord,
    SearchCampsiteByWord,
    Footer
  },
  data() {
    return {
      value: [],
      IsTag: true,
      Isclicked: true,
      flag: true,
      searchTagList: []
    };
  },
  methods: {
    parents(data) {
      this.IsTag = data;
      if (data === true) {
        //  console.log("태그결과화면");
      }
      // console.log(this.IsTag);
    }
    // searched(data) {
    //   console.log(data);
    //   this.flag = !this.flag;
    //   console.log(this.getSearchWordList)
    //   //  $("CampsiteListByTag").load(window.location.href + "CampsiteListByTag");
    // },
  },
  computed: {
    ...mapGetters({
      getSearchTagList: "campStore/getSearchTagList"
    }),
    ...mapGetters({
      getSearchWordList: "campStore/getSearchWordList"
    })
  }
};
</script>
<style scoped></style>
