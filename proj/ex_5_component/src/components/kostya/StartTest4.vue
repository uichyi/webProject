<!-- StartScreen.vue -->
<template>
    <RedButton/>
    <div v-if="!gameStarted" class="start-screen">
      <h1 class="start-title">Сравнение чисел</h1>
      <p class="start-description">
        Определи какой знак: больше, меньше или равно нужно поставить между числами, чтобы получилось верное утверждение. Нажмите на кнопку ниже, чтобы начать игру!
      </p>
      <button class="start-button" @click="startGame">Начать</button>
      <p>Последняя попытка: ?</p>
      <p>Рекорд: ?</p>
    </div>
    <Game v-else />
  </template>
  
  <script>
  import Game from './Test4.vue'; // Import the game component
  import RedButton from "../navbar/Return.vue";

  export default {
    components: {
      Game,
      RedButton
    },
    data() {
      return {
        gameStarted: false,  // Tracks if the game has started
      };
    },
    methods: {
      startGame() {
        this.gameStarted = true;  // Switch to the game component
      },
    },
  };
  </script>
  
  <style scoped>
  .start-screen {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #f9f9f9;
  }
  
  .start-title {
    font-size: 3rem;
    font-weight: bold;
    color: #6b48ff;
  }
  
  .start-description {
    font-size: 1.2rem;
    margin: 20px 0;
    color: #333;
  }
  
  .start-button {
    background-color: #6b48ff;
    color: white;
    font-size: 1.2rem;
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .start-button:hover {
    background-color: #8a3ffc;
  }
  </style>
  