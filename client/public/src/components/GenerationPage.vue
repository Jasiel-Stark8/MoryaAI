<template>
  <div class="h-screen flex flex-col justify-end items-center">
    <!-- Display received messages -->
    <div
      v-for="(message, index) in receivedMessages"
      :key="index"
      class="bg-gray-700 w-fit text-white rounded-lg p-2 m-2 md:object-left"
    >
      {{ message }}
    </div>

    <!-- Display sent messages -->
    <div
      v-for="(message, index) in sentMessages"
      :key="index"
      class="bg-gray-200 w-fit text-black rounded-lg p-2 m-2 md:object-right"
    >
      {{ message }}
    </div>
    <!-- Toggle label-->

    <!-- Input form -->
    <form
      class="flex items-center pt-6 pb-4 pr-4 rounded-lg"
      @submit.prevent="sendMessage"
    >
      <textarea
        v-model="newMessage"
        rows="1"
        cols="150"
        class="block mx-4 p-2.5 w-70 text-sm object-center text-gray-900 bg-white rounded-lg border border-gray-300 focus:ring-blue-700 focus:border-blue-500 dark:bg-gray-100 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="Your prompt..."
      ></textarea>
      <button
        type="submit"
        class="p-2 text-blue-600 rounded-full cursor-pointer hover:bg-blue-100 dark:text-blue-500 dark:hover:bg-gray-600"
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

<script>
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
  }
}
</script>

<style scoped>
/* Add your styling for received and sent messages here */
.received-message {
  text-align: left;
  /* Add other styles as needed */
}

.sent-message {
  text-align: right;
  /* Add other styles as needed */
}

.chat-form {
  /* Add form styling as needed */
}
</style>
