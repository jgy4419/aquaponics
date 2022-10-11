<template>
  <div style="height:20px; width:70vw">
    <canvas id = "chart" style="height:200px;"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
// import axios from 'axios';
Chart.register(...registerables);
export default {
  methods: {
    fillData(){
      const ctx = document.getElementById('chart').getContext('2d');
      this.myChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: ['221001', '221002', '221003', '221004', '221005', '221006', '221007'],
            datasets: [
              {
                label: '# of Votes',
                data: [5, 2, 3, 50, 20, 40, 10],
                // chartColor: ['#333', '#8e5ea2', '#3cba9f'],
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
        }
      );
    }
  },
  mounted(){
    this.fillData();
  },
  data(){
    return{
      myChart: null
    };
  }
}
</script>

<style lang="scss" scoped>
div{
  color: rgba(219, 252, 171, 0.2)
}
</style>