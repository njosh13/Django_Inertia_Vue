<template>
  <Navbar />
  <!-- Jumbotron -->
  <div class="p-5 text-center bg-body-tertiary">
    <h1 class="mb-3">
      <img
        src="https://mdbcdn.b-cdn.net/img/logo/mdb-transaprent-noshadows.webp"
        height="50"
        alt="MDB Logo"
        loading="lazy" />
    </h1>
    <h4 class="mb-3">Subheading</h4>
    <a data-mdb-ripple-init class="btn btn-primary" href="" role="button">Call to action</a>
  </div>
  <!-- Jumbotron -->
</template>

<script setup>
import Navbar from "../../Components/Navbar.vue";

const props = defineProps({
  clients: Object,
});
</script>
