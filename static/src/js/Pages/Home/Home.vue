<template>
  <p>props: {{ props }}</p>
</template>

<script setup>
const props = defineProps({
  clients: Object,
});
</script>
