<template>
  <div class="container padding-v-2">
    <div class="row">
      <div class="col">
        <h1 class="d3">VueJS+Flask Fullstack Example</h1>
        <EntityList />
      </div>
    </div>
  </div>
</template>

<script>
import EntityList from '@/components/EntityList.vue';
import { defineComponent } from 'vue';

export default defineComponent({
  components: {
    EntityList,
  },
});
</script>
