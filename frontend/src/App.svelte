<script lang="ts">
    import svelteLogo from './assets/svelte.svg'
    import viteLogo from '/vite.svg'
    import Counter from './Counter.svelte'
    import {apiUrl, addFetchData} from './api.js'

  let messages = [{ username: 'gpt', message: 'hello, im gpt' }, {username:'fulano', message:"my brother is ciclano"}];
  let username = 'Fulano';
  let message = '';
  let error = '';

    async function  handleAdd() {
      try {        
        messages =  await addFetchData({username:username, message:message});
        console.log(`messages: ${messages}`)
        message='';
      } catch (e: any){
        error = e.message || e;
      }
    }



  </script>
  
  <main>
    <div>
      <h3>Send message:</h3>
      <input placeholder="Type your message" bind:value={message}/>
      <button onclick="{handleAdd}">Send</button>
      <h3>Messages:</h3>
      <ul>
        {#each messages as msg}
          <li>{msg.username}: {msg.message}</li>
        {/each}


      <p>url da api {apiUrl}</p>
      <a href="https://vite.dev" target="_blank" rel="noreferrer">
        <img src={viteLogo} class="logo" alt="Vite Logo" />
      </a> 
      <a href="https://svelte.dev" target="_blank" rel="noreferrer">
        <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
      </a>
    </div>
    <h1>Vite + Svelte</h1>
  
    <div class="card">
      <Counter />
    </div>
  
    <p>
      Check out <a href="https://github.com/sveltejs/kit#readme" target="_blank" rel="noreferrer">SvelteKit</a>, the official Svelte app framework powered by Vite!
    </p>
  
    <p class="read-the-docs">
      Click on the Vite and Svelte logos to learn more
    </p>
  </main>
  
  <style>
    .logo {
      height: 6em;
      padding: 1.5em;
      will-change: filter;
      transition: filter 300ms;
    }
    .logo:hover {
      filter: drop-shadow(0 0 2em #646cffaa);
    }
    .logo.svelte:hover {
      filter: drop-shadow(0 0 2em #ff3e00aa);
    }
    .read-the-docs {
      color: #888;
    }
  </style>
  