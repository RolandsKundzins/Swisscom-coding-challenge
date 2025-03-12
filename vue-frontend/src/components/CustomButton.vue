<template>
  <div class="custom-button-wrapper">
    <sdx-button class="custom-button" theme="primary" icon-name="icon-database" :label="label" />
  </div>
</template>

<script>
export default {
  props: {
    label: String,
  },
};
</script>

<style scoped>
.custom-button-wrapper {
  display: inline-block;
  border-radius: 1.5rem;
  overflow: hidden; /* Ensures the button inside follows the radius */
}
</style>
