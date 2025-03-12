<template>
  <div v-if="error" class="col-lg-12">
    <sdx-card
      layout="notification"
      notification-type="alert"
      icon-name="icon-exclamation-mark-circle"
      label-aria-level="4"
      :label="error"
    />
  </div>
</template>

<script>
export default {
  props: {
    error: String,
  },
};
</script>
