<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './Counter.svelte'
  import Chat from './components/Chat.svelte'
  import { apiUrl, addFetchData } from './api.js'

  let messages = [{ username: 'gpt', message: 'hello, im gpt' }, {username:'fulano', message:"my brother is ciclano"}];
  let username = 'Fulano';
  let message = '';
  let error = '';

  //again, this function is purely an example.
  async function handleAdd() {
    try {
      messages = await addFetchData({ username: username, message: message });
      console.log(`messages: ${messages}`);
      message = '';
    } catch (e: any) {
      error = e.message || e;
    }
  }
</script>

<main>
  <div>
    <h3>This is the chat component:</h3>
    <!--  Repare que passamos pro chat a função handleAdd definida aqui que sera chamada quando o botao for apertado-->
    <Chat {handleAdd} bind:messages={messages} bind:message={message} />
  </div>
</main>