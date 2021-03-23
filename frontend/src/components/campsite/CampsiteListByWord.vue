<template>
<<<<<<< HEAD
  <div>
    <div
     v-for="(item, index) in tagList" :key="index">
      <swipertest :tag="item" /> 

    </div>

  </div>
</template>

<script>
import 'swiper/swiper-bundle.css'
import swipertest from '@/components/campsite/swipertest'


export default {
  components: {
    swipertest
  },
  data: function() {
    return {
      tagList: ['야경이 좋은 곳', '아이들이랑 가고 싶은 곳', '산책하기 좋은 곳'],
      swiperOption: {
        direction: 'vertical',
        pagination: {
          el: '.swiper-pagination',
          type: 'bullets',
        },
      },
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add('large');
    },
  },
  created: async function() {
    console.log(this.tagList[0]);
  },
};
</script>

<style>

</style>
<style scoped>
.swiper-slide {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.swiper-container {
  height: 500px;
}
</style>
=======
    <div>
        <p>검색결과</p>

        <b-form-group v-slot="{ ariaDescribedby }">
        <b-form-checkbox-group
            id="checkbox-group-1"
            v-model="selected"
            :options="options"
            :aria-describedby="ariaDescribedby"
            name="flavour-1"
        ></b-form-checkbox-group>
        </b-form-group>
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
        ]
      }
    }
}
</script>
>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8
