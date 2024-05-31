<template>
  <div class="container">
    <form @submit.prevent="submit">
      <div class="form-group">
        <label for="exampleInputEmail1">Name</label>
        <input v-model="form.name" type="text" class="form-control" id="name" placeholder="Enter name" />
        <p class="text-danger">{{ form.errors.name }}</p>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Date</label>
        <input v-model="form.date" type="date" class="form-control" id="date" placeholder="Date" />
        <p class="text-danger">{{ form.errors.date }}</p>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { useForm, router } from "@inertiajs/vue3";
import { useGlobals } from "../../globals.js";

// Access the global properties
const { route } = useGlobals();

const props = defineProps({
  event: Object,
});

const editMode = props.event ? true : false;

const form = useForm({
  name: editMode ? props.event?.name : "",
  date: editMode ? props.event?.date : "",
});

const submit = () => {
  if (!editMode) form.post(route("home:create_event"));
  else form.post(route("home:edit_event", props.event.id));
};
</script>
