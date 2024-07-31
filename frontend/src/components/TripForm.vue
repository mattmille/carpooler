<!-- TripForm.vue -->
<template>
  <form @submit.prevent="submitTrip">
    <input v-model="trip.departure_date" type="date">
    <input v-model="trip.departure_time" type="time">
    <input v-model="trip.return_date" type="date">
    <input v-model="trip.return_time" type="time">
    <button type="submit">Submit Trip</button>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      trip: {
        user_id: 1, // This should be dynamically set based on the logged-in user
        departure_date: '',
        departure_time: '',
        return_date: '',
        return_time: ''
      }
    }
  },
  methods: {
    async submitTrip() {
      try {
        await axios.post('/api/trips/', this.trip);
        this.$emit('trip-added');
        // Reset form or show success message
      } catch (error) {
        // Handle error
      }
    }
  }
}
</script>