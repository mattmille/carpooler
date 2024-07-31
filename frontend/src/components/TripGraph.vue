<!-- TripGraph.vue -->
<template>
  <div>
    <canvas ref="chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from 'axios';

export default {
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.fetchAndRenderData();
  },
  methods: {
    async fetchAndRenderData() {
      const response = await axios.get('/api/trips/');
      const trips = response.data;

      console.log(response);

      const ctx = this.$refs.chart.getContext('2d');

      if (this.chart) {
        this.chart.destroy();
      }

      const footer = (tooltipItems) => {
        let sum = 0;

        tooltipItems.forEach(function (tooltipItem) {
          sum += tooltipItem.parsed.y;
        });
        return 'Sum: ' + sum;
      };

      this.chart = new Chart(ctx, {
        type: 'bar',
        data: {
          //labels: trips.map(trip => `User ${trip.user_name}`),
          labels: trips.map(trip => trip.user_name),
          datasets: [{
            label: 'Trip Duration (hours)',
            data: trips.map(trip => this.calculateDuration(trip))
          }]
        },
        options: {
          indexAxis: 'y',
          responsive: true,
          scales: {
            y: {
              beginAtZero: true
            }
          },
          plugins: {
            legend: {
              position: 'right',
            },
            title: {
              display: true,
              text: 'Dates'
            },
            plugins: {
              tooltip: {
                callbacks: {
                  footer: footer,
                }
              }
            }
          }
        }
      });
    },
    calculateDuration(trip) {
      console.log(Date.parse(trip.departure_date));
      console.log(Date.parse(trip.return_date));
      const start = new Date(`${trip.departure_date}T${trip.departure_time}`);
      const end = new Date(`${trip.return_date}T${trip.return_time}`);
      const totalTime = (end - start) / (1000 * 60 * 60); // Duration in hours

      return 20;
    }
  }
}
</script>