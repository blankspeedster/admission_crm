<template>
  <card>
    <h4 slot="header" class="card-title">Predict Population</h4>
    <form>
      <div class="row">
        <div class="col-md-3">
          <base-input
            type="number"
            label="Year"
            placeholder="2022"
            v-model="year"
          >
          </base-input>
        </div>
        <div class="col-md-3">
          <base-input
            type="number"
            label="Rooms"
            placeholder="0"
            v-model="rooms"
          >
          </base-input>
        </div>
        <div class="col-md-3">
          <base-input
            type="number"
            label="Number of Full Time"
            placeholder="0"
            v-model="fullTime"
          >
          </base-input>
        </div>
        <div class="col-md-3">
          <base-input
            type="number"
            label="Number of Part Time"
            placeholder="0"
            v-model="partTime"
          >
          </base-input>
        </div>
        <div v-if="replied" class="col-md-12">
          The predicted population is: {{population}}
        </div>
        <div v-if="fireError" class="col-md-12">
          {{errorMessage}}
        </div>
      </div>

      <div class="row"></div>
      <div class="text-center">
        <button
          type="submit"
          class="btn btn-primary btn-fill float-right"
          @click.prevent="validatePredictProgram"
        >
          Update Profile
        </button>
      </div>
      <div class="clearfix"></div>
    </form>
  </card>
</template>
<script>
import Card from "src/components/Cards/Card.vue";

export default {
  components: {
    Card,
  },
  data() {
    return {
        year: 2022,
        rooms: 0,
        fullTime: 0,
        partTime: 0,

        population: 0,

        fireError: false,
        fireMessage: "",
        replied: false,
    };
  },
  methods: {
    updateProfile() {
      alert("Your data: " + JSON.stringify(this.user));
    },
    async validatePredictProgram() {
      this.fireError = true;
      this.errorMessage = "Loading...";
      var axios = require("axios");
      var FormData = require("form-data");
      var data = new FormData();
      
      data.append("year", this.year);
      data.append("rooms", this.rooms);
      data.append("fullTime", this.fullTime);
      data.append("partTime", this.partTime);


      var config = {
        method: "post",
        url: "http://localhost:5000/get-population",
        headers: {},
        data: data,
      };

      await axios(config)
        .then((response) => {
          this.replied = true;
          this.population = response.data.population;
          this.fireError = false;
        })
        .catch((error) => {
          this.replied = true;
          this.fireError = true;
          this.errorMessage =
            "There is an error attempting to predict the population";
        });
    },
  },
};
</script>
<style></style>
