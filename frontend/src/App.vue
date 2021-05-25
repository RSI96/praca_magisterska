<template>
    <div id="app">
        <div id="nav">
            <app-header/>
        </div>
        <div>
            <transition name="slide" mode="out-in">
                <router-view class="view"></router-view>
            </transition>
        </div>
    </div>
</template>

<script>
    import Header from "./components/Header";

    export default {
        components: {
            appHeader: Header
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    .page {
        margin-top: 70px;
    }

    @media screen and (min-width: 768px) {
        .navbar {
            margin-bottom: 30px;
            width: 85vw;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    }

    .slide-enter-active {
        animation: slide-in 200ms ease-out forwards;
    }

    .slide-leave-active {
        animation: slide-out 200ms ease-out forwards;
    }

    @keyframes slide-in {
        0% {
            transform: translateY(1rem);
            opacity: 0;
        }
        100% {
            transform: translateY(0);
            opacity: 1;
        }
    }

    @keyframes slide-out {
        0% {
            transform: translateY(0);
            opacity: 1;
        }
        100% {
            transform: translateY(1rem);
            opacity: 0;
        }
    }
</style>
