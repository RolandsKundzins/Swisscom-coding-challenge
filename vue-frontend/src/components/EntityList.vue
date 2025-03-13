<template>
  <ErrorCard :error="error" />

  <div class="row row--gutters">
    <div v-for="entity in entities" :key="entity.urn" class="col-lg-6 col-xl-4">
      <sdx-card :label="entity.name" label-aria-level="2">
        <p>{{ entity.description }}</p>

        <CustomButton :label="entity.platform" />
      </sdx-card>
    </div>
  </div>

  <div class="row row--gutters" style="justify-content: center">
    <LoadMoreButton :isMoreData="isMoreData" :isLoading="isLoading" :loadMore="loadMore" />
  </div>
</template>

<script>
import { onMounted, computed } from 'vue';
import CustomButton from '@/components/CustomButton.vue';
import ErrorCard from '@/components/ErrorCard.vue';
import LoadMoreButton from './LoadMoreButton.vue';
import { useFetch } from '@/composables/useFetch.js';

export default {
  components: {
    CustomButton,
    ErrorCard,
    LoadMoreButton,
  },
  setup() {
    // If you need to use the request in multiple components on the same page, consider using Pinia
    const { data: entities, error, isLoading, nextScrollId, fetchData } = useFetch('/api/dataset_entities_list');

    onMounted(fetchData);

    const isMoreData = computed(() => !!nextScrollId.value);

    const loadMore = () => {
      if (nextScrollId.value) {
        fetchData(nextScrollId.value);
      }
    };

    return { entities, error, isLoading, isMoreData, loadMore };
  },
};
</script>
