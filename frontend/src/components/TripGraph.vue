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

      const ctx = this.$refs.chart.getContext('2d');

      if (this.chart) {
        this.chart.destroy();
      }

      this.chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: trips.map(trip => `User ${trip.user_id}`),
          datasets: [{
            label: 'Trip Duration (hours)',
            data: trips.map(trip => this.calculateDuration(trip))
          }]
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    },
    calculateDuration(trip) {
      const start = new Date(`${trip.departure_date}T${trip.departure_time}`);
      const end = new Date(`${trip.return_date}T${trip.return_time}`);
      return (end - start) / (1000 * 60 * 60); // Duration in hours
    }
  }
}
</script>