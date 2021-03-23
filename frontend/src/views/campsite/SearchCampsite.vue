<template>
    <div>
        <!-- 검색 부분 -->
<<<<<<< HEAD
        
        <!-- <SearchCampsiteByTag /> -->
        <SearchCampsiteByWord />
        
        
        
        
        <!-- 검색 결과 -->
        <!-- <CampsiteListByTag /> -->
        <CampsiteListByWord />
=======
        <div class="Search">
            <div class=tagGroup>
                <div style="width:50%; margin:0 auto; color:white; font-size:30px;">#추천태그</div><hr>
               <b-btn variant="outline-light">#가족들과 가기 좋은</b-btn>
               <b-btn variant="outline-light">#물놀이 하기 좋은</b-btn>
               <b-btn variant="outline-light">#봄</b-btn>
               <b-btn variant="outline-light">#바다가 보이는</b-btn>
               <b-btn variant="outline-light">#반려견 동반</b-btn>
               <b-btn variant="outline-light">#문화유적</b-btn>
               <b-btn variant="outline-light">#산이 보이는</b-btn>
               <b-btn variant="outline-light">#계곡옆</b-btn>
               <b-btn variant="outline-light">#익스트림</b-btn>
               <b-btn variant="outline-light">#생태교육</b-btn>
               <b-btn variant="outline-light">#별 보기 좋은</b-btn>
                
            </div>
            <div class="searchInput">
                <label for="tags-basic">Type a new tag and press enter</label>
                <b-form-tags input-id="tags-basic" v-model="value"></b-form-tags>
            </div>
        </div>
        
        <!-- 검색 결과 -->
        
        <CampsiteListByTag />
        <div style="height:3000px;"></div>
>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8

    </div>
</template>
<script>
<<<<<<< HEAD
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
=======
import CampsiteListByTag from '@/components/campsite/CampsiteListByTag';
export default {
  name: 'SearchCampsite',
  components: {
    CampsiteListByTag,
>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8
  },
  data() {
      return {
          value: [],
<<<<<<< HEAD
          ByTag: true,
=======
>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8
      }
  }
};
</script>
<style scoped>
<<<<<<< HEAD

=======
.Search{
    width: 100%;
    height: 70vh;
    background-image: url("../../assets/SearchPageImage2.jpg");
    background-repeat: no-repeat; 
    background-size: cover;
    background-position: center; 
    display: flex;
    align-items: center;
    text-align: center;
}
.tagGroup {
    width: 60%;
    top: 20%;
    margin: 0 5%;
}
.searchInput {
    width: 40%;
    float:left;
    margin-right: 5%;
} 

button {
    margin: 0 1% 8px 0;
}
>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8


</style>