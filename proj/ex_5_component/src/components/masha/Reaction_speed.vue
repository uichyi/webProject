<script setup>
  import Timer from './Timer_reaction_speed.vue'
</script>
<template>
    <div id="appp">
        <div class="navbarr">
            <RedButton />
        </div>
        <div class="wrapper">
            <h2 class='text-center mb-4'>Тест-тренажер на скорость реакции</h2>
            <div @click="do_actions" id="box">
                <h1 class="mb-5">{{ show_res }}</h1>
                <svg  id='icon' xmlns="http://www.w3.org/2000/svg" width="10%" fill="currentColor" class="bi bi-hourglass-split my-3" viewBox="0 0 16 16">
                    <path d="M6 .5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1H9v1.07a7.001 7.001 0 0 1 3.274 12.474l.601.602a.5.5 0 0 1-.707.708l-.746-.746A6.97 6.97 0 0 1 8 16a6.97 6.97 0 0 1-3.422-.892l-.746.746a.5.5 0 0 1-.707-.708l.602-.602A7.001 7.001 0 0 1 7 2.07V1h-.5A.5.5 0 0 1 6 .5m2.5 5a.5.5 0 0 0-1 0v3.362l-1.429 2.38a.5.5 0 1 0 .858.515l1.5-2.5A.5.5 0 0 0 8.5 9zM.86 5.387A2.5 2.5 0 1 1 4.387 1.86 8.04 8.04 0 0 0 .86 5.387M11.613 1.86a2.5 2.5 0 1 1 3.527 3.527 8.04 8.04 0 0 0-3.527-3.527"/>
                </svg>
                <div id="text-box">Кликните для старта</div>
                <p id="instr" v-if="is_touch==false && is_waiting==false && is_started">Кликните для продолжения</p>
                <div>
                    <p>Среднее время реакции: {{ avg_time }} мс</p>
                    <p>Попытка: {{ level }} / 5</p>
                </div>
                {{countTime}}
            </div>
            <Timer ref="timer"/>
        </div>
    </div>
</template>
<script>
    import axios from "axios";
    import RedButton from "../navbar/Return.vue";

    export default {
        components: {
           Timer,
           RedButton
        },
        data() {
            return {
                is_started: false,
                is_waiting: false,
                timer: null,
                time_used: 0,
                is_touch: false,
                result: 0,
                level: 0,
                testId: 19,
                results: [[0, 150,'Превосходно! Можно садиться за штурвал истребителя или болида формулы 1.'], [151, 170, 'Это пять с плюсом! Чемпионы мира по пинг-понгу и боксу смотрят на Вас как на конкурента.'], 
                [171, 190, 'Великолепно! Мастера спорта международного класса одобряют.'], [191, 200, 'Хорошо! Мастер спорта у Вас в кармане.'], [201, 210, 'Неплохо. КМС зачтен.'], [211, 230, 'Нормально. Вы активны, можете лучше.'], 
                [231, 270, 'Средненько. Скорость реакции, как и у большинства людей.'], [271, 350, 'Неуд.'], [351, 500, 'Незачет.'],['Вы вообще живы там? Лучше отдохните, попробуйте завтра.']]
            }
        },
        mounted(){
           
        },
        computed:{
            countTime(){
                if (this.is_waiting){
                    if (this.$refs.timer.totalTime == 3000){
                        this.is_waiting = false
                        this.is_touch = true
                        this.$refs.timer.resetTimer(0)
                        document.getElementById('box').style.background = '#00a851'
                        document.getElementById('text-box').innerHTML = 'Кликайте!'
                        document.getElementById('icon').innerHTML = '<path d="M7.5.026C4.958.286 3 2.515 3 5.188V5.5h4.5zm1 0V5.5H13v-.312C13 2.515 11.042.286 8.5.026M13 6.5H3v4.313C3 13.658 5.22 16 8 16s5-2.342 5-5.188z"/>'
                    }
                }
            },
            avg_time(){
                if (this.level == 0){
                    return 0
                }
                else{
                    return this.result / this.level
                }
            },
            show_res(){
                if (this.level == 5){
                    for (let i=0; i<this.results.length-1; i++){
                        if(this.result / this.level>=this.results[i][0] && this.result / this.level<=this.results[i][1]){
                            this.saveTestResult();
                            return 'Ваш результат: ' + this.results[i][2]
                        }
                    }
                    this.saveTestResult();
                    return 'Ваш результат: ' + this.results[this.results.length-1][1]
                }
                return ''
            }
        },
        methods: {
            async saveTestResult(result) {
                const testResultData = {
                    'user': localStorage.getItem('user_id'),
                    "test": this.testId,
                    "complete_time": 0,
                    "accuracy": Number((this.result / 5).toFixed(2))
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
            do_actions(){
                if(this.level < 5){
                    let box = document.getElementById('box')
                    if (this.is_waiting == false && this.is_touch == false){
                        this.is_started = true
                        box.style.background = '#fcd71e'
                        document.getElementById('text-box').innerText = 'Ждите зеленый!'
                        this.is_waiting = true
                        this.$refs.timer.resetTimer(0)
                        let icon = document.getElementById('icon')
                        icon.innerHTML = '<path d="M2.5 15a.5.5 0 1 1 0-1h1v-1a4.5 4.5 0 0 1 2.557-4.06c.29-.139.443-.377.443-.59v-.7c0-.213-.154-.451-.443-.59A4.5 4.5 0 0 1 3.5 3V2h-1a.5.5 0 0 1 0-1h11a.5.5 0 0 1 0 1h-1v1a4.5 4.5 0 0 1-2.557 4.06c-.29.139-.443.377-.443.59v.7c0 .213.154.451.443.59A4.5 4.5 0 0 1 12.5 13v1h1a.5.5 0 0 1 0 1zm2-13v1c0 .537.12 1.045.337 1.5h6.326c.216-.455.337-.963.337-1.5V2zm3 6.35c0 .701-.478 1.236-1.011 1.492A3.5 3.5 0 0 0 4.5 13s.866-1.299 3-1.48zm1 0v3.17c2.134.181 3 1.48 3 1.48a3.5 3.5 0 0 0-1.989-3.158C8.978 9.586 8.5 9.052 8.5 8.351z"/>'
                    }
                    else if(this.is_waiting && this.is_touch == false){
                        box.style.background = '#ff2e2e'
                        document.getElementById('text-box').innerText = 'Слишком рано!'
                        document.getElementById('icon').innerHTML = '<path d="M15 8a6.97 6.97 0 0 0-1.71-4.584l-9.874 9.875A7 7 0 0 0 15 8M2.71 12.584l9.874-9.875a7 7 0 0 0-9.874 9.874ZM16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0"/>'
                        this.is_waiting = false
                    }
                    else if(this.is_touch){
                        this.$refs.timer.stopTimer()
                        document.getElementById('text-box').innerText = this.$refs.timer.totalTime+' мс'
                        box.style.background = '#4B0082'
                        this.is_touch = false
                        this.result += this.$refs.timer.totalTime
                        this.level++
                        document.getElementById('icon').innerHTML = ' <path d="M6 .5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1H9v1.07a7.001 7.001 0 0 1 3.274 12.474l.601.602a.5.5 0 0 1-.707.708l-.746-.746A6.97 6.97 0 0 1 8 16a6.97 6.97 0 0 1-3.422-.892l-.746.746a.5.5 0 0 1-.707-.708l.602-.602A7.001 7.001 0 0 1 7 2.07V1h-.5A.5.5 0 0 1 6 .5m2.5 5a.5.5 0 0 0-1 0v3.362l-1.429 2.38a.5.5 0 1 0 .858.515l1.5-2.5A.5.5 0 0 0 8.5 9zM.86 5.387A2.5 2.5 0 1 1 4.387 1.86 8.04 8.04 0 0 0 .86 5.387M11.613 1.86a2.5 2.5 0 1 1 3.527 3.527 8.04 8.04 0 0 0-3.527-3.527"/>'
                    }
                }
                else{
                    this.level = 0
                    this.result = 0
                    this.$refs.timer.resetTimer(0)
                    this.is_started = false
                    document.getElementById('text-box').innerHTML='Кликните для старта'
                }    
            }
        } 
    }      
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

  .wrapper {
    /* height: 100vh; */
    display: flex;
    justify-content: center;
    flex-direction: column;
  }

    #box{
        background: #4B0082;
        width:100%;
        padding-top: 1%;
        padding-bottom: 1%;
        text-align: center;
        font-size: 150%;
        color: white
    }
    #text-box{
        font-size: 200%;
    }
    h2{
        color: #4B0082;
    }
    #instr{
        font-size: 130%;
        color: #f53dc4
    }
    h1{
        color: #ed55b5
    }
</style>