<!-- StartScreen.vue -->
<template>
    <div v-if="!gameStarted" class="start-screen">
      <h1 class="start-title">Emoji Memory Game</h1>
      <p class="start-description">
        Test your memory by matching pairs of emojis. Click the button below to start the game!
      </p>
      <button class="start-button" @click="startGame">Start Game</button>
      <p>Последняя попытка: ?</p>
      <p>Рекорд: ?</p>
    </div>
    <Game v-else />
  </template>
  
  <script>
  import Game from './Test2.vue'; // Import the game component
  
  export default {
    components: {
      Game
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
  