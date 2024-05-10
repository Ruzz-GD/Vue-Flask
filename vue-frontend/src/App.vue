<template>
  <div class="ruzz-gd">
    <!-- GETTED data using axios -->
    <span>VUE WITH AXIOS: {{ message_1 }}</span>
    <button @click="Get1">GET DATA USING AXIOS</button>
    <!-- GETTED data using fetch -->
    <span>VUE WITH FETCH:{{ message_2 }}</span>
    <button @click="Get2">GET DATA USING FETCH</button>
    <!-- send data to you'r database table  -->
    <input type="text" v-model="username" placeholder="username">
    <button @click="send_data_to_database">Send Data To Batabase</button>
  </div>
</template>
<script>
import axios from 'axios';// to use axios we need to import it 
export default{
  data(){
    return{
      username:'',
      message_1:'',
      message_2:'',
    }
  },
  methods:{
    Get1(){
      axios.get('http://127.0.0.1:5000/axios_method')
      .then(response =>{
        this.message_1 = response.data.message;
      })
      .catch(error =>{
        console.error(error)
      })
    },
    Get2(){
      fetch('http://127.0.0.1:5000/fetch_method',{
        method:'GET',
        headers: {
          'Content-Type': 'application/json',
                       
        },
      })
      .then(res => {
        return res.json();
      })
      .then(data =>{
        this.message_2 = data.message;
      })
      .catch(error =>{
        console.error(error)
      })
    },
    send_data_to_database(){
      axios.post('http://127.0.0.1:5000/mysql',{
        username:this.username,
        // this is the data that you gonna pass to backend flask 
      })
      .then(response =>{
        alert(response.data.message)
      })
      .catch(err =>{
        console.error(err)
      })
    }
  }
}
</script>
<style>
body{
  margin:0;
}
.ruzz-gd{
  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 10px;
}
</style>