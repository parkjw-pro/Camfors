<template>
  <div>
    <div v-for="(item, index) in SearchTagList" :key="index">
      <br />
      <br />
      <h3 style="text-align: left; font-family: 'Hanna', sans-serif; color: black; margin-left: 20px;">
        {{ getSearchTagListName[index] }}
      </h3>
      <ListByTagSwiper :tag="item" :tagName="getSearchTagListName[item]" />
    </div>
  </div>
</template>
<script>
import ListByTagSwiper from '@/components/campsite/ListByTagSwiper';
import { mapGetters } from 'vuex';
export default {
  components: {
    ListByTagSwiper,
  },
  name: 'CampsiteListByTag',
  props: {
    SearchTagList: Array,
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters({
      getSearchTagListName: 'campStore/getSearchTagListName',
    }),
  },
};
</script>
<style scoped>
.campsiteList {
  margin: 0 auto;
}
</style>
