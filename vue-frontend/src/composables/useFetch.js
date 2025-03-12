import { ref } from 'vue';
import apiClient from '@/api/axios';

export function useFetch(url) {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);

  const fetchData = async () => {
    isLoading.value = true;
    error.value = null;

    try {
      const response = await apiClient.get(url);
      data.value = response.data;
    } catch (err) {
      error.value = 'Failed to load data. Please try again later.';
      console.error('Fetch error:', err);
    } finally {
      isLoading.value = false;
    }
  };

  return { data, error, isLoading, fetchData };
}
