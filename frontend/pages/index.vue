<template>
  <div>
    <div></div>
    <v-btn color="accent" @click="fetchAPI()">
      APIを取得
    </v-btn>
    <template v-if="fetched">
      {{ products }}
    </template>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      products: [],
      fetched: false
    }
  },
  methods: {
    async fetchAPI() {
      try {
        const response = await axios.get(
          'https://madefor.github.io/postal-code-api/api/v1/223/0062.json'
        )
        this.fetched = true
        this.products = response.data
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
