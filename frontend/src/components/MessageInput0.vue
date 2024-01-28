<template>
    <div class="container p-6 space-y-4">
        <h2 class="text-2xl text-white text-semibold">Make Teddy say something</h2>

        <div class="input-container">
            <input placeholder="Enter Message" class="input-field">
            <button class="submit-button">Submit</button>
        </div>
    </div>
</template>

<style scoped>
.container {
    width: 500px;
}

.input-container {
    display: flex;
    justify-content: space-between;
}

.input-field {
    flex-grow: 1;
    margin-right: 10px;
}

.submit-button {
    background-color: rgb(0, 149, 255);
    padding: 5px 10px;
}
</style>