<template>
  <div id="app">
    <h1>Carpool Planner</h1>
    <TripForm @trip-added="refreshGraph" />
    <TripGraph ref="graph" />
  </div>
</template>

<script>
import TripForm from './components/TripForm.vue'
import TripGraph from './components/TripGraph.vue'

export default {
  name: 'App',
  components: {
    TripForm,
    TripGraph
  },
  methods: {
    refreshGraph() {
      this.$refs.graph.fetchAndRenderData()
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
