<template>
    <div class="puzzle-game">
      <div>
        <h1>Пятнашки</h1>
        <input type="file" @change="uploadImage" accept="image/*" />
        <select v-model="gridSize" @change="initializeGame">
          <option value="3">3x3</option>
        </select>
      </div>
      <div
  v-if="imageLoaded"
  class="puzzle-grid"
  :style="{ 
    width: '400px',
    height: '400px',
    gridTemplateColumns: `repeat(${gridSize}, 1fr)`,
    gridTemplateRows: `repeat(${gridSize}, 1fr)`
  }"
>
  <div
    v-for="(piece, index) in shuffledPieces"
    :key="index"
    :class="['puzzle-piece', { empty: piece.empty }]"
    :style="getPieceStyle(piece)"
    @click="movePiece(index)"
  ></div>
</div>
      <div v-if="gameWon" class="win-message">
        <h2>Поздравляем! Вы победили!</h2>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";

  export default {
    data() {
      return {
        gridSize: 3,
        imageSrc: null,
        pieces: [],
        shuffledPieces: [],
        emptyIndex: null,
        imageLoaded: false,
        gameWon: false,
        imageWidth: 0,
        imageHeight: 0,
        testId: 24
      };
    },
    methods: {
        uploadImage(event) {
          const file = event.target.files[0];
          if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
              const img = new Image();
              img.onload = () => {
                this.imageWidth = img.width;
                this.imageHeight = img.height;

                this.imageSrc = e.target.result;
                this.imageLoaded = true;

                if (this.imageWidth > this.imageHeight) {
                  this.imageHeight = (this.imageHeight / this.imageWidth) * 400;
                  this.imageWidth = 400;
                } else {
                  this.imageWidth = (this.imageWidth / this.imageHeight) * 400;
                  this.imageHeight = 400;
                }

                this.initializeGame();
              };
              img.src = e.target.result;
            };
            reader.readAsDataURL(file);
          }
        },
      initializeGame() {
        this.pieces = [];
        const totalPieces = this.gridSize * this.gridSize;

        const pieceWidth = this.imageWidth / this.gridSize;
        const pieceHeight = this.imageHeight / this.gridSize;
  
        for (let i = 0; i < totalPieces - 1; i++) {
          const col = i % this.gridSize;
          const row = Math.floor(i / this.gridSize);
  
          this.pieces.push({
            index: i,
            x: col * pieceWidth,
            y: row * pieceHeight,
            empty: false,
          });
        }
  
        this.pieces.push({
          index: totalPieces - 1,
          x: null,
          y: null,
          empty: true,
        });
  
        this.shufflePieces();
      },
      shufflePieces() {
        const piecesCopy = [...this.pieces];
        do {
          for (let i = piecesCopy.length - 1; i > 0; i--) {
            const randomIndex = Math.floor(Math.random() * (i + 1));
            [piecesCopy[i], piecesCopy[randomIndex]] = [piecesCopy[randomIndex], piecesCopy[i]];
          }
        } while (!this.isSolvable(piecesCopy));
  
        this.shuffledPieces = piecesCopy;
        this.emptyIndex = this.shuffledPieces.findIndex((piece) => piece.empty);
        this.gameWon = false;
      },
      isSolvable(pieces) {
        const flattened = pieces.filter((p) => !p.empty).map((p) => p.index);
        let inversions = 0;
        for (let i = 0; i < flattened.length; i++) {
          for (let j = i + 1; j < flattened.length; j++) {
            if (flattened[i] > flattened[j]) {
              inversions++;
            }
          }
        }
        if (this.gridSize % 2 === 1) {
          return inversions % 2 === 0;
        } else {
          const emptyRow = Math.floor(this.emptyIndex / this.gridSize);
          return (inversions + emptyRow) % 2 === 0;
        }
      },
      getPieceStyle(piece) {
        if (piece.empty) {
          return {
            width: '100%',
            height: '100%',
            backgroundColor: '#f0f0f0',
          };
        }
        const pieceWidth = 400 / this.gridSize;
        const pieceHeight = 400 / this.gridSize;

        return {
          width: `${pieceWidth}px`,
          height: `${pieceHeight}px`,
          backgroundImage: `url(${this.imageSrc})`,
          backgroundSize: `400px 400px`,
          backgroundPosition: `${-piece.x * (400 / this.imageWidth)}px ${-piece.y * (400 / this.imageHeight)}px`,
        };
      },
      movePiece(index) {
        if (this.isAdjacent(index, this.emptyIndex)) {
          [this.shuffledPieces[index], this.shuffledPieces[this.emptyIndex]] = [
            this.shuffledPieces[this.emptyIndex],
            this.shuffledPieces[index],
          ];
          this.emptyIndex = index;
  
          if (this.checkWin()) {
            this.saveTestResult();
            this.gameWon = true;
          }
        }
      },
      isAdjacent(index1, index2) {
        const row1 = Math.floor(index1 / this.gridSize);
        const col1 = index1 % this.gridSize;
        const row2 = Math.floor(index2 / this.gridSize);
        const col2 = index2 % this.gridSize;
        return (row1 === row2 && Math.abs(col1 - col2) === 1) || (col1 === col2 && Math.abs(row1 - row2) === 1);
      },
      checkWin() {
          return this.shuffledPieces.every((piece, index) => piece.index === index);
      },
      async saveTestResult() {
        const testResultData = {
          'user': localStorage.getItem('user_id'),
          "test": this.testId,
          "number_correct_answers": 1,
        };
        console.log(testResultData);

        try {
          const response = await axios.post(
            'http://localhost:8000/api/test-results/create/',
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
  };
  </script>
  
  <style scoped>
  .puzzle-game {
    max-width: 400px;
    margin: 0 auto;
    text-align: center;

    height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  }
  
  .puzzle-grid {
  display: grid;
  margin: 20px auto;
  border: 1px solid #ccc;
  width: 400px;
  height: 400px;
  position: relative;
  background-color: #f9f9f9;
  overflow: hidden;
}

.puzzle-piece {
  cursor: pointer;
  background-repeat: no-repeat;
  box-sizing: border-box;
}

.puzzle-piece.empty {
  background-color: #f0f0f0;
  cursor: default;
}
  .win-message {
    margin-top: 20px;
    font-size: 1.5em;
    color: green;
  }
  </style>