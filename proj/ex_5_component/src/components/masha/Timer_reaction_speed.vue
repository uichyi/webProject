<template>
    <div>
    </div>
  </template>

<script>
  export default {
    data() {
      return {
        totalTime: 0,
        isRunning: false,
        
      };
    },
    beforeMount() {
      this.startTimer()
    },
    computed: {
      milliseconds() {
        return this.totalTime 
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
            this.totalTime+=10;
        }, 10);
      },
      stopTimer() {
        clearInterval(this.timer);
        this.isRunning = false;
      },
      resetTimer(time) {
        this.stopTimer();
        this.totalTime = time;
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
  