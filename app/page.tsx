"use client";

import { useState } from "react";

function rot13(str: string): string {
  return str.replace(/[a-zA-Z]/g, (ch) => {
    const base = ch <= "Z" ? 65 : 97;
    return String.fromCharCode(((ch.charCodeAt(0) - base + 13) % 26) + base);
  });
}

export default function Home() {
  const [input, setInput] = useState("");

  return (
    <main
      style={{
        maxWidth: 600,
        margin: "4rem auto",
        padding: "0 1rem",
      }}
    >
      <h1>ROT13</h1>
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type text here..."
        rows={6}
        style={{
          width: "100%",
          fontSize: "1rem",
          padding: "0.5rem",
          boxSizing: "border-box",
        }}
      />
      <h2>Result</h2>
      <pre
        style={{
          background: "#f4f4f4",
          padding: "1rem",
          whiteSpace: "pre-wrap",
          wordBreak: "break-word",
          minHeight: "3rem",
        }}
      >
        {rot13(input)}
      </pre>
    </main>
  );
}
