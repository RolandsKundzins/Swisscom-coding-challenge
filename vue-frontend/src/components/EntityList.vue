<template>
  <template v-if="isLoading">
    <sdx-loading-spinner />
  </template>

  <template v-else-if="error">
    <p class="error">{{ error }}</p>
  </template>

  <div class="row row--gutters">
    <div v-for="entity in entities" :key="entity.urn" class="col-lg-6 col-xl-4">
      <sdx-card :label="entity.name" label-aria-level="2">
        <p>{{ entity.description }}</p>

        <CustomButton :label="entity.platform" />
      </sdx-card>
    </div>
  </div>
</template>

<script>
import CustomButton from '@/components/CustomButton.vue';
import { onMounted } from 'vue';
import { useFetch } from '@/composables/useFetch.js';

export default {
  components: {
    CustomButton,
  },
  data() {
    return {
      entities: null,
      error: null,
      isLoading: false,
    };
  },
  setup() {
    let { data: entities, error, isLoading, fetchData } = useFetch('/api');
    onMounted(fetchData);
    return { entities, error, isLoading };
  },
};
</script>
