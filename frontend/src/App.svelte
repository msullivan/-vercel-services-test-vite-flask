<script>
  const operations = [
    { id: "rot13", label: "ROT13" },
    { id: "base64encode", label: "Base64 Encode" },
    { id: "base64decode", label: "Base64 Decode" },
    { id: "rot8000", label: "ROT8000" },
  ];

  let input = $state("bss-ol-bar");
  let output = $state("");
  async function runOp(op) {
    output = "";
    try {
      const res = await fetch(`/cipher/api/${op}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: input }),
      });
      if (!res.ok) {
        output = `Error: ${res.status} ${res.statusText}`;
        return;
      }
      const data = await res.json();
      output = data.result;
    } catch (err) {
      output = `Error: ${err.message}`;
    }
  }
</script>

<main>
  <h1>Cipher Tool</h1>
  <textarea bind:value={input} placeholder="Enter text…" rows="6"></textarea>
  <div class="buttons">
    {#each operations as op}
      <button onclick={() => runOp(op.id)}>{op.label}</button>
    {/each}
  </div>
  <textarea value={output} placeholder="Result" rows="6" readonly></textarea>
  <a href="/cipher/api/status">
    <img src="/cipher/api/status.svg" alt="Backend: unreachable" class="status-img"
      onerror={(e) => { e.target.style.display='none'; e.target.nextElementSibling.style.display='block'; }} />
    <div class="status status-error" style="display:none">Backend: unreachable</div>
  </a>
</main>

<style>
  main {
    width: 100%;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  h1 {
    text-align: center;
    font-size: 1.5rem;
    font-weight: 600;
  }

  textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #334155;
    border-radius: 0.5rem;
    background: #1e293b;
    color: #e2e8f0;
    font-family: ui-monospace, monospace;
    font-size: 0.95rem;
    resize: vertical;
  }

  textarea:focus {
    outline: 2px solid #6366f1;
    outline-offset: -1px;
  }

  .buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  button {
    flex: 1 1 auto;
    padding: 0.6rem 1rem;
    border: none;
    border-radius: 0.5rem;
    background: #6366f1;
    color: #fff;
    font-size: 0.9rem;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.15s;
  }

  button:hover {
    background: #4f46e5;
  }

  button:active {
    background: #4338ca;
  }

  .status-img {
    width: 100%;
    height: 32px;
    display: block;
  }

  .status {
    text-align: center;
    font-size: 0.8rem;
    color: #94a3b8;
    padding: 0.5rem;
    border: 1px solid #334155;
    border-radius: 0.5rem;
    background: #1e293b;
  }

  .status-error {
    color: #f87171;
    border-color: #7f1d1d;
    background: #450a0a;
  }
</style>
