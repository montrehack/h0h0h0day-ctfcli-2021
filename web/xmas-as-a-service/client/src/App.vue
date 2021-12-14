<template>
  <Header />
  <Body />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Body from "./components/Body.vue";
import Header from "./components/Header.vue";

export default defineComponent({
  name: "App",
  components: {
    Header,
    Body,
  },
});
</script>

<style>

html {
  background-image: url("./assets/background.png");
  background-size: cover;
}

html,
body {
  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #ffffff;
  text-shadow: -2px 0 black, 0 2px black, 2px 0 black, 0 -2px black;
  -webkit-font-smoothing: antialiased;

  display: flex;
  flex-direction: column;
  width: 100%;
  min-height: 100%;
}
</style>
