<!-- TripForm.vue -->
<template>
  <form @submit.prevent="submitTrip">
    <input v-model="trip.user_name" type="string">
    <input v-model="trip.departure_date" type="date">
    <select v-model="trip.departure_time">
      <option value="Morning">Morning</option>
      <option value="Afternoon">Afternoon</option>
      <option value="Night">Night</option>
    </select>
    <!-- <input v-model="trip.departure_time" type="time"> -->
    <input v-model="trip.return_date" type="date">
    <select v-model="trip.return_time">
      <option value="Morning">Morning</option>
      <option value="Afternoon">Afternoon</option>
      <option value="Night">Night</option>
    </select>
    <!-- <input v-model="trip.return_time" type="time"> -->
    <button type="submit">Submit Trip</button>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      trip: {
        user_name: '',
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
        console.log(this.trip);
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