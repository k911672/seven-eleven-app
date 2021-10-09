<template>
  <div>
    <div></div>
    <v-btn color="accent" @click="fetchAPI()">
      APIを取得
    </v-btn>
    <template v-if="fetched">
      <img
        class="image"
        src="https://img.7api-01.dp1.sej.co.jp/item-image/140070/AB52A01A9D707E08388655C41B613141.jpg"
      />
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

<style lang="scss" scoped>
.image {
  width: 100px;
  height: 100px;
}
</style>
