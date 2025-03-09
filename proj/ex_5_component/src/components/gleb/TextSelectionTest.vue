<template>
  <div id="appp">
    <div class="navbarr">
      <RedButton/>
    </div>
    <div class="wrapper">
      <div class="text-selection-test">
      <h2>Тест: выделение слов</h2>
      <p>
        Постарайтесь выделить слова в следующем тексте. После того как вы
        завершите, нажмите кнопку "Готово".
      </p>
      <div
        class="text-area"
        contenteditable="true"
        ref="editableText"
        @mouseup="handleSelection"
      >
        {{ text }}
      </div>
      <button @click="finishTest">Готово</button>
      <div v-if="showResults" class="results">
        <h3>Результаты:</h3>
        <p>Вы выделили {{ selectedWords.length }} слов(а).</p>
        <p>Вы пропустили {{ totalWords - selectedWords.length }} слов(а).</p>
        <button @click="restartTest">Начать заново</button>
      </div>
    </div>
    </div>
  </div>
  
</template>

<script>
import axios from "axios";
import RedButton from "../navbar/Return.vue";

export default {
  components: {
    RedButton
  },
  data() {
    return {
      text: `клодфитренмстоловоапряглицетыпошлидровоставракосылимонедпрыгаютвребелокречьщедорогакапустаквартирымыркодчебылкитюленувлесузебраскидаюхолстореворыпалкаочагпрокартайлебедяжукстарыйовражекореньдроваимеломшапканоркастихлосолнцезвенитшансгрибоклепестокпартастеклопосудажучокдверьлупень`,
      words: ["белок", "стол", "прыгают", "капуста", "лимон", "квартиры", "дорога", "код", "кит", "лес", "зебра",
              "палка", "очаг", "жук", "овраг", "дрова", "шапка", "норка", "солнце", "гриб", "парта", "жучок", "дверь"],
      selectedWords: [],
      totalWords: 23,
      showResults: false,
      testStarted: false,
      testId: 9
    };
  },
  methods: {
    handleSelection() {
      if (!this.testStarted){
        this.$emit('test-start');
        this.testStarted = true
      }

      const selection = window.getSelection().toString().trim();
      if (selection && !this.selectedWords.includes(selection) && this.words.includes(selection)) {
        this.selectedWords.push(selection);
      }

      if (selection.charAt(0) === "[" && selection.charAt(selection.length-1) === "]" ){
        this.text = this.text.replace(selection, selection.slice(1, selection.length-1))
      }
      else {
        let firstInsertion = this.text.slice(0, window.getSelection().anchorOffset) + '[' + this.text.slice(window.getSelection().anchorOffset);
        let adjustedIndex2 = window.getSelection().focusOffset + 1;
        this.text = firstInsertion.slice(0, adjustedIndex2) + ']' + firstInsertion.slice(adjustedIndex2);
      }
    },
    finishTest() {
      this.showResults = true;
      this.saveTestResult()
      this.$emit('test-complete', this.selectedWords.length, this.totalWords);
    },
    restartTest() {
      this.selectedWords = [];
      this.showResults = false;
      this.$emit('test-start');
    },
    async saveTestResult() {
      const testResultData = {
        'user': localStorage.getItem('user_id'),
        "test": this.testId,
        "number_correct_answers": this.selectedWords.length,
        "number_all_answers": this.totalWords,
        "accuracy": this.selectedWords.length / this.totalWords
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
    }
  },
  mounted() {
    this.$emit('test-start');
  },
};
</script>

<style scoped>
#appp {
  background-color: #0000003f;
  height: 100vh;
  width: 100vw;
  display: grid;
  grid-template-rows: auto 1fr;
}

.wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;

  height: auto;
}

.text-selection-test {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

.text-area {
  margin: 20px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  height: 200px;
  overflow-y: auto;
  white-space: pre-wrap;
  font-family: monospace;
  background: #f9f9f9;
  user-select: text;
  color: black;
}

button {
  margin: 10px;
  padding: 10px 20px;
  cursor: pointer;
}

.results {
  margin-top: 20px;
}

.results p {
  margin: 10px 0;
}
</style>