<template>
    <div class="start-page">
      <h1>Тренажер №3: Тест на гибкость мозга</h1>
      <h2>Правила игры.</h2>
      <p>Название цвета на верху должно соответствовать цвету текста внизу.</p>
      <p>За 60 секунд ответьте, соответсвует ли?</p>
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