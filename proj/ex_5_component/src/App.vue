<template>
  <div id="app" class="container mt-5 text-center">
    <h1 class="mb-4">Тесты</h1>
    <div class="btn-group mb-4" role="group">
      <button class="btn btn-secondary" @click="selectApp('test1')">Найди пару эмодзи</button>
      <button class="btn btn-secondary" @click="selectApp('test2')">Путь стрелки</button>
      <button class="btn btn-secondary" @click="selectApp('test3')">Совпадает ли эмодзи?</button>
      <button class="btn btn-secondary" @click="selectApp('test4')">Сравнение чисел</button>
      <button class="btn btn-secondary" @click="selectApp('test5')">Преобладающий цвет</button>
      <button class="btn btn-secondary" @click="selectApp('test6')">тестглеба1</button>
      <button class="btn btn-secondary" @click="selectApp('test7')">тестглеба2</button>
      <button class="btn btn-secondary" @click="selectApp('test8')">тестглеба3</button>
      <button class="btn btn-secondary" @click="selectApp('test9')">тестглеба4</button>
      <button class="btn btn-secondary" @click="selectApp('test10')">тестглеба5</button>
      <button class="btn btn-secondary" @click="selectApp('test11')">тестильи1</button>
      <button class="btn btn-secondary" @click="selectApp('test12')">тестильи2</button>
      <button class="btn btn-secondary" @click="selectApp('test13')">тестильи3</button>
      <button class="btn btn-secondary" @click="selectApp('test14')">тестильи4</button>
      <button class="btn btn-secondary" @click="selectApp('test15')">тестильи5</button>
      <button class="btn btn-secondary" @click="selectApp('test16')">тестмаши1</button>
      <button class="btn btn-secondary" @click="selectApp('test17')">тестмаши2</button>
      <button class="btn btn-secondary" @click="selectApp('test18')">тестмаши3</button>
      <button class="btn btn-secondary" @click="selectApp('test19')">тестмаши4</button>
      <button class="btn btn-secondary" @click="selectApp('test20')">тестмаши5</button>
      <button class="btn btn-secondary" @click="selectApp('test21')">тестмити1</button>
      <button class="btn btn-secondary" @click="selectApp('test22')">тестмити2</button>
      <button class="btn btn-secondary" @click="selectApp('test23')">тестмити3</button>
      <button class="btn btn-secondary" @click="selectApp('test24')">тестмити4</button>
      <button class="btn btn-secondary" @click="selectApp('test25')">тестмити5</button>
      <button class="btn btn-secondary" @click="selectApp('test26')">тестксюши1</button>
      <button class="btn btn-secondary" @click="selectApp('test27')">тестксюши2</button>
      <button class="btn btn-secondary" @click="selectApp('test28')">тестксюши3</button>
    </div>
    <div v-if="selectedGame"> 
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
        <Test4/> 
      </div>
      <div v-else-if="selectedApp == 'test5'">
        <Test5/> 
      </div>
      <div v-else-if="selectedApp == 'test6'">
        <AttentionTest/>
      </div>
      <div v-else-if="selectedApp == 'test7'">
        <ReactionTest/>
      </div>
      <div v-else-if="selectedApp == 'test8'">
        <MemoryTest/>
      </div>
      <div v-else-if="selectedApp == 'test9'">
        <TextSelectionTest/> 
      </div>
      <div v-else-if="selectedApp == 'test10'">
        <SumDigitsTest/> 
      </div>
      <div v-else-if="selectedApp == 'test11'">
        <test1ilya/>
      </div>
      <div v-else-if="selectedApp == 'test12'">
        <test2ilya/>
      </div>
      <div v-else-if="selectedApp == 'test13'">
        <test3ilya/>
      </div>
      <div v-else-if="selectedApp == 'test14'">
        <test4ilya/> 
      </div>
      <div v-else-if="selectedApp == 'test15'">
        <test5ilya/> 
      </div>
      <div v-else-if="selectedApp == 'test16'">
        <Rectangles/>
      </div>
      <div v-else-if="selectedApp == 'test17'">
        <Twelve_number_test/>
      </div>
      <div v-else-if="selectedApp == 'test18'">
        <Numbers_puzzle/>
      </div>
      <div v-else-if="selectedApp == 'test19'">
        <Reaction_speed/> 
      </div>
      <div v-else-if="selectedApp == 'test20'">
        <Classical_Stroop_Test/> 
      </div>
      <div v-else-if="selectedApp == 'test21'">
        <test1mitya/>
      </div>
      <div v-else-if="selectedApp == 'test22'">
        <test2mitya/>
      </div>
      <div v-else-if="selectedApp == 'test23'">
        <test3mitya/>
      </div>
      <div v-else-if="selectedApp == 'test24'">
        <test4mitya/> 
      </div>
      <div v-else-if="selectedApp == 'test25'">
        <test5mitya/> 
      </div>
      <div v-else-if="selectedApp == 'test26'">
        <Test1k/>
      </div>
      <div v-else-if="selectedApp == 'test27'">
        <Test2k/> 
      </div>
      <div v-else-if="selectedApp == 'test28'">
        <Test3k/> 
      </div>

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
  </div>
</template>

<script>
import Test1 from './components/kostya/Test1.vue';
import Test2 from './components/kostya/Test2.vue';
import Test3 from './components/kostya/Test3.vue';
import Test4 from './components/kostya/Test4.vue'; 
import Test5 from './components/kostya/Test5.vue'; 

import Timer from './components/gleb/Timer.vue';
import AttentionTest from './components/gleb/AttentionTest.vue';
import ReactionTest from './components/gleb/ReactionTest.vue';
import MemoryTest from './components/gleb/MemoryTest.vue';
import TextSelectionTest from './components/gleb/TextSelectionTest.vue';
import SumDigitsTest from './components/gleb/SumDigitsTest.vue';

import test1ilya from './components/ilya/test_1_numbers/src/test1ilya.vue';
import test2ilya from './components/ilya/test_2_unique_color/src/test2ilya.vue';
import test3ilya from './components/ilya/test_3_extra_item/src/test3ilya.vue';
import test4ilya from './components/ilya/test_4_clicks/src/test4ilya.vue';
import test5ilya from './components/ilya/test_5_typing/src/test5ilya.vue';

import Rectangles from './components/masha/Rectangles.vue'
import Twelve_number_test from './components/masha/Twelve_number_test.vue'
import Numbers_puzzle from './components/masha/Numbers_puzzle.vue'
import Reaction_speed from './components/masha/Reaction_speed.vue'
import Classical_Stroop_Test from './components/masha/Classical_Stroop_Test.vue'

import test1mitya from './components/mitya/test1/test1mitya.vue'
import test2mitya from './components/mitya/test2/test2mitya.vue'
import test3mitya from './components/mitya/test3/test3mitya.vue'
import test4mitya from './components/mitya/test4/test4mitya.vue'
import test5mitya from './components/mitya/test5/test5mitya.vue'

import Test1k from './components/ksysha/Test1k.vue';
import Test2k from './components/ksysha/Test2k.vue';
import Test3k from './components/ksysha/Test3k.vue';

export default {
  components: {
    Test1,
    Test2,
    Test3, 
    Test4, 
    Test5,
    AttentionTest,
    ReactionTest,
    MemoryTest,
    TextSelectionTest,
    SumDigitsTest,
    test1ilya,
    test2ilya,
    test3ilya, 
    test4ilya,
    test5ilya,
    Rectangles,
    Twelve_number_test,
    Numbers_puzzle,
    Reaction_speed,
    Classical_Stroop_Test,
    test1mitya,
    test2mitya,
    test3mitya,
    test4mitya,
    test5mitya,
    Test1k,
    Test2k,
    Test3k
  },
  data() {
    return {
      selectedApp: null,
      selectedGame: false 
    };
  },
  methods: {
    selectApp(app) {
      this.selectedApp = app;
      this.selectedGame = false; 
    },

    startGame(){
      this.selectedGame = true;
    }
  }
};
</script>
