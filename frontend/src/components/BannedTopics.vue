<template>
    <div class="container p-6 space-y-4">
        <h2 class="text-2xl text-white text-semibold">Banned Topics</h2>

        <div class="input-container">
            <input v-model="newItem" placeholder="Enter an item" class="input-field">
            <button @click="addItem" class="submit-button">Submit</button>
        </div>
        <ul class="items-list">
            <li v-for="(item, index) in items" :key="index" class="item">
                <span>{{ item }}</span>
                <button @click="removeItem(index)" class="remove-button">x</button>
            </li>
        </ul>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const newItem = ref('');
const items = ref([]);

function addItem() {
    if (newItem.value.trim() !== '') {
        items.value.push(newItem.value);
        updateS3();
        newItem.value = '';
    }
}

function removeItem(index) {
    items.value.splice(index, 1);
    updateS3();
}


async function updateS3() {
  const s3Url = '';

  try {
    // Fetch the existing JSON object from S3
    const response = await fetch(s3Url);
    if (!response.ok) {
      console.error('Failed to fetch existing data from S3:', response.statusText);
      return;
    }

    const existingData = await response.json();

    // Update the "banned" attribute
    existingData.banned = items.value;

    // Send the modified JSON object back to S3
    const putResponse = await fetch(s3Url, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(existingData),
    });

    if (!putResponse.ok) {
      console.error('Failed to update S3:', putResponse.statusText);
    }
  } catch (error) {
    console.error('Error updating S3:', error);
  }
}
</script>

<style scoped>
.container {
    width: 300px;
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

.items-list {
    list-style-type: none;
    padding: 0;
}

.item {
    display: inline-block;
    background-color: #f0f0f0;
    padding: 5px 10px;
    margin: 5px 10px 5px 0px;
    border-radius: 20px;
}

.remove-button {
    background: none;
    border: none;
    cursor: pointer;
    margin-left: 5px;
}
</style>