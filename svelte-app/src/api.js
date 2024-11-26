const API_URL = "http://127.0.0.1:8000";

export async function fetchData() {
    const response = await fetch(`${API_URL}/data`);
    return response.json();
}

export async function addData(key, value) {
    const response = await fetch(`${API_URL}/data`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ key, value }),
    });
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail);
    }
    return response.json();
}

export async function deleteData(key) {
    const response = await fetch(`${API_URL}/data/${key}`, { method: "DELETE" });
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail);
    }
    return response.json();
}
