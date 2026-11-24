import { useState } from "react";

export default function App() {
  const [status, setStatus] = useState<string>("checking");

  async function checkHealth() {
    try {
      const res = await fetch("/api/healthz");
      const json = await res.json();
      setStatus(json.status);
    } catch {
      setStatus("unreachable");
    }
  }

  return (
    <div className="min-h-screen flex flex-col">
      <header className="border-b bg-white px-6 py-4">
        <h1 className="text-xl font-semibold text-slate-900">Personal AI Brain</h1>
        <p className="text-sm text-slate-500">
          Day 2: backend + frontend scaffolding complete
        </p>
      </header>
      <main className="flex-1 flex flex-col items-center justify-center p-6">
        <div className="w-full max-w-md rounded-xl border bg-slate-900/90 p-6 text-white shadow-xl">
          <h2 className="text-lg font-bold mb-2">Backend Status</h2>
          <p className="mb-4">
            <span className={`font-mono ${status === "ok" ? "text-emerald-400" : "text-rose-400"}`}>
              {status}
            </span>
          </p>
          <button
            onClick={checkHealth}
            className="w-full px-4 py-2 rounded bg-emerald-600 hover:bg-emerald-500 text-sm font-medium transition"
          >
            Refresh
          </button>
        </div>
      </main>
    </div>
  );
}
