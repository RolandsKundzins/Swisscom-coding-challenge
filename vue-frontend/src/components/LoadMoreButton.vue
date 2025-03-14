<template>
  <sdx-button
    theme="primary"
    :label="isMoreData ? 'Load more' : 'No more data'"
    :disabled="!isMoreData"
    :loading="isLoading"
    @click="loadMore"
  />
</template>

<script>
export default {
  props: {
    isMoreData: Boolean,
    isLoading: Boolean,
    loadMore: Function,
  },
};
</script>
