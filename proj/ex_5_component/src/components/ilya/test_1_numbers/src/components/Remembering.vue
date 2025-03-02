<script setup>
import { ref, onMounted } from "vue";

const props = defineProps({
  currentState: String,
  currentLevel: Number,
  grid: Array,
});

const emit = defineEmits(["updateCurrentState", "updateGrid"]);

const totalCells = 30;
const filledCells = props.currentLevel;

let cells = Array(totalCells).fill(null);

const generateGrid = () => {
  const valuesToEmbed = new Set(
    Array.from({ length: props.currentLevel }, (_, index) => index + 1)
  );

  const indices = new Set();

  while (indices.size < filledCells) {
    indices.add(Math.floor(Math.random() * totalCells));
  }

  indices.forEach((index, i) => {
    const randomValue = [...valuesToEmbed][
      Math.floor(Math.random() * valuesToEmbed.size)
    ];
    cells[index] = randomValue;
    valuesToEmbed.delete(randomValue);
  });

  updateGrid(cells);
};

onMounted(() => {
  generateGrid();

  setTimeout(() => {
    emit("updateCurrentState", "guessing");
  }, 3000);
});

const updateGrid = (c) => {
  emit("updateGrid", c);
};
</script>

<template>
  <h2>Пожалуйста, запомните расположение чисел ниже...</h2>

  <div class="gridWrapper">
    <div class="grid">
      <div v-for="(cell, index) in grid" :key="index" class="cell">
        <span>{{ cell !== null ? cell : "" }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.gridWrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.grid {
  display: grid;
  grid-template-columns: repeat(
    6,
    1fr
  ); /* Adjust number of columns as needed */
  grid-template-rows: repeat(5, 1fr); /* Adjust number of rows as needed */
  max-width: 600px;
  width: 100%;
  max-height: 500px; /* Optional: to limit the height */
  height: 100%;
  justify-content: center;
  align-content: center;
  justify-items: center;
  align-items: center;
}

.cell {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f0f0;
  color: #333;
  border: 1px solid #ccc;
  font-size: 3rem;
  font-weight: bold;
  position: relative;
  padding-top: 100%; /* This creates a square aspect ratio */
  width: 100%; /* Fill the parent width */
  height: 0; /* Allow padding-top to define the height */
  max-width: 100%;
  user-select: none;
  box-sizing: border-box; /* Include padding and border in the total width/height */

  display: flex;
  align-items: center;
  justify-content: center;
}

.cell > span {
  margin-bottom: 100%;
}

.cell.hidden {
  background-color: #333;
}

.cell.hidden:hover {
  cursor: pointer;
}

button {
  margin-bottom: 20px;
}

@media (width < 800px) {
  .cell {
    font-size: 2rem;
  }
}
</style>

