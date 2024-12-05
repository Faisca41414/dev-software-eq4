<!-- Chat.svelte -->
<script lang="ts">
    export let messages: { username: string, message: string }[];
    export let message = "Hello sir";
    export let handleAdd: () => void;
  </script>
  
  <div class="chat-container">
    <div class="input-container">
      <input class="message-input" placeholder="Type your message" bind:value={message} />
      <button class="send-button" on:click={handleAdd}>Send</button>
    </div>
    <h3>Messages:</h3>
    <ul class="messages-list">
      {#each messages as msg}
        <li class="message-item"><strong>{msg.username}:</strong> {msg.message}</li>
      {/each}
    </ul>
  </div>
  
  <style>
    .chat-container {
      display: flex;
      flex-direction: column;
      box-shadow: 0 4px 20px rgb(10, 34, 255, 0.5);
      padding: 1rem;
      border-radius: 8px;
      background-color: #5bb4a4;
      max-width: 700px;
      margin: 0 auto;
    }
  
    .input-container {
      display: flex;
      margin-bottom: 1rem;
    }
  
    .message-input {
      flex: 1;
      padding: 0.5rem;
      border: 1px solid #7e3f3f;
      border-radius: 4px;
      margin-right: 0.5rem;
    }
  
    .send-button {
      padding: 0.5rem 1rem;
      border: none;
      border-radius: 4px;
      background-color: #007bff;
      color: white;
      cursor: pointer;
    }
  
    .send-button:hover {
      background-color: #0056b3;
    }
  
    .messages-list {
      list-style-type: none;
      padding: 0;
    }
  
    .message-item {
      padding: 0.5rem;
      border-bottom: 1px solid #41ad16;
    }
  
    .message-item:last-child {
      border-bottom: none;
    }
  </style>