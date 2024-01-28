<script setup>
import { onMounted, ref } from 'vue';

let data = ref(null);

onMounted(() => {
    fetch('', {
  method: 'GET',
  headers: {
    'Cache-Control': 'no-store'
  }})
        .then(response => response.json())
        .then(jsonData => {
            data.value = jsonData.data;
        });

    setInterval(() => {
        fetch('', {
  method: 'GET',
  headers: {
    'Cache-Control': 'no-store'
  }})
            .then(response => response.json())
            .then(jsonData => {
                data.value = jsonData.data;
            });
    }, 5000);
});
function formatTimestamp(timestamp) {
    let date = new Date(timestamp);
    return date.toLocaleString();
}
</script>

<template>
    <div class="flex flex-col m-8 space-y-4 w-[40%]">
        <h1 class="text-2xl text-white ">Chat Log</h1>
        <div class="p-4 bg-white max-h-[50vh] overflow-auto rounded-lg shadow-lg">
            <div v-for="(message, index) in data" :key="index" class="mb-4">
                <div class="max-w-lg"
                    :class="{ 'bubble-blue': message.speaker === 'Teddy Assistant', 'bubble-dark': message.speaker !== 'Teddy Assistant' }">
                    <p class="text-sm text-gray-200">{{ formatTimestamp(message.timestamp) }}</p>
                    <p class="font-bold text-gray-400">{{ message.speaker }}</p>
                    <p class="text-gray-200">{{ message.message }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
  
<style scoped>
.bubble-blue {
    background-color: #2a2aca;
    border-radius: 10px;
    padding: 10px;
    color: white;
    margin: 0 0 0 auto;
}

.bubble-dark {
    background-color: #a910a9;
    border-radius: 10px;
    padding: 10px;
    color: white;
}
</style>