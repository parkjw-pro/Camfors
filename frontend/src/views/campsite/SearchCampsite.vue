<template>
    <div>
        <!-- 검색 부분 -->

        
        <!-- <SearchCampsiteByTag /> -->
        <SearchCampsiteByWord />
        
  
        <!-- 검색 결과 -->
        <!-- <CampsiteListByTag /> -->
        <CampsiteListByWord />

    </div>
</template>
<script>
// import SearchCampsiteByTag from '@/components/campsite/SearchCampsiteByTag';
import SearchCampsiteByWord from '@/components/campsite/SearchCampsiteByWord';
// import CampsiteListByTag from '@/components/campsite/CampsiteListByTag';
import CampsiteListByWord from '@/components/campsite/CampsiteListByWord';
export default {
  name: 'SearchCampsite',
  components: {
    // CampsiteListByTag,
    // SearchCampsiteByTag,
    CampsiteListByWord,
    SearchCampsiteByWord
  },
  data() {
      return {
          value: [],
          ByTag: true,
      }
  }
};
</script>
<style scoped>


</style>