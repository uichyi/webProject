<template>
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
</template>

<script>
export default {
  data() {
    return {
      text: `клодфитренмстоловоапряглицетыпошлидровоставракосылимонедпрыгаютвребелокречьщедорогакапустаквартирымыркодчебылкитюленувлесузебраскидаюхолстореворыпалкаочагпрокартайлебедяжукстарыйовражекореньдроваимеломшапканоркастихлосолнцезвенитшансгрибоклепестокпартастеклопосудажучокдверьлупень`,
      words: ["белок", "стол", "прыгают", "капуста", "лимон", "квартиры", "дорога", "код", "кит", "лес", "зебра",
              "палка", "очаг", "жук", "овраг", "дрова", "шапка", "норка", "солнце", "гриб", "парта", "жучок", "дверь"],
      selectedWords: [],
      totalWords: 23,
      showResults: false,
      testStarted: false
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
      this.$emit('test-complete', this.selectedWords.length, this.totalWords);
    },
    restartTest() {
      this.selectedWords = [];
      this.showResults = false;
      this.$emit('test-start');
    },
  },
  mounted() {
    this.$emit('test-start');
  },
};
</script>

<style>
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