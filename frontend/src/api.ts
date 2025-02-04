export const apiUrl= import.meta.env.VITE_API_URL

interface Message{
    username: string;
    content:string;
}


export async function addMessage(msg: Message){
    const response = await fetch(`${apiUrl}/addMessage`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(msg),
    })
    console.log(response);
    return response.json()
}