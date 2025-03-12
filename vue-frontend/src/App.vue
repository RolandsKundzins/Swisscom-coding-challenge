<template>
  <div class="container padding-v-2">
    <div class="row">
      <div class="col">
        <h1 class="d3">VueJS+Flask Fullstack Example</h1>
        <!--

        Fill this section with the server response. Feel free to style it as you wish (this is not a design competition).
        If you want to use the Swisscom style guide, you can find it here: https://sdx.swisscom.com/

        -->
        <ul>
            <li v-for="user in users" :key="user.id">{{ user.name }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import axios from 'axios';

const API_BASE_URL = import.meta.env.FLASK_API_URL;

export default defineComponent({
    data() {
        return {
            responseData: null,
            error: null
        };
    },
    async mounted() {
        console.log("I am mounted now");

        try {
            const response = await axios.get(`${API_BASE_URL}/api`);
            this.message = response.data.message;

            console.log("reponse.data:", response.data);
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    }
  /*

  Fill this section with the necessary code to fetch the data from the server
  We have added axios as a dependency, so you can use it to make the request

  */
})
</script>