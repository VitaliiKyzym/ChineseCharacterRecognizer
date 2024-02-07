<template>
  <div class="root_container">
    <Main/>
    <CharacterInput v-on:status="test"/>
  </div>
</template>

<script>
import CharacterInput from './components/CharacterInput.vue'
import Main from './components/Main.vue'

export default {
  name: 'App',
  components: {
    CharacterInput, Main
  },
  methods: {
    character (data) {
      console.log(data.character)
    },
    test (message) {
      console.log(message)
    }
  },
}
</script>

<style lang="scss">
@import "./styles/main.scss";
</style>
