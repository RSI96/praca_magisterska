<template>
    <div class="page">
        <h1>testjson</h1>
        <p>{{test}}</p>
        <p>{{test.location}}</p>
        <br>
        <h1>endpoint with parameter*2</h1>
        <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="times 2" v-model="parameter">
            <div class="input-group-append">
                <button class="btn btn-outline-dark" type="button" @click="show">Show</button>
            </div>
        </div>
        <p>{{parameter}}</p>
    </div>
</template>

<script>
    import {HTTP} from '../http-common';

    export default {
        name: "Test",
        data() {
            return {
                errors: [],
                test: {},
                parameter: null
            }
        },
        methods: {
            async show() {
                try {
                    const response = await HTTP.get(`testresponse/?value=` + this.parameter)
                    this.parameter = response.data
                } catch (e) {
                    this.errors.push(e)
                }
            }
        },
        async created() {
            try {
                const response = await HTTP.get(`testjson`)
                this.test = response.data
            } catch (e) {
                this.errors.push(e)
            }
            try {
                const response = await HTTP.get(`testresponse/?value=2`)
                this.parameter = response.data
            } catch (e) {
                this.errors.push(e)
            }
        }
    }
</script>