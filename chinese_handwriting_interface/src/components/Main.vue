<template>
    <div class="main_container">
        <Header/>
        <Form/>
    </div>
</template>

<script>
import Header from './Header.vue'
import Form from './Form.vue'

export default {
    name: 'Main',
    components: {
        Header, Form
    }
}
</script>