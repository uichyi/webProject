<template>
    <div id="appp">
      <div class="navbarr">
        <RedButton />
      </div>
      <div class="game">
        <p>Время: {{ remainingTime }} секунд</p>
        <p v-if="!first_start">Будет дана матрица 9х9 из чисел (от 1 до 9). Необходимо будет отметить такой набор чисел, который в сумме будет давать указанное число.</p>
        <button v-if="!first_start" @click="startGame">Начать</button>
        <div v-if="gameOver & first_start" class="game-over">
          <h2>Игра завершена!</h2>
          <p>Ваши очки: {{ score }}</p>
          <button @click="startGame">Начать заново</button>
        </div>
        <div v-else>
          <button v-if="first_start" @click="startGame">Начать игру заново</button>
          <h1>Сумма: {{ targetSum }}</h1>
          <div class="matrix">
            <div v-for="(row, rowIndex) in matrix" :key="rowIndex" class="row">
              <div
                v-for="(cell, colIndex) in row"
                :key="colIndex"
                class="cell"
                :class="getCellClass(rowIndex, colIndex)"
                @click="selectCell(rowIndex, colIndex)"
              >
                {{ cell }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import RedButton from "../../navbar/Return.vue";

  export default {
    components: {
    RedButton
  },
    data() {
      return {
        matrix: [],
        availableNumbers: [],
        selectedCells: [],
        targetSum: null,
        score: 0,
        remainingTime: 100,
        gameOver: false,
        isGameStarted: false,
        timer: null,
        indexes_used: [],
        testic: {},
        values: [],
        first_start: false,
        testId: 25
      };
    },
    methods: {
      generateMatrix() {
        const matrix = [];
        for (let i = 0; i < 9; i++) {
          const row = [];
          for (let j = 0; j < 9; j++) {
            const num = Math.floor(Math.random() * 9) + 1;
            row.push(num);
            this.availableNumbers.push([num, 3]);
          }
          matrix.push(row);
        }
        return matrix;
      },
      generateTargetSum() {
        let numCount = Math.floor(Math.random() * 4) + 2;
        if (numCount > this.values.length & this.values.length != 0){
          numCount = this.values.length
        }
        const selectedNumbers = [];
        this.values = Object.values(this.testic);
        if (this.values.length == 1){
          return this.values[0]
        }
        for (let i = 0; i < numCount; i++) {
          if (this.values.length === 0) break;
          let randomIndex = Math.floor(Math.random() * this.values.length);
          selectedNumbers.push(this.values[randomIndex]);
          this.values.splice(randomIndex, 1);
        }
        let sum2 = selectedNumbers.reduce((acc, val) => acc + val, 0);
        if (sum2 === null) this.checkGameOver()
        return sum2;
      },
      startGame() {
        this.first_start = true;
        this.isGameStarted = true;
        this.resetGame();
      },
      selectCell(row, col) {
        
        if (this.gameOver || this.matrix[row][col] === null) return;
  
        const cellIndex = this.selectedCells.findIndex(
          ([r, c]) => r === row && c === col
        );
        const index4 = row *9 + col;

        if (cellIndex !== -1) {
          this.selectedCells.splice(cellIndex, 1);
          this.indexes_used.pop(index4);
        } else {
          this.selectedCells.push([row, col]);
          this.indexes_used.push(index4); 
        }
  
        const sum = this.selectedCells.reduce(
          (total, [r, c]) => total + this.matrix[r][c],
          0
        );

        if (sum > this.targetSum) {
          this.indexes_used.pop(index4);
          alert("Сумма больше указанного числа. Попробуйте снова!");
          this.resetSelection();
        } else if (sum === this.targetSum) {
          this.markCellsAsUsed();
          this.score++;
          for (let i =0; i<this.indexes_used.length; i++){
            let a = this.indexes_used[i] 
            delete this.testic[a]
          }
          this.targetSum = this.generateTargetSum();
          this.resetSelection();
          this.indexes_used = [];
        }
        this.checkGameOver();
      },
  
      getCellClass(row, col) {
        if (this.matrix[row][col] === null) {
          return "used";
        }
  
        if (this.selectedCells.some(([r, c]) => r === row && c === col)) {
          return "selected";
        }
  
        return "";
      },
  
      resetSelection() {
        this.selectedCells = [];
      },
      markCellsAsUsed() {
        this.selectedCells.forEach(([row, col]) => {
          this.matrix[row][col] = null; 
        });
      },
  
      resetGame() {
        if (this.timer) clearInterval(this.timer);
        this.matrix = this.generateMatrix();
        this.availableNumbers = [...this.matrix.flat()];
        this.testic = JSON.stringify(Object.assign({}, this.availableNumbers))
        this.testic = JSON.parse(this.testic)
        
      this.targetSum = this.generateTargetSum();
      this.score = 0;
      this.remainingTime = 100;
      this.gameOver = false;
      this.startTimer();
    },

    startTimer() {
      this.timer = setInterval(() => {
        if (this.remainingTime > 0) {
          this.remainingTime--;
        } else {
          this.gameOver = true;
          clearInterval(this.timer);
          this.checkGameOver();
        }
      }, 1000);
    },

    checkGameOver() {
        if (this.values.length === 0 || this.remainingTime <= 0) {
        this.gameOver = true;
        this.saveTestResult();
        clearInterval(this.timer);
        }
    },
    async saveTestResult() {
      const testResultData = {
        'user': localStorage.getItem('user_id'),
        "test": this.testId,
        "number_correct_answers": this.score,
        "complete_time": 10 - this.remainingTime,
      };
      console.log(testResultData);

      try {
        const response = await axios.post(
          '/test-results/create/',
          testResultData,
          {
            headers: { 'Content-Type': 'application/json' }
          }
        );
        console.log('Результат теста сохранен:', response.data);
      } catch (error) {
        console.error('Ошибка при сохранении результата:', error);
      }
    },
  },
  beforeDestroy() {
    if (this.timer) clearInterval(this.timer);
  },
};
</script>

<style scoped>
  #appp {
      height: 100vh;
      width: 100vw;
      display: grid;
      grid-template-rows: auto 1fr;
      justify-content: center;
      align-items: center; 
  }
.game {
  text-align: center;

  /* height: 100vh; */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.matrix {
  display: grid;
  grid-template-columns: repeat(9, 50px); /* 9 columns, each 50px wide */
  grid-template-rows: repeat(9, 50px); /* 9 rows, each 50px tall */
  gap: 1rem; /* Add a gap between the cells */
  justify-content: center; /* Center the grid horizontally */
  margin-top: 20px;
}

.cell {
  border: 1px solid black;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f0f0f0;
  cursor: pointer;
  font-size: 20px;
  box-sizing: border-box; /* Prevents padding from affecting the size */
}

.cell.selected {
  background-color: #ffeb3b;
}

.cell.used {
  background-color: #9e9e9e;
  cursor: not-allowed;
}

button {
  margin-top: 20px;
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.game-over {
  margin-top: 20px;
  font-size: 24px;
}

</style>