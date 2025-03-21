<!-- 
TRK 11-12-2024 Добавил рамку для выбранного эмодзи
-->

<template>
  <div class="container text-center">
    <div v-if="!gameOver">
      <div class="row" v-for="rowIndex in getRowCount" :key="rowIndex">
        <div class="col-3" v-for="(emoji, index) in getRowEmojis(rowIndex)" :key="index">
          <div :class="['emoji'
          , { 'selected-emoji': isSelected(index, rowIndex) } // TRK 11-12-2024
          ]" @click="selectEmoji(index + (rowIndex - 1) * 4)">  
            {{ emoji }}
          </div>
        </div>
      </div>
      <div class="my-2">Счет: {{ score }}</div>
      <div class="my-2">Осталось {{ time }} секунд</div>
    </div>
    <div v-else>
      <h2>Игра окончена, Счет: {{ score }}</h2>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      emojis: this.getRandomEmojis(4),
      firstChoice: null,
      secondChoice: null,
      score: 0,
      time: 60,
      timer: null,
      gameOver: false,
      testId: 1,
    };
  },
  watch: {
    gameOver(newValue) {
      if (newValue) {
        this.saveTestResult();
      }
    },
  },
  computed: {
    getRowCount() {
      return Math.ceil(this.emojis.length / 4);
    }
  },
  methods: {
    async saveTestResult() {
      const testResultData =
      {
        'user': localStorage.getItem('user_id'),
        "test": this.testId,
        "number_correct_answers": this.score,
        "complete_time": 60,
      };
      axios.post
      (
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
    },
    getRowEmojis(rowIndex) {
      const startIndex = (rowIndex - 1) * 4;
      return this.emojis.slice(startIndex, startIndex + 4);
    },
    // TRK 11-12-2024 ->
    isSelected(index, rowIndex) {
      const actualIndex = index + (rowIndex - 1) * 4;
      return actualIndex == this.firstChoice;
    },
    // TRK 11-12-2024 <-
    getRandomEmojis(count) {
      const emojiList = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠', '😈', '👿', '👹', '👺', '🤡', '💩', '👻', '💀', '☠️', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾'];
      const selectedEmojis = [];
      const pairEmoji = emojiList[Math.floor(Math.random() * emojiList.length)];
      selectedEmojis.push(pairEmoji, pairEmoji);
      while (selectedEmojis.length < count) {
        const randomEmoji = emojiList[Math.floor(Math.random() * emojiList.length)];
        if (!selectedEmojis.includes(randomEmoji)) {
          selectedEmojis.push(randomEmoji);
        }
      }
      return this.shuffle(selectedEmojis);
    },
    shuffle(array) {
      for (let i = 0; i < array.length; i++) {
        const j = Math.floor(Math.random() * (array.length - i)) + i;
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
    },
    selectEmoji(index) {
      if (this.firstChoice == null) {
        this.firstChoice = index;
      } else if (this.firstChoice != index) {
        this.secondChoice = index;
        this.checkMatch();
      }
    },
    checkMatch() {
      if (this.emojis[this.firstChoice] == this.emojis[this.secondChoice]) {
        this.score += 1;
        this.increaseEmojiCount();
      }
      this.resetSelection();
    },
    resetSelection() {
      this.firstChoice = null;
      this.secondChoice = null;
    },
    increaseEmojiCount() {
      const newCount = this.emojis.length + 1;
      this.emojis = this.getRandomEmojis(newCount);
    },
    startTimer() {
      this.timer = setInterval(() => {
        this.time--;
        if (this.time <= 0) {
          this.stopGame();
        }
      }, 1000);
    },
    stopGame() {
      this.gameOver = true;
      clearInterval(this.timer);
    },
  },
  mounted() {
    this.startTimer();
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f9f9f9;
}

.emoji {
  font-size: 64px;
  margin: 10px;
  cursor: pointer;
  user-select: none;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 2px solid transparent;
  border-radius: 8px;
  height: 100px;
}

.selected-emoji {
  border-color: blue;
}
</style>