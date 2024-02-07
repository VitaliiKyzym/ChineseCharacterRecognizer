<template>
    <div class="counter">
        <div class="top">{{ top }}</div>
        <div class="divider"></div>
        <div class="bottom">{{ bottom }}</div>
    </div>
</template>

<script>
export default {
    name: 'Counter',
    props: ['top', 'bottom']
}
</script>