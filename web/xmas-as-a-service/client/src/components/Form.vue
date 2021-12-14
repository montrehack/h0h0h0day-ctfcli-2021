<template>
  <div id="form">
    <div id="inputs">
      <input type="text" placeholder="Image name" v-model="image" />
      <input type="number" placeholder="Port" v-model="port" />
      <input type="submit" value="GO" v-on:click="create" />
    </div>
    <div v-bind:style="{ color: hint.color }" class="hint">
      {{ hint.message }}
    </div>
  </div>
  <pre>{{ output }}</pre>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Form",
  data: function () {
    return {
      image: "",
      port: 80,
      output: "",
      hint: {
        color: "green",
        message: "",
      },
    };
  },
  methods: {
    logger: async function (
      /* global ReadableStreamDefaultReader */
      reader?: ReadableStreamDefaultReader<Uint8Array>,
      wait = false
    ) {
      if (!reader) return () => console.log("canceled null reader");
      const consumer = async () => {
        for (;;) {
          let { done, value } = await reader.read();
          if (done) break;
          this.$data.output += new TextDecoder().decode(value);
        }
      };

      if (wait) await consumer();
      else consumer();

      return () => reader.cancel();
    },
    sleep: async function (ms: number) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    },
    spawn: async function (): Promise<{
      uuid: string;
      port: number;
      exp: number;
    }> {
      this.$data.output = "";
      return await fetch("/api/spawn", {
        method: "POST",
        headers: {
          "content-type": "application/x-www-form-urlencoded",
        },
        body: `name=${encodeURIComponent(
          this.$data.image
        )}&port=${encodeURIComponent(this.$data.port)}`,
      }).then((r) => r.json());
    },
    run: async function (uuid: string) {
      return await fetch("/api/run/" + uuid)
        .then((resp) => resp.body?.getReader())
        .then((reader) => this.logger(reader, true));
    },
    logs: async function (uuid: string) {
      return await fetch("/api/logs/" + uuid)
        .then((resp) => resp.body?.getReader())
        .then(this.logger);
    },
    remove: async function (uuid: string): Promise<void> {
      return await fetch("/api/remove/" + uuid).then(() => {
        console.log("cleaned up");
      });
    },
    health: async function (uuid: string): Promise<string> {
      return await fetch("/api/health/" + uuid).then((resp) => resp.text());
    },
    // This function doesn't work well if there's a proxy involved
    create: async function () {
      try {
        this.$data.hint = {
          color: "inherit",
          message: "",
        };

        const { uuid, port, exp } = await this.spawn();
        this.$data.hint.message = "Starting up image..";
        await this.run(uuid);
        const stopLogs = await this.logs(uuid);

        this.$data.hint.message = "Waiting for container to be healthy..";
        let status = await this.health(uuid);
        while (status === "starting") {
          await this.sleep(2500);
          status = await this.health(uuid);
        }

        if (status === "dead") {
          this.$data.hint = {
            color: "red",
            message:
              "Your image died or doesn't have a healthcheck, please check the logs.",
          };
        } else if (status === "unhealthy") {
          this.$data.hint = {
            color: "yellow",
            message:
              "Your image is unhealthy and cannot be used, please check the logs.",
          };
        } else if (status === "healthy") {
          this.$data.hint = {
            color: "green",
            message:
              "Your image is up and running! Please take note that it will only be available until " +
              new Date(exp).toLocaleString(),
          };
          open(location.protocol + "//" + location.hostname + ":" + port);
        } else {
          this.$data.hint = { color: "red", message: "unexpected " + status };
        }

        if (status !== "healthy") {
          await this.sleep(1000);
          await this.remove(uuid);
        }

        this.$data.output += "<EOF>";
        stopLogs();
      } catch (e) {
        alert(e);
      }
    },
  },
});
</script>

<style scoped>
#form {
  margin-top: 20px;

  display: flex;
  flex-direction: column;
  flex-grow: 1;

  justify-content: center;
  align-items: center;
  
}

.hint {
  text-align: center;
}

#inputs {
  margin-top: 20px;

  display: flex;
  flex-direction: row;
  flex-grow: 1;

  justify-content: center;
  align-items: center;
}

input {
  margin: 5px;
  padding: 10px;
  border-radius: 10px;
  font-family: inherit;
  font-size: inherit;
}

input[type="text"] {
  width: 800%;
}

input[type="number"] {
  width: 100%;
}
</style>
