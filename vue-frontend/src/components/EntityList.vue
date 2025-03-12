<template>
  <sdx-loading-spinner v-if="isLoading" />
  <ErrorCard :error="error" />

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
import ErrorCard from '@/components/ErrorCard.vue';
import { onMounted } from 'vue';
import { useFetch } from '@/composables/useFetch.js';

export default {
  components: {
    CustomButton,
    ErrorCard,
  },
  data() {
    return {
      entities: null,
      error: null,
      isLoading: false,
    };
  },
  setup() {
    let { data: entities, error, isLoading, fetchData } = useFetch('/api/dataset_entities_list');
    onMounted(fetchData);
    return { entities, error, isLoading };
  },
};
</script>
