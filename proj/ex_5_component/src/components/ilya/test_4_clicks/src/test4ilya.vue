<script setup>
import Game from "./components/Game.vue";
import Start from "./components/Start.vue";
import Results from "./components/Results.vue";
import { ref } from "vue";
import axios from "axios";

const gameState = ref("start");
const results = ref([]);
const duration = ref(1);
const testId = 14;

const setDuration = (value) => {
  duration.value = value;
};

const menu = () => {
  gameState.value = "start";
};

const startGame = () => {
  gameState.value = "game";
  console.log("startGAme");
};

async function saveTestResult(value) {
    const testResultData =
      {
        'user': localStorage.getItem('user_id'),
        "test": testId,
        "accuracy": value,
      };
    console.log(testResultData)
      axios.post(
        '/test-results/create/',
        testResultData,
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      ).then(response => {
        console.log('Результат теста сохранен:', response.data);
      }
      ).catch(error => {
        console.error('Ошибка при сохранении результата:', error);
      }
      );
}

const gameOver = (value) => {
  gameState.value = "gameover";
  saveTestResult(value);
  results.value.push(value);
};
</script>

<template>
  <div class="wrapper">
    <div class="navbarr">
      <RedButton />
    </div>
    <div v-if="gameState === 'start'">
      <Start @startGame="startGame" @setDuration="setDuration"></Start>
    </div>
    <div v-if="gameState === 'game'">
      <Game @gameIsOver="gameOver" :duration="duration"></Game>
    </div>
    <div v-if="gameState === 'gameover'">
      <Results :results="results" @startGame="menu"></Results>
    </div>
  </div>
</template>


<script> 
import RedButton from "../../../navbar/Return.vue";
export default {
  components: {
    RedButton
  }
}
</script>

<style scoped>
.wrapper {
  height: 100vh;
  width: 100vw;
  display: grid;
  grid-template-rows: auto 1fr;
  justify-content: center;
  align-items: center;
}

.wrapper > * {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
