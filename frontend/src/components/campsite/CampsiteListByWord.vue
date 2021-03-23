<template>
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
  name: "CampsiteListByTag",
  data() {
    return {
      selected: [], // Must be an array reference!
      options: [
        { text: "부대시설1", value: "부대시설1" },
        { text: "부대시설2", value: "부대시설2" },
        { text: "부대시설3", value: "부대시설3" },
        { text: "부대시설4", value: "부대시설4" },
        { text: "부대시설5", value: "부대시설5" }
      ]
    };
  }
};
</script>
