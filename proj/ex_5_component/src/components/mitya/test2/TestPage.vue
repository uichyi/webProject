<template>
    <div class="test-page">
      <p>Осталось времени: {{ timer }} сек</p>
      <div class="game-container">
    <p class="word" :style="{ color: firstWordColor }">{{ firstWord }}</p>
      <p class="word" :style="{ color: secondWordColor }">{{ secondWord }}</p>
    </div>
      <div>
        <button @click="checkAnswer(true)">Да</button>
        <button @click="checkAnswer(false)">Нет</button>
      </div>

    </div>
  </template>
  
  <script>
  export default {
    name: "TestPage",
    props: ["firstWordColor", "timer", "secondWordColor", "firstWord", "secondWord"],
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
  .game-container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  gap: 20px;
  margin: 20px;
}
.word {
  font-size: 24px;
  font-weight: bold;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  text-align: center;
  margin-top: auto;
  margin: auto;
  width: 150px;
  text-align: center;
  justify-content: center;
}
</style>