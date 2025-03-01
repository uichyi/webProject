<template>
    <div class="start-page">
      <h1>Тренажер №2: Тест на скорость мозга</h1>
      <h2>Правила игры.</h2>
      <p>Сравните два числа, выражение правильное? Новое выражение будет появляться каждый раз, когда вы ответите. Вы получаете баллы за каждый правильный ответ.</p>
      <p>За 60 секунд ответьте, верны ли выражения</p>
      <button @click="startTest">Начать тест</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "StartPage",
    emits: ["start"],
    methods: {
      startTest() {
        this.$emit("start");
      },
    },
  };
  </script>
  
  <style scoped>
  .start-page {
    text-align: center;
    padding: 20px;
  }
  button {
    margin: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  button:hover {
    background-color: #f0f0f0;
  }
  </style>
  