<template>
  <div id="header">
    <img src="../assets/logo.png" width="300" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Header",
});
</script>

<style scoped>
#header {
  display: flex;
  flex-direction: column;
  flex-grow: 0.10;

  justify-content: center;
  align-items: center;

  margin-top: 10px;
}

img {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>
