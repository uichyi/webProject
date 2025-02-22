<!-- 
TRK 11-12-2024 Добавил описание к игре перед началом игры, Тест 4
TRK 12-12-2024 Добавил Тест 5
-->

<template>
  <div id="app" class="container mt-5 text-center">
    <h1 class="mb-4">Тесты</h1>
    <div class="btn-group mb-4" role="group">
      <button class="btn btn-secondary" @click="selectApp('test1')">Найди пару эмодзи</button>
      <button class="btn btn-secondary" @click="selectApp('test2')">Путь стрелки</button>
      <button class="btn btn-secondary" @click="selectApp('test3')">Совпадает ли эмодзи?</button>
      <button class="btn btn-secondary" @click="selectApp('test4')">Сравнение чисел</button>
      <button class="btn btn-secondary" @click="selectApp('test5')">Преобладающий цвет</button>
    </div>
    <div v-if="selectedGame"> <!-- TRK 11-12-2024 -->
      <div v-if="selectedApp == 'test1'">
        <Test1/>
      </div>
      <div v-else-if="selectedApp == 'test2'">
        <Test2/>
      </div>
      <div v-else-if="selectedApp == 'test3'">
        <Test3/>
      </div>
      <div v-else-if="selectedApp == 'test4'">
        <Test4/> <!-- TRK 11-12-2024 --> 
      </div>
      <div v-else-if="selectedApp == 'test5'">
        <Test5/> <!-- TRK 12-12-2024 --> 
      </div>
    <!-- TRK 11-12-2024 -> -->
    </div>
    <div v-else-if="!selectedGame">
      <div v-if="selectedApp == 'test1'">
        <p>Перед вами набор эмодзи, в котором одинаковые только <b>два.</b> <br> 
          Найдите как можно больше пар таких эмодзи за минуту</p>
      </div>
      <div v-else-if="selectedApp == 'test2'">
        <p>Перед вами стрелка, которая смотрит вверх/вниз/влево/вправо и либо красный фон, либо синий. <br> 
          Вам необходимо за минуту определить как можно больше раз путь стрелки, где синий фон обозначает <b>куда</b> направлена стрелка, а красный обозначает <b>откуда</b> идет стрелка</p>
      </div>
      <div v-else-if="selectedApp == 'test3'">
        <p>Перед вами один эмодзи, который будет виден на протяжении 3 секунд. После, он заменится другим либо тем же самым. <br>
          За одну минуту вам необходимо как можно больше раз указать, изменился ли эмодзи или нет.</p>
      </div>
      <div v-else-if="selectedApp == 'test4'">
        <p>Перед вами два числа. За одну минуту вам необходимо сравнить как можно больше раз, какое число больше, а какое меньше</p>
      </div>
      <div v-else-if="selectedApp == 'test5'">
        <p>Перед вами оттенок. За одну минуту вам необходимо определить как можно больше раз, какой цвет преобладает в этом оттенке</p> <!-- TRK 12-12-2024 --> 
      </div>
      <div v-if="selectedApp">
        <button class="btn btn-primary" @click="startGame()">Начать игру</button>  
      </div>
      <div v-else>
        <p>Привет! Здесь ты можешь выбрать один из 5 тестов. <br>
        При нажатии, откроется описание выбранного теста</p>
      </div>
    </div>
    <!-- TRK 11-12-2024 <- -->
  </div>
</template>

<script>
import Test1 from './components/Test1.vue';
import Test2 from './components/Test2.vue';
import Test3 from './components/Test3.vue';
import Test4 from './components/Test4.vue'; // TRK 11-12-2024
import Test5 from './components/Test5.vue'; // TRK 12-12-2024

export default {
  components: {
    Test1,
    Test2,
    Test3, 
    Test4, // TRK 11-12-2024
    Test5 // TRK 12-12-2024
  },
  data() {
    return {
      selectedApp: null,
      selectedGame: false // TRK 11-12-2024 
    };
  },
  methods: {
    selectApp(app) {
      this.selectedApp = app;
      this.selectedGame = false; // TRK 11-12-2024 
    },
    // TRK 11-12-2024 ->
    startGame(){
      this.selectedGame = true;
    }
    // TRK 11-12-2024 <-
  }
};
</script>
