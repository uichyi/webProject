<script setup>
const emits = defineEmits(["handleClick"]);

const handleClick = () => {
  emits("handleClick", "countdown");
};
</script>

<template>
  <div class="startWrapper">
    <h2>Тест на запоминание чисел !</h2>
    <p>
      Тест на запоминание чисел - это простая игра на память. Все, что вам нужно
      сделать, это запомнить числа, которые вы видите в каждом раунде, и повторить
      последовательность от 1 до наибольшего числа после того, как они исчезнут.
    </p>
    <button @click="handleClick">Начать</button>
  </div>
</template>

<style scoped>
.startWrapper {
  max-width: 800px; 
  /* height: 100vh; */
  text-align: center;
  display: grid;
  place-content: center;
}
</style>