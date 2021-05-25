<template>
    <div>
        <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
            <router-link to="/" class="navbar-brand"><a>Nazwa</a></router-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link to="/test" class="nav-link"><a>Test</a></router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/addData" class="nav-link"><a>Add Data</a></router-link>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
    export default {
        name: "Header"
    }
</script>

<style scoped>
    .navbar-brand {
        text-transform: uppercase;
    }
</style>
