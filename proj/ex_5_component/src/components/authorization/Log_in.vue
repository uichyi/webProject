<script setup>
</script>

<template>
  <section class="vh-100 mt-5">
    <div class="container-fluid h-custom">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-md-9 col-lg-6 col-xl-5">
          <img src="https://img.freepik.com/free-vector/placeholder-concept-illustration_114360-4983.jpg"
            class="img-fluid" alt="Sample image">
        </div>
        <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
          <form method='post' id="my_form">
            {% csrf_token %}
            <div class="d-flex flex-row align-items-center justify-content-center">
              <h2 class="text-primary my-5">Вход</h2>
            </div>
            <p class='text-danger'>{{error}}</p>
            <!-- Nickname input -->
            <div data-mdb-input-init class="form-outline mb-4">
              <input type="text" v-model='name' id="nickname" class="form-control form-control-lg"
                placeholder="Введите логин" required/>
            </div>

            <!-- Password input -->
            <div data-mdb-input-init class="form-outline mb-3">
              <input type="password" v-model='password' id="password" class="form-control form-control-lg"
                placeholder="Введите пароль" required/>
            </div>

            <div class="text-center text-lg-start mt-4 pt-2">
              <button @click='checkData' type="submit" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-lg"
                style="padding-left: 2.5rem; padding-right: 2.5rem;">Войти</button>
              <p class="small fw-bold mt-2 pt-1 mb-0">Нет аккаунта? <a href="#!"
                  class="link-primary mb-3">Зарегистрироваться</a></p>
            </div>

          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Books",
    data() {
      return {
        error: '',
        name:'',
        password:''
      };
    },
    methods: {
      async checkData() {
        document.getElementById('my_form').onsubmit = function(event) {
          event.preventDefault();
        }
        if (this.name ==''){
          this.error='Введите никнейм'
          return
        }

        if(this.password == ""){
          this.error='Введите пароль'
          return
        }
        const log =
        {
          "username": this.name,
          "password": this.password
        };
        console.log(log)
        const response = await fetch('/api/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(log)  // Преобразование объекта в JSON
        });

        const data = await response.json();
        if (response.ok) {
          console.log(data);
          localStorage.setItem('user_id', data.user_id);
          window.location.href = '/backend';
        } else {
          this.error = data.error || 'Ошибка при входе';
        }
        localStorage.setItem('user_id', data.user_id);
      }
    }
  };
</script>
