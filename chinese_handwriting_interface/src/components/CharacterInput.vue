<template>
  <div class="button_container">
    <Button label="Trace" color="green" @click="trace()"/>
    <Button label="Clear" color="red" @click="clear()" />
  </div>
  <div class="character_input_container">
    <Editor
      :canvasWidth="515"
      :canvasHeight="515"
      ref="editor"
      editorId="canvasId"
    />
  </div>
</template>

<script>
  import Editor from "vue-image-markup";
  import Button from "./Button.vue";

  import axios from 'axios'

  import {emitter} from "../mitt";

  export default {
    name: "CharacterInput",
    components: {
      Editor,
      Button,
    },
    data() {
      return {
        freeDrawingOptions: {
          stroke: "black",
          strokeWidth: "30",
          background: "red",
          response: []
        },
      };
    },
    mounted() {
      this.$refs.editor.set("freeDrawing", this.freeDrawingOptions);
    },
    methods: {
      trace () {
        let image = this.$refs.editor.saveImage()
        let data = new FormData();
        let url = process.env.VUE_APP_SERVER_URL + "/trace"

        data.append('image', image);

        let config = {
          method: 'post',
          url: url,
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          },
          data: data,
          response: ''
        };

        axios(config)
        .then(response => {
          emitter.emit("character-input", response.data.character);
        })
        .catch(function (error) {
            console.log(error);
          });      
      },
      clear() {
        this.$refs.editor.clear();
      }
    },
  };
</script>