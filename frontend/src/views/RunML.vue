<template>
  <div class="page">
    <h2>Run and visualize</h2>
    <br>
    <div class="row justify-content-center">
    <div class="col-lg-6 col-md-6 col-sm-4" >
      <h3>Select Dataset and Column</h3>
      <select class="form-select" v-model="selectedPair">
        <option v-for="option in pairList" :key="option.id" :value="{column_name: option.column_name, dataset_name: option.dataset_name }" >
          <span>Column Name: {{ option.column_name }}, Dataset: {{ option.dataset_name}}</span>
        </option>
      </select>
      <br>
      <span>Selected Column Name: {{ selectedPair.column_name }} and Dataset: {{ selectedPair.dataset_name}}</span>
    </div>
    </div>
    <br>
    <div class="row justify-content-center">
    <div class="col-lg-6 col-md-6 col-sm-4" >
      <h3>Select Alghoritm</h3>
      <select class="form-select" v-model="selectedAlghoritm">
        <option v-for="option in alghoritmList" :key="option.text" :value="option.text">
          {{ option.text }}
        </option>
      </select>
      <br>
      <span>Selected Alghoritm: {{ selectedAlghoritm }}</span>
    </div>
    </div>
    <div>
      <br>
      <button type="button" class="btn btn-dark" v-on:click="runML()">Run ML alghoritm</button>
      <br>
      <div>
        <br>
        <h3>Result: {{ result.result }}</h3>
      </div>
      <div class="row justify-content-center">
        <div class="col-lg-11 col-md-10 col-sm-8">
          <apexcharts type="line" :options="chartOptions" :series="series"></apexcharts>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
//import axios from 'axios';
import { HTTP } from "../http-common";
//import Chart from "../components/Chart";

//import LineChart from '../components/LineChart.vue'

import VueApexCharts from 'vue-apexcharts'

export default {
  name: "runML",
  components: {
    //highcharts: Chart,
    //LineChart
    apexcharts: VueApexCharts,
  },
  data() {
    return {
        chartOptions: {
          chart: {
            id: 'vuechart-example',
          },
          // xaxis: {
          //   categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
          // },
        },
        series: [{
          name: 'y_test',
          data: []
        },
        {
          name: 'y_pred',
          data: []
        }],



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
    };
  },

  methods: {
    async runML() {
      try {
        const response = await HTTP.post("runML", {
              column_name: this.selectedPair.column_name,
              dataset_name: this.selectedPair.dataset_name,
              alghoritm_name: this.selectedAlghoritm
            })
          this.result = response.data,
          this.series = [{
          data: response.data.y_test.slice(0, 100)
          },
          {
          data: response.data.y_pred.slice(0, 100)
          }]
      } catch (e) {
        this.errors.push(e)
        }

      },

  },
    async created() {
        try {
            const response = await HTTP.get(`getDistinctPairs`)
            this.pairList = response.data
        } catch (e) {
            this.errors.push(e)
        }
    }
};
</script>
