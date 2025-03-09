<!-- StartScreen.vue -->
<template>
    <div id="appp">
      <div class="navbarr">
        <RedButton />
      </div>
      <div v-if="!gameStarted" class="start-screen">
        <h1 class="start-title">Название и цвет совпадают</h1>
        <p class="start-description">
          Выбери квадраты, в которых название цвета совпадает с цветом их квадрата.
        </p>
        <button class="start-button" @click="startGame">Начать</button>
      </div>
      <Game v-else />
    </div>
  </template>
  
  <script>
  import Game from './Rectangles.vue'; // Import the game component
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
  #appp {
  margin: 0 auto;
  padding: 2rem;

  height: 100vh;
  width: 100vw;
  display: grid;
  grid-template-rows: auto 1fr;
  justify-content: center;
  align-items: center; 
}

  .start-screen {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    /* min-height: 100vh; */
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
  