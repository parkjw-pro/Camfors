<template>
  <div>
      <h2>{{ campsiteId }}</h2>
    <!-- <div style="text-align: center; margin : 0 auto; width: 50%;"> -->
<div>디테일 화면입니다.</div>

  </div>
</template>

<script>



export default {
  name: 'CampsiteDetail',
  components: {

  },
  data: function() {
    return {
      campsiteId : '',
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add('large');
    },
  },
  created: async function() {
    this.campsiteId = this.$route.params.campsiteId
  },
};
</script>

<style>

/* 파스텔 컬러 */
.color_red {
  background-color: #f5d5cb;
}

.color_yellow {
  background-color: #f6f6eb;
}

.color_green {
  background-color: #d7ecd9;
}

.color_purple {
  background-color: #d5d6ea;
}
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
