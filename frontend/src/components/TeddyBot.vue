<template>
    <div class="my-4 teddy-bot">
        <div class="teddy-bot-header">
            <img src="../assets/teddy.jpg" alt="Teddy Bear" class="teddy-bot-profile-pic" />
            <h1 class="text-white teddy-bot-title">Teddy Bot</h1>
        </div>
        <button class="turn-off-button">Turn Off</button>
    </div>
</template>

<style>
.teddy-bot {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.teddy-bot-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
}

.teddy-bot-profile-pic {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

.teddy-bot-title {
    font-size: 20px;
    margin-top: 10px;
}

.turn-off-button {
    padding: 8px 16px;
    background-color: #f44336;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 12px;
    cursor: pointer;
}
</style>
