<script setup>
import { ref, onMounted } from "vue";
const props = defineProps(["currentState"]);
const emit = defineEmits(["updateCurrentState"]);

const endCountdown = () => {
  emit("updateCurrentState", "remembering");
};

const countdownValue = ref(3);

onMounted(() => {
  const interval = setInterval(() => {
    if (countdownValue.value > 1) {
      countdownValue.value -= 1;
    } else {
      clearInterval(interval);
      endCountdown();
    }
  }, 1000);
});
</script>

<template>
  <div class="countdownWrapper">
    <h2>Пожалуйста, подождите...</h2>
    <h1>{{ countdownValue }}</h1>
  </div>
</template>

<script></script>

<style scoped>
.countdownWrapper {
  max-width: 800px; 
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
