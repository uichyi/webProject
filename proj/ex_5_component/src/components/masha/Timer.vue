
<template>
    <div>
      <h5 id='timer'><b>Время прохождения:</b> {{ minutes }}:{{ seconds < 10 ? '0' : '' }}{{ seconds }}</h5>
    </div>
  </template>

<script>
  export default {
    data() {
      return {
        totalTime: 60, // 1 минута в секундах
        timeLeft: 60,
        timeUsed: 0,
        isRunning: false,
        
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
      resetTimer(time) {
        this.stopTimer();
        this.totalTime = time;
        this.timeLeft = time;
        this.timeUsed = 0;
        this.startTimer()
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
  