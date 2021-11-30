<template>
  <card>
    <h4 slot="header" class="card-title">Edit Profile</h4>
    <form>
      <div class="row">
        <div class="col-md-5">
          <base-input
            type="text"
            label="Company"
            :disabled="true"
            placeholder="Light dashboard"
            v-model="user.company"
          >
          </base-input>
        </div>
        <div class="col-md-3">
          <base-input
            type="text"
            label="Username"
            placeholder="Username"
            v-model="user.username"
          >
          </base-input>
        </div>
        <div class="col-md-4">
          <base-input
            type="email"
            label="Email"
            placeholder="Email"
            v-model="user.email"
          >
          </base-input>
        </div>
      </div>

      <div class="row">
        <div class="col-md-6">
          <base-input
            type="text"
            label="First Name"
            placeholder="First Name"
            v-model="user.firstName"
          >
          </base-input>
        </div>
        <div class="col-md-6">
          <base-input
            type="text"
            label="Last Name"
            placeholder="Last Name"
            v-model="user.lastName"
          >
          </base-input>
        </div>
      </div>

      <div class="row">
        <div class="col-md-12">
          <base-input
            type="text"
            label="Address"
            placeholder="Home Address"
            v-model="user.address"
          >
          </base-input>
        </div>
      </div>

      <div class="row">
        <div class="col-md-4">
          <base-input
            type="text"
            label="City"
            placeholder="City"
            v-model="user.city"
          >
          </base-input>
        </div>
        <div class="col-md-4">
          <base-input
            type="text"
            label="Country"
            placeholder="Country"
            v-model="user.country"
          >
          </base-input>
        </div>
        <div class="col-md-4">
          <base-input
            type="number"
            label="Postal Code"
            placeholder="ZIP Code"
            v-model="user.postalCode"
          >
          </base-input>
        </div>
      </div>

      <div class="row">
        <div class="col-md-12">
          <div class="form-group">
            <label>About Me</label>
            <textarea
              rows="5"
              class="form-control border-input"
              placeholder="Here can be your description"
              v-model="user.aboutMe"
            >
            </textarea>
          </div>
        </div>
      </div>
      <div class="text-center">
        <button
          type="submit"
          class="btn btn-info btn-fill float-right"
          @click.prevent="updateProfile"
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
import axios from "axios";
export default {
  components: {
    Card,
  },
  data() {
    return {
      user: {
        company: "Light dashboard",
        username: "michael23",
        email: "",
        firstName: "Mike",
        lastName: "Andrew",
        address: "Melbourne, Australia",
        city: "melbourne",
        country: "Australia",
        postalCode: "",
        aboutMe: `Lamborghini Mercy, Your chick she so thirsty, I'm in that two seat Lambo.`,
      },
    };
  },
  methods: {
    updateProfile() {
      alert("Your data: " + JSON.stringify(this.user));
    },
    async validatePredictProgram() {
      this.fireSnackbar = true;
      this.messageSnackbar = "Loading...";
      var axios = require("axios");
      var FormData = require("form-data");
      var data = new FormData();
      data.append("gwa", this.gwa);
      data.append("strand", this.strand);
      data.append("admissionScore", this.admissionScore);

      var config = {
        method: "post",
        url: "http://localhost:5000/recommend-program",
        headers: {},
        data: data,
      };

      await axios(config)
        .then((response) => {
          console.log(JSON.stringify(response.data));
          this.replied = true;
          this.recommendedProgram = response.data.program;
          console.log(JSON.stringify(response.data.program));
          this.fireSnackbar = false;
        })
        .catch((error) => {
          console.log(error);
          this.replied = true;
          this.fireSnackbar = true;
          this.messageSnackbar =
            "There is an error attempting to predict your program";
        });
    },
  },
};
</script>
<style></style>
