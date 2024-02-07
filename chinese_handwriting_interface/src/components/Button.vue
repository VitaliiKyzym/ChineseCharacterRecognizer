<template>
    <div class="button">
        <div class="color_bar" v-bind:class="color"></div>
        <div class="label">{{ label }}</div>
    </div>
</template>

<script>
export default {
    name: 'Button',
    props: ['label', 'color'],
    methods: {
        click () {

        }
    },
}
</script>