<template>
  <div class="container">
    <Link class="btn btn-primary" :href="route('home:create_event')">Create New Event</Link>
    <div class="card mt-5" v-for="event in events">
      <h5 class="card-header">
        <Link :href="route('home:single_event', event.id)">{{ event.name }} </Link>
      </h5>
      <div class="card-body">
        <h5 class="card-title">This event will happen on : {{ event.date }}</h5>
        <Link :href="route('home:edit_event', event.id)" class="btn btn-primary">Edit</Link>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  events: Object,
});
</script>
