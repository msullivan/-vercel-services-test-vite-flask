<script>
	let input = $state('');

	function rot13(str) {
		return str.replace(/[a-zA-Z]/g, (ch) => {
			const base = ch <= 'Z' ? 65 : 97;
			return String.fromCharCode(((ch.charCodeAt(0) - base + 13) % 26) + base);
		});
	}
</script>

<svelte:head>
	<title>ROT13</title>
</svelte:head>

<main>
	<h1>ROT13</h1>
	<textarea bind:value={input} placeholder="Type text here..." rows="6"></textarea>
	<h2>Result</h2>
	<pre>{rot13(input)}</pre>
</main>

<style>
	main {
		max-width: 600px;
		margin: 4rem auto;
		padding: 0 1rem;
		font-family: system-ui, sans-serif;
	}

	textarea {
		width: 100%;
		font-size: 1rem;
		padding: 0.5rem;
		box-sizing: border-box;
	}

	pre {
		background: #f4f4f4;
		padding: 1rem;
		white-space: pre-wrap;
		word-break: break-word;
		min-height: 3rem;
	}
</style>
