<template>
  <div class="sum-digits-test">
    <h2>Тест на суммирование цифр</h2>
    <p>Суммируйте цифры в каждом ряду и введите результат в соответствующее поле.</p>

    <div class="rows">
      <div v-for="(row, index) in rows" :key="index" class="row">
        <span class="number-row">{{ row }}</span>
        <input
          type="number"
          v-model.number="userAnswers[index]"
          class="answer-input"
        />
      </div>
    </div>

    <button @click="submitAnswers" class="submit-button">Готово</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rows: [],
      userAnswers: [],
      correctAnswers: 0,
      resultsVisible: false,
    };
  },
  methods: {

    generateRows() {
      this.rows = Array.from({ length: 5 }, () =>
        Array.from({ length: 10 }, () => Math.floor(Math.random() * 10)).join("")
      );
      this.userAnswers = Array(this.rows.length).fill(null);
      this.$emit('test-start');
    },

    submitAnswers() {
      this.correctAnswers = this.rows.reduce((count, row, index) => {
        const correctSum = row
          .split("")
          .reduce((sum, digit) => sum + parseInt(digit), 0);
        return count + (this.userAnswers[index] === correctSum ? 1 : 0);
      }, 0);
      this.resultsVisible = true;
      this.$emit('test-complete', this.correctAnswers, 5);
    },

    restartTest() {
      this.generateRows();
      this.resultsVisible = false;
      this.correctAnswers = 0;
      this.$emit('test-start');
    },
  },
  mounted() {
    this.generateRows();
  },
};
</script>

<style>

.timer{
  display: block;
}

.sum-digits-test {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}
.rows {
  margin: 20px 0;
}
.row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 10px 0;
}
.number-row {
  font-size: 20px;
  margin-right: 10px;
}
.answer-input {
  width: 80px;
  padding: 5px;
  font-size: 16px;
  text-align: center;
}
.submit-button,
.restart-button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  margin-top: 20px;
}
.results {
  margin-top: 20px;
  font-size: 18px;
}
</style>