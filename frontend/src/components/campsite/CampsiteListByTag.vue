<template>
    <div>
        <h3>검색결과</h3>

        <b-form-group v-slot="{ ariaDescribedby }">
        <b-form-checkbox-group
            id="checkbox-group-1"
            v-model="selected"
            :options="options"
            :aria-describedby="ariaDescribedby"
            name="flavour-1"
            size="lg"
        ></b-form-checkbox-group>
        </b-form-group>

        <!-- b-card -->
        <div class="campsiteList">
          <b-row class="text-center">
      <div class="card mb-4 " style="width: 33%;"
      v-for="(item, index) in campsiteList" :key="index">
   
        <img height="90%" width="100%" src="@/assets/SearchPageImage2.jpg" />
        
          <h6 class="card-title" >A캠핑장</h6>
          <p class="card-text" >강원도 춘천시</p>

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

    </div>
</template>
<script> 
export default {
    name: 'CampsiteListByTag',
    data() {
      return {
        selected: [], // Must be an array reference!
        options: [
          { text: '부대시설1', value: '부대시설1' },
          { text: '부대시설2', value: '부대시설2' },
          { text: '부대시설3', value: '부대시설3' },
          { text: '부대시설4', value: '부대시설4' },
          { text: '부대시설5', value: '부대시설5' },
        ],
        campsiteList: [1, 2, 3, 4, 5, 6],
      }
    }
}
</script>
<style scoped>
.campsiteList {
  margin: 0 auto;
}
</style>