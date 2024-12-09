<!-- Chat.svelte -->
<script lang="ts">
	//essa é a sintaxe pra avisar que messages,message e handleadd sao variaveis compartilhadas com quem usa o componente
	export let messages: { username: string; content: string }[];
	export let message = "Hello sir";
	export let handleAdd: () => void;
</script>

<div class="box">
	<h3>Messages:</h3>
	<ul class="messages-list">
		{#each messages as msg}
			<li class="message-item box">
				<strong>{msg.username}:</strong>
				{msg.content}
			</li>
		{/each}
	</ul>
	<div class="field is-flex is-align-items-center is-justify-content-center">
		<input
		  class="input"
		  type="text"
		  placeholder="Type your message"
		  bind:value={message}
		/>
		<button class="button" on:click={handleAdd}>Send</button>
	  </div>
</div>
