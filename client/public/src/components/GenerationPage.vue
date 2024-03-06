<!-- Script setup-->

<script setup lang='ts'>
import { ref } from "vue";

// Tone dropdown select script setup
const selectedTone = ref();
const tone = ref([
    { name: 'Amused' },
    { name: 'Apologetic' },
    { name: 'Assertive' },
    { name: 'Authoritative' },
    { name: 'Cooperative' },
    { name: 'Conversational' },
    { name: 'Curious' },
    { name: 'Encouraging' },
    { name: 'Formal' },
    { name: 'Friendly' },
    { name: 'Humorous' },
    { name: 'Humor' },
    { name: 'Informative' },
    { name: 'Joyful' },
    { name: 'Optimistic' },
    { name: 'Passionate' },
    { name: 'Persuasive' },
    { name: 'Pessimistic' },
    { name: 'Sad' },
    { name: 'Serious' },
    { name: 'Tense' },
    { name: 'Worried' },  
]);

 // Audience dropdown select script setup
const selectedAudience = ref();
const audience = ref([
    { name: 'Uninformed' },
    { name: 'Managerial' },
    { name: 'Readers' },
    { name: 'Friendly' },
    { name: 'Academic audiences' },
    { name: 'Expert audience' },
    { name: 'Hostile' },
    { name: 'Apathy' },
    { name: 'Neutral' },
    { name: 'Assumptions about audience' }
]);

const generate = ref('');
</script>


<template>
  <div class="generation-page h-screen flex flex-col justify-end items-center text-l text-gray-800">
    
    <div>
    <!-- Display received messages -->
    <div
      v-for="(message, index) in receivedMessages"
      :key="index"
      class="received-message bg-gray-900 w-fit text-white rounded-lg p-2 m-2 md:object-left">
      
      {{ message }}
      
    </div>
<button @click="copyMessage(message.text)">Copy</button>
    <!-- Display sent messages -->
    <div
      v-for="(message, index) in sentMessages"
      :key="index"
      class="sent-message bg-gray-900 w-fit text-white rounded-lg p-2 mb-5 md:object-right"
    >
      {{ message }}
    </div>

    
  </div>
    <!-- Title label-->
    <div
    class="mb-3">
      <label 
      for="default-input" 
      class="subpixel-antialiased block mb-1 text-2xl font-medium text-gray-700 dark:text-white">Title</label>
      <input
      type="text" 
      id="default-input" 
      class="subpixel-antialiased default-input bg-gray-100 border border-indigo-300 text-gray-900 text-xl rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-700 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
    </div>

    <!-- Radiobutton type select-->
    <div class="flex flex-wrap gap-3 mb-2 p-2 text-xl">
      <div class="flex items-center">
          <RadioButton v-model="generate" inputId="type1" name="newsletter" value="Newsletter" class="bg-indigo-700"/>
          <label for="newsletter" class="mr-2">Newsletter</label>
      </div>
      <div class="flex items-center">
          <RadioButton v-model="generate" inputId="type2" name="article" value="Article" class="bg-indigo-700"/>
          <label for="article" class="ml-2">Article</label>
      </div>
  </div>

    <!-- Dropdown selects-->
    <div class="dropdown flex items-center pt-1 pb-4 pr-4 rounded-lg">
    <!-- Tone dropdown select-->
    <div class="card flex justify-center mb-3 mr-3 ">
      <MultiSelect v-model="selectedTone" :options="tone" optionLabel="name" placeholder="Select Tones"
          :maxSelectedLabels="3" class="w-full md:w-[20rem] bg-gray-300" />
  </div>

    <!-- Audience dropdown select  -->
    <div class="card flex justify-center mb-3 ml-3">
      <MultiSelect v-model="selectedAudience" :options="audience" optionLabel="name" placeholder="Select Audience"
          :maxSelectedLabels="3" class="w-full md:w-[20rem] bg-gray-300" />
  </div>
</div>

    <!-- Input form -->
    <form class="flex items-center pt-1 pb-4 pr-4 rounded-lg md:w-[20rem]" @submit.prevent="sendMessage">
      <textarea
        v-model="newMessage"
        rows="1"
        cols="80"
        class="block mx-9 p-2 w-full text-xl object-center text-gray-700 bg-white rounded-lg border border-purple-100 focus:ring-blue-700 focus:border-blue-500 dark:bg-gray-100 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="Your prompt..."
      ></textarea>
      <button
        type="submit"
        class="p-1 text-blue-600 rounded-full cursor-pointer hover:bg-blue-100 dark:text-blue-500 dark:hover:bg-gray-600"
      >
        <svg
          class="w-10 h-10 rotate-90 rtl:-rotate-90"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="currentColor"
          viewBox="0 0 18 20"
        >
          <path
            d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z"
          />
        </svg>
        <span class="sr-only">Send message</span>
      </button>
    </form>
  </div>
</template>


<!-- Script logic for messages-->
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

export default {
  data() {
    return {
      receivedMessages: ['Hello there!', 'How may I help you today?'],
      sentMessages: [''],
      newMessage: ''
    }
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim()) {
        this.sentMessages.push(this.newMessage)
        this.newMessage = ''
      }
    }
  },
  copyMessage(text: string) {
    navigator.clipboard.writeText(text)
      .then(() => {
        console.log('Message copied to clipboard');
        // You can add a toast or notification here to inform the user
      })
      .catch((error) => {
        console.error('Failed to copy message:', error);
        // Handle error, e.g., show an error toast
      });
  }
}
</script>


<style scoped>
form {
  margin-left: 15em;
  margin-right: 10em;
  margin-bottom: 0.5em;
  min-width: 750px; /* min-width for responsiveness */
  max-width: 600px;
  align-items: center;
}

.default-input {
 min-width: 400px;
 max-width: 300px;
}

.received-message {
  width: auto;
  color: #fff;
  background-color: #000;
}
</style>
