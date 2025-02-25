<template>
  <div class="timer">
    Время прохождения теста: {{ formattedTime }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      timeElapsed: 0,
      timer: null,
    };
  },
  computed: {
    formattedTime() {
      const seconds = Math.floor((this.timeElapsed / 1000) % 60);
      const minutes = Math.floor(this.timeElapsed / 60000);
      return `${minutes} мин ${seconds} сек`;
    },
  },
  methods: {
    startTimer() {
      if (this.timer) clearInterval(this.timer);
      this.timeElapsed = 0;
      this.timer = setInterval(() => {
        this.timeElapsed += 100;
      }, 100);
    },
    stopTimer() {
      if (this.timer) {
        clearInterval(this.timer);
        this.timer = null;
      }
    },
    resetTimer() {
      this.stopTimer();
      this.timeElapsed = 0;
    },
  },
  beforeDestroy() {
    this.stopTimer();
  },
};
</script>

<style>
.timer {
  font-size: 18px;
  font-weight: bold;
  margin: 20px 0;
  text-align: center;
}
</style>