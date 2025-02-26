<script setup>
</script>

<template>
  <section class="vh-100" style='background:#dbf0ff'>
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-lg-12 col-xl-11">
          <div class="card text-black">
            <div class="card-body p-md-5">
              <div class="row justify-content-center">
                <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                  <p class="text-center text-primary h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Регистрация</p>
                  <form class="mx-1 mx-md-4" method='post'>
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
                  <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp"
                    class="img-fluid" alt="Sample image">

                </div>
              </div>
            </div>
          </div>
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
        password1:'',
        password2:''
      };
    },
    methods: {
      checkData() {
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
      }
    }
  };
</script>


<style scoped>
  input, select {
    box-shadow: none !important; /* Никаких теней */
  }
</style>

