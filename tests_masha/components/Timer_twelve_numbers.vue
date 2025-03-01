
<template>
    <div>
      <h5><b>Осталось:</b> {{ minutes }}:{{ seconds < 10 ? '0' : '' }}{{ seconds }}</h5>
    </div>
  </template>

<script>
  export default {
    data() {
      return {
        totalTime: 20, // 1 минута в секундах
        timeLeft: 20,
        timeUsed: 0,
        isRunning: false,
        timer: null,
      };
    },
    beforeMount() {
      this.startTimer()
    },
    computed: {
      minutes() {
        return Math.floor(this.timeLeft / 60);
      },
      seconds() {
        return this.timeLeft % 60;
      },
      timeLeftCount(){
        return this.timeLeft
      },
      timeUsedCount(){
        return this.timeUsed
      },
    },
    methods: {
      startTimer() {
        if (this.isRunning) return;
        this.isRunning = true;
        this.timer = setInterval(() => {
          if (this.timeLeft > 0) {
            this.timeLeft--;
            this.timeUsed++;
          } else {
            clearInterval(this.timer);
            this.isRunning = false;
          }
        }, 1000);
      },
      stopTimer() {
        clearInterval(this.timer);
        this.isRunning = false;
      },
      resetTimer() {
        this.stopTimer();
        this.timeLeft = this.totalTime;
      },
    },
    beforeDestroy() {
      this.stopTimer();
    },
  };
</script>
    
<style scoped>
  h5{
      color: #9966CC;
  }
</style>
  