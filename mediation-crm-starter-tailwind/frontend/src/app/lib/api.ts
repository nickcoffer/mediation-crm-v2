export const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export function getToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("access_token");
}

// Kept for compatibility with other pages - just reads the token, no auto-login
export function ensureLoggedIn(): string | null {
  return getToken();
}

export function logout() {
  if (typeof window === "undefined") return;
  localStorage.removeItem("access_token");
}

export async function login(username: string, password: string) {
  const res = await fetch(`${API_BASE}/api/auth/jwt/create/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });
  if (!res.ok) throw new Error("Login failed");
  return res.json();
}

export async function getCases(token: string) {
  const res = await fetch(`${API_BASE}/api/cases/`, {
    headers: { Authorization: `Bearer ${token}` },
    cache: "no-store",
  });
  if (!res.ok) throw new Error("Failed to fetch cases");
  return res.json();
}

export async function getCase(id: string, token: string) {
  const res = await fetch(`${API_BASE}/api/cases/${id}/`, {
    headers: { Authorization: `Bearer ${token}` },
    cache: "no-store",
  });
  if (!res.ok) throw new Error("Failed to fetch case");
  return res.json();
}
