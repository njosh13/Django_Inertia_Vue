<template>
  <div v-for="event in events">
    <p>Event Name: "{{ event.name }}".</p>
    <p>Event Date: {{ event.date }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  events: Object,
});
</script>
