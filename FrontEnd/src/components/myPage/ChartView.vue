<template>
  <div style="width:75vw;">
    <canvas id = "chart" class="chart"/>
    <canvas id = "chart2" class="chart"/>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
import axios from 'axios';
Chart.register(...registerables);
export default {
  data(){
    return{
      myChart: null,
      chartData: {
        humidity: [],
        lux: [],
        temperature: [],
        time: []
      },
      waterData: 0
    };
  },
  methods: {
    luxData(){
      const ctx = document.getElementById('chart2').getContext('2d');
      setTimeout(() => {
      this.myChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: [...this.chartData.time],
            datasets: [
              {
                label: '조도',
                data: [...this.chartData.lux],
                backgroundColor: '#3cba9f',
                borderColor: 'rgb(7, 95, 95)',
                postDetailChartState: 0,
                borderWidth: 1
              }
            ]
          },
          options: {
            title: {
              display: true,
              responsive: false,
              text: 'World population per region (in millions)'
            },
            animation: {
              animateScale: true,
              animateRotate: true,
            }
          },
        });
      }, 1000);
    },
      fillData(){
      const ctx = document.getElementById('chart').getContext('2d');
      setTimeout(() => {
      this.myChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: [...this.chartData.time],
            datasets: [
              {
                label: '습도',
                data: [...this.chartData.humidity],
                backgroundColor: '#3e95cd',
                borderColor: 'rgb(7, 95, 95)',
                postDetailChartState: 0,
                borderWidth: 1
              },
              {
                label: '온도',
                data: [...this.chartData.temperature],
                backgroundColor: '#8e5ea2',
                borderColor: 'rgb(7, 95, 95)',
                postDetailChartState: 0,
                borderWidth: 1
              }
            ]
          },
          options: {
            title: {
              display: true,
              responsive: false,
              text: 'World population per region (in millions)'
            },
            animation: {
              animateScale: true,
              animateRotate: true,
            }
          },
        });
      }, 1000);
    }
  },
  mounted(){
    this.fillData();
    this.luxData();
  },
  created(){
    // setInterval(() => {
      axios.get(`http://127.0.0.1:5000/sensor`)
      .then(res => {
        for(let i = 0; i < res.data.length; i++){
          this.chartData.humidity.push(Number(res.data[i].humidity));
          this.chartData.lux.push(Number(res.data[i].lux));
          this.chartData.time.push(res.data[i].time.toString());
          this.chartData.temperature.push(Number(res.data[i].temperature));
        }
      })
    // }, 10000);
  },
}
</script>

<style lang="scss" scoped>
div{
  color: rgba(219, 252, 171, 0.2)
}
</style>