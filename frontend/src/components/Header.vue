<template>
    <div>
        <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
            <router-link to="/" class="navbar-brand"><a class="navbar-brand"> ML</a></router-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">

                    <li class="nav-item">
                        <router-link to="/addData" class="nav-link"><a>Add Data</a></router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/runML" class="nav-link"><a>Run ML</a></router-link>
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
    /*
                    <li class="nav-item">
                        <router-link to="/test" class="nav-link"><a>Test</a></router-link>
                    </li>
    */
</script>

<style scoped>
    .navbar-brand {
        text-transform: uppercase;
        margin-left: 10px;
    }

    .navbar {
        border-bottom-left-radius: 5px;
        border-bottom-right-radius: 5px;
    }
</style>
