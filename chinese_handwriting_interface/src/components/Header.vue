<template>
    <div class="header">
        <Counter :top="this.top" :bottom="this.bottom"/>
        <div class="divider"></div>
        <div class="type">{{ this.type }}</div>
    </div>
</template>

<script>
import Counter from './Counter.vue'

export default {
    name: 'Header',
    components: {
        Counter
    },
    data () {
        return {
            top: 12,
            bottom: 20,
            type: 'Translate'
        }
    }
}
</script>