<template>
  <div class="container">
    <div class="card mt-5" v-for="event in events">
      <h5 class="card-header">
        <Link :href="route('home:single_event', event.id)">{{ event.name }} </Link>
      </h5>
      <div class="card-body">
        <h5 class="card-title">{{ event.date }}</h5>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  events: Object,
});
</script>
