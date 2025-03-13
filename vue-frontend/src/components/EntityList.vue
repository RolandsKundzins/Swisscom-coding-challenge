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
    <sdx-button
      theme="primary"
      :label="isMoreData ? 'Load more' : 'No more data'"
      :disabled="!isMoreData"
      :loading="isLoading"
      @click="loadMore"
    />
  </div>
</template>

<script>
import CustomButton from '@/components/CustomButton.vue';
import ErrorCard from '@/components/ErrorCard.vue';
import { onMounted, ref } from 'vue';
import { useFetch } from '@/composables/useFetch.js';

export default {
  components: {
    CustomButton,
    ErrorCard,
  },
  setup() {
    // If need to use the request in multiple components in the same page, should use Pinia
    const { data: entities, error, isLoading, nextScrollId, fetchData } = useFetch('/api/dataset_entities_list');
    const isMoreData = ref(true);

    onMounted(fetchData);

    const loadMore = () => {
      if (!nextScrollId.value) {
        isMoreData.value = false;
        return;
      }

      fetchData(nextScrollId.value);
      if (nextScrollId.value) isMoreData.value = false;
    };

    return { entities, error, isLoading, nextScrollId, isMoreData, loadMore };
  },
};
</script>
