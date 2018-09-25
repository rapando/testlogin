<template>
    <div>
        Movies Page
    </div>
</template>

<script>
import router from "../../router";
export default {
  name: "Movies",
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    }
  }
};
</script>
