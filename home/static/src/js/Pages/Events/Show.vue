<template>
  <div class="container">
    <div class="card mt-5">
      <h5 class="card-header">{{ event.name }}</h5>
      <div class="card-body">
        <h5 class="card-title">{{ event.date }}</h5>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  event: Object,
});
</script>
