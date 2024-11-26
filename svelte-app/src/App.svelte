<script>
    import { onMount } from "svelte";
    import { fetchData, addData, deleteData } from "./api";

    let data = {};
    let newKey = "";
    let newValue = "";
    let error = "";

    async function loadData() {
        data = await fetchData();
    }

    async function handleAdd() {
        try {
            error = "";
            await addData(newKey, newValue);
            newKey = "";
            newValue = "";
            await loadData();
        } catch (e) {
            error = e.message;
        }
    }

    async function handleDelete(key) {
        try {
            error = "";
            await deleteData(key);
            await loadData();
        } catch (e) {
            error = e.message;
        }
    }

    onMount(loadData);
</script>

<main>
    <h1>Interactive Dictionary</h1>

    {#if error}
        <p style="color: red;">{error}</p>
    {/if}

    <h2>Add Entry</h2>
    <input placeholder="Key" bind:value={newKey} />
    <input placeholder="Value" bind:value={newValue} />
    <button on:click={handleAdd}>Add</button>

    <h2>Current Data</h2>
    <ul>
        {#each Object.entries(data) as [key, value]}
            <li>
                {key}: {value} 
                <button on:click={() => handleDelete(key)}>Delete</button>
            </li>
        {/each}
    </ul>
</main>

<style>
    input {
        margin-right: 10px;
    }
    button {
        margin-left: 10px;
    }
</style>
