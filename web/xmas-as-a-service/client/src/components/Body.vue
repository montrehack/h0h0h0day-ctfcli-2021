<template>
  <div id="body">
    <div id="title">Xmas as a Service</div>
    <div id="subtitle">Run your web gift in a temporarity instance</div>
    <div id="text">*Your gift must run as user 1000 and have a healthcheck</div>
    <Form />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Form from "./Form.vue";

export default defineComponent({
  name: "Body",
  components: {
    Form,
  },
});
</script>

<style scoped>
div {
  text-align: center;
}

#body {
  display: flex;
  flex-direction: column;
  flex-grow: 1;

  align-items: center;
}

#title {
  font-size: 800%;
}

#subtitle {
  font-size: 200%;
}
</style>
