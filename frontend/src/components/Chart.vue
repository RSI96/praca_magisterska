<template>
    <div class="row justify-content-center">
        <div class="col-lg-6 col-md-8 col-sm-10">
            <highcharts
                :options="chartOptions"
            ></highcharts>
        </div>
    </div>
</template>

<script>
import {Chart} from 'highcharts-vue'

export default {
    components: {
        highcharts: Chart
    },
    props: {
        y_series_1_prop: Array,
        y_series_2_prop: Array
    },
    data() {
        return {
            chartOptions: {
                turboThreshold: 0,
                title: {
                    text: 'Title'
                },
                yAxis: {
                    title: {
                        text: 'Y Title'
                    }
                },
                tooltip: {
                    crosshairs: true,
                },
                plotOptions: {
                    series: {
                        color: 'var(--dark)'
                    }
                },
                series: [
                {
                    name: 'Some text',
                    data: this.y_series_1_prop,
                },
                {
                    name: 'Some text',
                    data: this.y_series_2_prop,
                }
                ]
            }
        };
  }
};
</script>
