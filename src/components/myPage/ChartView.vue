<template>
  <div>
    <canvas id = "chart" width="600" height="150"></canvas>
  </div>
</template>

<script>
import { BarElement, Chart } from 'chart.js';
import { BarController, CategoryScale, LinearScale } from 'chart.js';
Chart.register( BarElement, BarController, LinearScale, CategoryScale);
export default {
  methods: {
    fillData(){
      const ctx = document.getElementById('chart').getContext('2d');
      this.myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
          datasets: [
            {
              label: '# of Votes',
              data: [12, 20, 3, 5, 2, 3],
              backgroundColor: [
                'rgba(219, 252, 0, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)'
              ],
              borderColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
              ],
              borderWidth: 1
            }
          ]
        },
        option: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
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