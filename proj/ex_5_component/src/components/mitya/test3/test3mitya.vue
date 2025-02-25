<template>
  <div class="game">
    <h1>Игра на реакцию</h1>
    <p v-if="!isPlaying & !gameOver">
      Нажмите "Начать игру", чтобы проверить вашу реакцию. У вас есть 60 секунд!
    </p>
    <button v-if="!isPlaying & !gameOver" @click="startGame">Начать игру</button>

    <div v-if="isPlaying">
      <p>Осталось времени: {{ timeLeft }} секунд</p>
      <p>Очки: {{ score }}</p>
      
      <div class="matrix">
        <div
          v-for="(cell, index) in matrix"
          :key="index"
          :class="['cell', { active: activeCell === index }]"
          @click="handleClick(index)"
        ></div>
      </div>
    </div>

    <div v-if="gameOver" class="game-over">
      <h2>Игра окончена!</h2>
      <p>Ваш результат: {{ score }} очков</p>
      <button @click="resetGame">Начать заново</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isPlaying: false,
      gameOver: false,
      timeLeft: 60,
      score: 0,
      matrix: Array(28).fill(0),
      activeCell: null,
      timer: null,
      autoChangeTimer: null,
    };
  },
  methods: {
    startGame() {
      this.resetGame();
      this.isPlaying = true;

      this.timer = setInterval(() => {
        this.timeLeft--;
        if (this.timeLeft <= 0) {
          this.endGame();
        }
      }, 1000);

      this.spawnActiveCell();
    },
    spawnActiveCell() {
      this.activeCell = Math.floor(Math.random() * this.matrix.length);

      clearTimeout(this.autoChangeTimer);
      this.autoChangeTimer = setTimeout(this.spawnActiveCell, 1500);
    },
    handleClick(index) {
      if (this.activeCell === index) {
        this.score++; 
        this.spawnActiveCell();
      }
    },
    endGame() {
      clearInterval(this.timer);
      clearTimeout(this.autoChangeTimer);
      this.isPlaying = false;
      this.gameOver = true;
    },
    resetGame() {
      clearInterval(this.timer);
      clearTimeout(this.autoChangeTimer);
      this.isPlaying = false;
      this.gameOver = false;
      this.timeLeft = 10;
      this.score = 0;
      this.activeCell = null;
    },
  },
};
</script>

<style scoped>
.game {
  text-align: center;
  font-family: Arial, sans-serif;
}
button {
  padding: 10px 20px;
  font-size: 16px;
  margin: 20px;
}
.matrix {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-gap: 5px;
  margin-left: 37% ;
  width: 250px;
}
.cell {
  width: 50px;
  height: 50px;
  background-color: blue;
  border: 2px solid #000;
  cursor: pointer;
}
.cell.active {
  background-color: pink;
}
.game-over {
  margin-top: 20px;
}
</style>