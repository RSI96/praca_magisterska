<template>
  <div class="page">
    <h2>Run alghoritms here</h2>

    <div>
      <select v-model="selectedPair">
        <option v-for="option in pairList" :key="option.id" :value="{column_name: option.column_name, dataset_name: option.dataset_name }" >
          {{ option }}
        </option>
      </select>
      <br>
      <span>Selected: {{ selectedPair }}</span>
        <br>
      <span>cl: {{ selectedPair.column_name }}</span>
    </div>
    <div>
      <select v-model="selectedAlghoritm">
        <option v-for="option in alghoritmList" :key="option.text" :value="option.text">
          {{ option.text }}
        </option>
      </select>
      <span>Selected: {{ selectedAlghoritm }}</span>
    </div>
    <div>
      <button v-on:click="runML()">Baton</button>
      <br>
      <highcharts
        :y_series_1_prop="y_series_1"
        :y_series_2_prop="y_series_2"
      />
      <br>
      <span>Result: {{ result.result }}</span>
      <br>
      <span>y_test: {{ y_series_1 }}</span>
      <br>
      <span>y_pred: {{ y_series_2 }}</span>
    </div>
  </div>
</template>

<script>
//import axios from 'axios';
import { HTTP } from "../http-common";

import Chart from "../components/Chart";

export default {
  name: "runML",
  components: {
    highcharts: Chart
  },
  data() {
    return {
        selectedPair: {id: 2, column_name: 'RainTomorrow', dataset_name:'weatherAUS.csv'},
        selectedAlghoritm: 'RandomForestRegressor',
        pairList: [
        {id: 1, column_name: 'Default', dataset_name:'DefaultDataset'},
        {id: 2, column_name: 'Default2', dataset_name:'DefaultDataset2'}
        ],
        alghoritmList: [
        {text: 'LinearRegression'},
        {text: 'RandomForestRegressor'},
        {text: 'KNeighborsClassifier'}
      ],
        result: {},
        y_series_11: [],
        y_series_2: []
    };
  },
  computed: {
    y_series_1: function () {
      const toNumbers = arr => arr.map(Number);
      return toNumbers(this.y_series_11)
    }
  },
  methods: {
    // runML() {
    //   axios
    //     .post("http://localhost:5000/runML", {
    //           column_name: this.selectedPair.column_name,
    //           dataset_name: this.selectedPair.dataset_name,
    //           alghoritm_name: this.selectedAlghoritm
    //         })
    //     .then(response => (this.result = response.data,
    //                       this.y_series_11 = response.data.y_test))
    //     .then(response => (console.log(response.data)))
    //     .catch(error => console.log(error))
    //     ;
    // },
    async runML() {
      try {
        const response = await HTTP.post("runML", {
              column_name: this.selectedPair.column_name,
              dataset_name: this.selectedPair.dataset_name,
              alghoritm_name: this.selectedAlghoritm
            })
          this.result = response.data,
          this.y_series_11 = response.data.y_test
          this.y_series_2 = response.data.y_pred
      } catch (e) {
        this.errors.push(e)
        }
    }
  },
    async created() {
        try {
            const response = await HTTP.get(`getDistinctPairs`)
            this.pairList = response.data
        } catch (e) {
            this.errors.push(e)
        }
        try {
          const response = await HTTP.post("runML", {
              column_name: this.selectedPair.column_name,
              dataset_name: this.selectedPair.dataset_name,
              alghoritm_name: this.selectedAlghoritm
            })
          this.result = response.data,
          this.y_series_11 = response.data.y_test
          this.y_series_2 = response.data.y_pred
      } catch (e) {
        this.errors.push(e)
        }
    }
};
</script>