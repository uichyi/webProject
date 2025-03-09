<script setup>
</script>

<template>
  <div id="appp">
    <section v-if="showSignupSection" class="vh-100" style='background:#dbf0ff'>
      <div class="container h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-lg-12 col-xl-11">
            <div class="card text-black">
              <div class="card-body p-md-5">
                <div class="row justify-content-center">
                  <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">
                    <p class="text-center text-primary h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Регистрация</p>
                    <form class="mx-1 mx-md-4" method='post' id="my_form">
                      <p class="text-danger">{{error}}</p>
                      <div class="d-flex flex-row align-items-center mb-4">
                        <div data-mdb-input-init class="form-outline flex-fill mb-0">
                          <input type="text" v-model='name' id="name" class="form-control" placeholder="Придумайте никнейм" required/>
                        </div>
                      </div>
                      <div class="d-flex flex-row align-items-center mb-4">
                        <div data-mdb-input-init class="form-outline flex-fill mb-0">
                          <input type="password" v-model='password1' id="password1" class="form-control" placeholder="Придумайте пароль" required/>
                        </div>
                      </div>
                      <div class="d-flex flex-row align-items-center mb-4">
                        <div data-mdb-input-init class="form-outline flex-fill mb-0">
                          <input type="password" v-model='password2' id="password2" class="form-control" placeholder="Повторите пароль" required/>
                        </div>
                      </div>
                      <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                        <button @click="checkData" type="submit" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-lg">Зарегистрироваться</button>
                      </div>
                    </form>
                  </div>
                  <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">
                    <img src="https://img.freepik.com/free-vector/mobile-login-concept-illustration_114360-83.jpg"
                      class="img-fluid" alt="Sample image">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section v-else class="h-100" style='background:#dbf0ff'>
        <div class="container py-5 h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
          <form method='post' id="my_form2">
            <div class="col">
              <div class="card card-registration my-2">
                <div class="row g-0">
                  <div>
                    <div class="card-body p-md-5 text-black">
                      <h3 class="mb-5 text-primary text-center">Введите информацию о себе</h3>
                      <div class="row">
                        <div class="col-md-6 mb-4">
                          <div class="form-outline">
                            <label class="form-label text-primary" for="age">Возраст</label>
                            <input type="number" min="1" max="117" id="age" v-model='age' class="form-control form-control-lg" placeholder="Введите значение" required/>
                            <label class="form-label text-danger" for="age">{{error_age}}</label>
                          </div>
                        </div>
                        <div class="col-md-6 mb-4">
                          <div data-mdb-input-init class="form-outline">
                            <label class="form-label text-primary" for="height">Рост (см)</label>
                            <input type="number" min="0" id="height" v-model='height' class="form-control form-control-lg" placeholder="Введите значение" required/>
                            <label class="form-label text-danger" for="height">{{error_height}}</label>
                          </div>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col-md-6 mb-4">
                          <div data-mdb-input-init class="form-outline">
                            <label class="form-label text-primary" for="weight">Вес (кг)</label>
                            <input type="number" min="0" id="weight" v-model='weight' class="form-control form-control-lg" placeholder="Введите значение" required/>
                            <label class="form-label text-danger" for="weight">{{error_weight}}</label>
                          </div>
                        </div>
                        <div class="col-md-6 mb-4">
                          <div data-mdb-input-init class="form-outline">
                            <label class="form-label text-primary" for="leading_arm">Ведущая рука</label>
                            <select class="form-select form-select-lg" v-model="lead_hand" id="leading_arm" required>
                              <option value="" selected></option>
                              <option value="1">Правая</option>
                              <option value="2">Левая</option>
                            </select>
                          </div>
                        </div>
                      </div>
                    <div class="row">
                      <div class="col-md-6 mb-4">
                        <label class="form-label text-primary" for="education">Базовое образование</label>
                        <select class="form-select form-select-lg" v-model="education" id="education" required>
                          <option value="" selected></option>
                          <option value="1">Основное общее</option>
                          <option value="2">Среднее общее</option>
                          <option value="3">Высшее образование: бакалавриат</option>
                          <option value="4">Высшее образование: магистратура, специалитет</option>
                        </select>
                      </div>
                      <div class="col-md-6 mb-4">
                        <div data-mdb-input-init class="form-outline">
                          <label class="form-label text-primary" for="speciality">Специальность</label>
                          <input type="text" id="speciality" v-model="speciality" class="form-control form-control-lg" placeholder="Введите название" required/>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6 mb-4">
                        <label class="form-label text-primary" for="place_of_residence">Место основного проживания</label>
                        <select class="form-select form-select-lg" v-model="residence" id="place_of_residence" required>
                          <option value="" selected></option>
                          <option value="1">Столичный город (Москва или Санкт-Петербург)</option>
                          <option value="2">Областной центр</option>
                          <option value="3">Районный центр</option>
                          <option value="4">Малый город или поселок городского типа</option>
                          <option value="5">Деревня / село</option>
                        </select>
                      </div>
                    </div>
                    <h6 class="mb-0 me-4 text-primary">Как Вы себя чувствуете: </h6>
                    <div class="d-md-flex justify-content-start align-items-center mb-4 py-2">
                      <div class="form-check form-check-inline mb-0 me-4">
                        <input class="form-check-input" v-model="current_health" type="radio" name="inlineRadioOptions" id="very_bad"
                          v-bind:value="Number(1)" required/>
                        <label class="form-check-label" for="very_bad">
                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-emoji-tear" viewBox="0 0 16 16">
                              <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                              <path d="M6.831 11.43A3.1 3.1 0 0 1 8 11.196c.916 0 1.607.408 2.25.826.212.138.424-.069.282-.277-.564-.83-1.558-2.049-2.532-2.049-.53 0-1.066.361-1.536.824q.126.27.232.535.069.174.135.373ZM6 11.333C6 12.253 5.328 13 4.5 13S3 12.254 3 11.333c0-.706.882-2.29 1.294-2.99a.238.238 0 0 1 .412 0c.412.7 1.294 2.284 1.294 2.99M7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5m4 0c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5m-1.5-3A.5.5 0 0 1 10 3c1.162 0 2.35.584 2.947 1.776a.5.5 0 1 1-.894.448C11.649 4.416 10.838 4 10 4a.5.5 0 0 1-.5-.5M7 3.5a.5.5 0 0 0-.5-.5c-1.162 0-2.35.584-2.947 1.776a.5.5 0 1 0 .894.448C4.851 4.416 5.662 4 6.5 4a.5.5 0 0 0 .5-.5"/>
                            </svg>
                        </label>
                      </div>
                      <div class="form-check form-check-inline mb-0 me-4">
                        <input class="form-check-input" v-model="current_health" type="radio" name="inlineRadioOptions" id="bad"
                          v-bind:value="Number(2)"/>
                        <label class="form-check-label" for="bad">
                          <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-emoji-frown" viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                            <path d="M4.285 12.433a.5.5 0 0 0 .683-.183A3.5 3.5 0 0 1 8 10.5c1.295 0 2.426.703 3.032 1.75a.5.5 0 0 0 .866-.5A4.5 4.5 0 0 0 8 9.5a4.5 4.5 0 0 0-3.898 2.25.5.5 0 0 0 .183.683M7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5m4 0c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5"/>
                          </svg>
                        </label>
                      </div>
                      <div class="form-check form-check-inline mb-0 me-4">
                        <input class="form-check-input" v-model="current_health" type="radio" name="inlineRadioOptions" id="neutral"
                          v-bind:value="Number(3)" />
                        <label class="form-check-label" for="neutral">
                          <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-emoji-neutral" viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                            <path d="M4 10.5a.5.5 0 0 0 .5.5h7a.5.5 0 0 0 0-1h-7a.5.5 0 0 0-.5.5m3-4C7 5.672 6.552 5 6 5s-1 .672-1 1.5S5.448 8 6 8s1-.672 1-1.5m4 0c0-.828-.448-1.5-1-1.5s-1 .672-1 1.5S9.448 8 10 8s1-.672 1-1.5"/>
                          </svg>
                        </label>
                      </div>
                      <div class="form-check form-check-inline mb-0 me-4">
                        <input class="form-check-input" v-model="current_health" type="radio" name="inlineRadioOptions" id="good"
                          v-bind:value="Number(4)" />
                        <label class="form-check-label" for="good">
                          <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-emoji-smile" viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                            <path d="M4.285 9.567a.5.5 0 0 1 .683.183A3.5 3.5 0 0 0 8 11.5a3.5 3.5 0 0 0 3.032-1.75.5.5 0 1 1 .866.5A4.5 4.5 0 0 1 8 12.5a4.5 4.5 0 0 1-3.898-2.25.5.5 0 0 1 .183-.683M7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5m4 0c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5"/>
                          </svg>
                        </label>
                      </div>
                      <div class="form-check form-check-inline mb-0 me-4">
                        <input class="form-check-input" v-model="current_health" type="radio" name="inlineRadioOptions" id="very_good"
                          v-bind:value="Number(5)"/>
                        <label class="form-check-label" for="very_good">
                          <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-emoji-grin" viewBox="0 0 16 16">
                            <path d="M12.946 11.398A6.002 6.002 0 0 1 2.108 9.14c-.114-.595.426-1.068 1.028-.997C4.405 8.289 6.48 8.5 8 8.5s3.595-.21 4.864-.358c.602-.07 1.142.402 1.028.998a5.95 5.95 0 0 1-.946 2.258m-.078-2.25C11.588 9.295 9.539 9.5 8 9.5s-3.589-.205-4.868-.352c.11.468.286.91.517 1.317A37 37 0 0 0 8 10.75a37 37 0 0 0 4.351-.285c.231-.407.407-.85.517-1.317m-1.36 2.416c-1.02.1-2.255.186-3.508.186s-2.488-.086-3.507-.186A5 5 0 0 0 8 13a5 5 0 0 0 3.507-1.436ZM6.488 7c.114-.294.179-.636.179-1 0-1.105-.597-2-1.334-2C4.597 4 4 4.895 4 6c0 .364.065.706.178 1 .23-.598.662-1 1.155-1 .494 0 .925.402 1.155 1M12 6c0 .364-.065.706-.178 1-.23-.598-.662-1-1.155-1-.494 0-.925.402-1.155 1a2.8 2.8 0 0 1-.179-1c0-1.105.597-2 1.334-2C11.403 4 12 4.895 12 6"/>
                            <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m0-1A7 7 0 1 1 8 1a7 7 0 0 1 0 14"/>
                          </svg>
                        </label>
                      </div>
                    </div>
                    <div class="form-outline mb-4">
                        <label class="form-label text-primary" for="diseases">Заболевания</label>
                        <input type="text" id="diseases" v-model="diseases" class="form-control form-control-lg" placeholder="Введите Ваши заболевания" required/>
                    </div>
                    <div class="row">
                      <div class="col-md-4 mb-4">
                        <div class="form-check form-switch">
                          <input class="form-check-input" v-model="smoking" type="checkbox" id="smoking">
                          <label class="form-check-label" for="smoking">Курение</label>
                        </div>
                      </div>
                      <div class="col-md-4 mb-4">
                        <div class="form-check form-switch">
                          <input class="form-check-input" v-model="insomnia" type="checkbox" id="insomnia">
                          <label class="form-check-label" for="insomnia">Бессоница</label>
                        </div>
                      </div>
                      <div class="col-md-4 mb-4">
                        <div class="form-check form-switch">
                          <input class="form-check-input" v-model="gaming" type="checkbox" id="gamer">
                          <label class="form-check-label" for="gamer">Являетесь ли Вы геймером</label>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6 mb-4">
                        <label class="form-label text-primary" for="alcohol_frequency">Как часто Вы употребляете алкогольные напитки?</label>
                        <select class="form-select form-select-lg" v-model="alcohol" id="alcohol_frequency" required>
                          <option value="" selected></option>
                          <option value="1">Никогда</option>
                          <option value="2">Раз в месяц или реже</option>
                          <option value="3">2 - 4 раза в месяц</option>
                          <option value="4">2 - 3 раза в неделю</option>
                          <option value="5">4 раза в неделю и чаще</option>
                        </select>
                      </div>
                    </div>
                    <div data-mdb-input-init class="form-outline mb-4">
                      <label class="form-label text-primary" for="sports">Спорт</label>
                      <input type="text" id="sports" class="form-control form-control-lg" v-model="sport" placeholder="Каким спортом занимаетесь?" required/>
                    </div>
                    <div class="d-flex justify-content-end pt-3">
                      <button type="submit" @click='checkData' data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-lg ms-2">Перейти к тестам</button>
                    </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            </form>
          </div>
        </div>
      </section>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        showSignupSection: true,
        error: '',
        name:'',
        password1:'',
        password2:'',
        error_age: '',
        error_weight:'',
        error_height:'',
        age:'',
        weight:'',
        height:'',
        lead_hand:'',
        education:'',
        speciality:'',
        residence:'',
        diseases:'',
        smoking:false,
        alcohol:'',
        sport:'',
        insomnia:false,
        current_health:'',
        gaming:false
      };
    },
    methods: {
      async checkData() {
        if(this.showSignupSection) {
          document.getElementById('my_form').onsubmit = function (event) {
            event.preventDefault();
          }
        }
        else {
          document.getElementById('my_form2').onsubmit = function (event) {
            event.preventDefault();
          }
        }

        this.error_age=''
        this.error_height=''
        this.error_weight=''
        if (this.name ==''){
          this.error='Введите никнейм'
          return
        }

        if(this.password1 == ""){
          this.error='Введите пароль'
          return
        }
        if(this.password2 == ""){
          this.error='Повторите пароль'
          return
        }
        if(this.password1 != this.password2){
          this.error='Пароли не совпадают'
          return
        }
        this.error = ''
        this.showSignupSection = false;

        if (this.age ==''){
          this.error_age='Введите возаст'
          return
        }
        if (this.age<0){
          this.error_age='Возраст не может быть отрицательным числом'
          return
        }
        if (this.height ==''){
          this.error_height='Введите рост'
          return
        }
        if (this.height<0){
          this.error_height='Рост не может быть отрицательным числом'
          return
        }
        if (this.weight ==''){
          this.error_weight='Введите вес'
          return
        }
        if (this.weight<0){
          this.error_weight='Вес не может быть отрицательным числом'
          return
        }

         const log =
        {
          "username": this.name,
          "password": this.password1,
          "age": this.age,
          "education": this.education,
          "speciality": this.speciality,
          "residence": this.residence,
          "height": this.height,
          "weight": this.weight,
          "lead_hand": this.lead_hand,
          "diseases": this.diseases,
          "smoking": this.smoking,
          "alcohol": this.alcohol,
          "sport": this.sport,
          "insomnia": this.insomnia,
          "current_health": this.current_health,
          "gaming": this.gaming
        };
        console.log(log)
        const response = await fetch('/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(log)
        });
        const data = await response.json();
        if (response.ok) {
          console.log(data);
          localStorage.setItem('user_id', data.user_id);
          window.location.href = '/';
        } else {
          this.error = data.error || 'Ошибка при входе';
        }
      }
    }
  };
</script>


<style scoped>
  input, select {
    box-shadow: none !important; /* Никаких теней */
  }

  #appp {
    min-height: 100vh;
    width: 100vw;
    display: grid;
    place-content: center;

    background: rgb(219, 240, 255);
  }
</style>
