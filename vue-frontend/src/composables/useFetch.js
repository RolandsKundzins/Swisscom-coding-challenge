import { ref } from 'vue';
import apiClient from '@/api/axios';

// Fetch data from the server - currently only GET method
export function useFetch(baseUrl) {
  const data = ref([]);
  const nextScrollId = ref(null);
  const error = ref(null);
  const isLoading = ref(false);

  const fetchData = async (scrollId = null) => {
    isLoading.value = true;
    error.value = null;

    try {
      const params = scrollId ? { scrollId } : {};
      const response = await apiClient.get(baseUrl, { params });
      data.value = [...data.value, ...response.data.entity_list];
      nextScrollId.value = response.data.next_scroll_id;
    } catch (err) {
      error.value = 'Failed to load data. Please try again later.';
      console.error('Fetch error:', err);
    } finally {
      isLoading.value = false;
    }
  };

  return { data, error, isLoading, nextScrollId, fetchData };
}
