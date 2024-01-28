<template>
    <div class="container p-6 space-y-4">
      <h2 class="text-2xl text-white text-semibold">Make Teddy say something</h2>
  
      <div class="input-container">
        <input ref="inputField" placeholder="Enter Message" class="input-field">
        <button class="submit-button" @click="handleSubmit">Submit</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const inputField = ref(null);
  
  const handleSubmit = async () => {
    try {
      // Read content from the input field
      const message = inputField.value.value;
  
      // Create JSON content
      const jsonContent = JSON.stringify({ data: message }, null, 2);
  
      // Upload the JSON document to S3
      await uploadToS3(jsonContent);
  
      // Optional: Show success message or perform other actions
      console.log('JSON document uploaded successfully');
    } catch (error) {
      console.error('Error uploading JSON document:', error);
      // Handle error, show error message, etc.
    }
  };
  
  const uploadToS3 = async (content) => {
  try {
    // Set your S3 bucket name and the destination file name
    const bucketName = 'teddyconversationhistory';
    const fileName = 'message.json';

    // Construct the S3 endpoint URL
    const s3Endpoint = `https://${bucketName}.s3.amazonaws.com/${fileName}`;

    // Make a PUT request to upload the JSON content to S3
    await fetch(s3Endpoint, {
      method: 'PUT',
      body: content,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    console.log('JSON document uploaded successfully');
  } catch (error) {
    console.error('Error uploading JSON document:', error);
    // Handle error, show error message, etc.
  }
};
  </script>
  
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
  