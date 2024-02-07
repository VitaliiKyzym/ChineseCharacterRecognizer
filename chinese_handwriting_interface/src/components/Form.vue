<template>
    <div class="form">
        <div class="prompt">{{ this.prompt }}</div>
        <div class="answer">
            <input v-model="answer" type="text" name="answer">
        </div>
    </div>
</template>
<script>

    import {emitter} from '../mitt'

    export default {
        name: 'Form',
        data () {
            return {
                prompt: 'How are you?',
                answer: ''
            }
        },
        mounted () {
            emitter.on("character-input", character => {
                console.log(character)
                this.answer += character;
            })
        }
    }
</script>