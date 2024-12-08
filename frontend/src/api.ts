export const apiUrl= import.meta.env.VITE_API_URL

interface Message{
    username: string;
    message:string;
}


export async function addFetchData(msg: Message){
    const response = await fetch(`${apiUrl}/addData`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(msg),
    })
    console.log(response);
    return response.json()
}