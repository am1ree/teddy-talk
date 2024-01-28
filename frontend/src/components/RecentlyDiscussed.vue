<template>
    <div class="flex flex-col justify-center w-full p-6 mx-auto">
        <h2 class="mb-4 text-2xl text-center">Recently discussed topics</h2>
        <ol class="pl-6 mx-auto list-disc">
            <div class="item">Travels</div>
            <div class="item">Cooking</div>
            <div class="item">School Stories</div>
            <div class="item">French language</div>
        </ol>
    </div>
</template>

<script>
export default {
    name: 'RecentlyDiscussed',
}
</script>

<style scoped>
.item {
    display: inline-block;
    color: #000;
    background-color: #f0f0f0;
    padding: 5px 10px;
    margin: 5px 10px 5px 0px;
    border-radius: 20px;
}

li {
    list-style: lower-roman;
}

* {
    color: #fff;
}
</style>
