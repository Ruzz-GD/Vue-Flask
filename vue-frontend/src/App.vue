<template>
  <div class="ruzz-gd">
    <!-- GETTED data using axios -->
    <span class="data-message">VUE WITH AXIOS: {{ message_1 }}</span>
    <button class="fetch-button" @click="Get1">GET DATA USING AXIOS</button>
    <!-- GETTED data using fetch -->
    <span class="data-message">VUE WITH FETCH: {{ message_2 }}</span>
    <button class="fetch-button" @click="Get2">GET DATA USING FETCH</button>
    <!-- send data to your database table -->
     <button class="fetch-button" style="background-color: lawngreen;" @click="refreshpage">REFRESH</button>
  </div>
</template>

<script>
import axios from 'axios'; // to use axios we need to import it
export default {
  data() {
    return {
      message_1: '',
      message_2: '',
    }
  },
  methods: {
     // this method get the data in flask-backend/FlaskApp.py using .then
    Get1() {
      axios.get('http://127.0.0.1:5000/axios_method')
        // stored the message data from backend to frontend message_1: '',
        .then(response => {
          this.message_1 = response.data.message;
        })
        // this methods catch the error if function fail
        .catch(error => {
          this.message_1 = error
        })
    },
    // this method get the data in flask-backend/FlaskApp.py useing async
    async Get2() {
      try {
        const res = await fetch('http://127.0.0.1:5000/fetch_method', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const data = await res.json();
        // stored the message data from backend to frontend message_2: '',
        this.message_2 = data.message;
      } catch (error) { // this methods catch the error if function fail
        this.message_2 = error;
      }
    },
    refreshpage(){
      window.location.reload();
    }
  }
}
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif; /* Sets a clean font for the body */
}

.ruzz-gd {
  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 20px; /* Increased gap for better spacing */
  background-color: #f0f0f0; /* Light gray background */
}

.data-message {
  font-size: 18px; /* Increases font size for messages */
  color: #333; /* Darker text color for readability */
}

.fetch-button {
  padding: 10px 20px; /* Padding for better button size */
  font-size: 16px; /* Font size for button text */
  color: white; /* Button text color */
  background-color: #007bff; /* Button background color */
  border: none; /* No border */
  border-radius: 5px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
  transition: background-color 0.3s; /* Smooth transition for background color */
}

.fetch-button:hover {
  background-color: #0056b3; /* Darker blue on hover */
}
</style>
