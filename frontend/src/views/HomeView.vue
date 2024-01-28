<script setup>
import BannedTopics from '@/components/BannedTopics.vue';
import ChatLog from '@/components/ChatLog.vue';
import MessageInput from '@/components/MessageInput.vue';
import RecentlyDiscussed from '@/components/RecentlyDiscussed.vue';
import SuggestedTopics from '@/components/SuggestedTopics.vue';
import TeddyBot from '@/components/TeddyBot.vue';
</script>

<template>
  <main>
    <TeddyBot />

    <div class="flex flex-row justify-center w-full mx-auto">
      <ChatLog />
      <div class="flex flex-col">
        <SuggestedTopics />
        <BannedTopics />
        <MessageInput />
      </div>

    </div>
    <RecentlyDiscussed />
  </main>
</template>
