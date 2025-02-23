<template>
    <div class="test-page">
      <p>Осталось времени: {{ timeLeft }} сек</p>
      <h2>{{ currentExpression }}</h2>
      <div>
        <button @click="checkAnswer(true)">Да</button>
        <button @click="checkAnswer(false)">Нет</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "TestPage",
    props: ["currentExpression", "timeLeft"],
    emits: ["answer"],
    methods: {
      checkAnswer(userAnswer) {
        this.$emit("answer", userAnswer);
      },
    },
  };
  </script>
  
  <style scoped>
  .test-page {
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