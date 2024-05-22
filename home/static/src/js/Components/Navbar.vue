<template>
  <!-- Navigation-->
  <nav class="navbar navbar-light bg-light static-top">
    <div class="container">
      <a class="navbar-brand" href="#!">Start Bootstrap</a>
      <a class="btn btn-primary" href="#signup">Sign Up</a>
      <Link class="btn-indigo ml-1" :href="route('home:events')"> Events</Link>
    </div>
  </nav>
</template>

<script setup></script>
