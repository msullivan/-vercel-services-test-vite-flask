const input = document.getElementById("input");
const output = document.getElementById("output");

document.querySelectorAll("[data-op]").forEach((btn) => {
  btn.addEventListener("click", async () => {
    const op = btn.dataset.op;
    output.value = "";
    try {
      const res = await fetch(`/_/backend/api/${op}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: input.value }),
      });
      const data = await res.json();
      if (!res.ok) {
        output.value = `Error: ${data.error || res.statusText}`;
        return;
      }
      output.value = data.result;
    } catch (err) {
      output.value = `Error: ${err.message}`;
    }
  });
});
