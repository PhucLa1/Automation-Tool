async function loginAdmin() {
    try {
        const result = await eel.login()(); // Gọi hàm login từ Python
    } catch (error) {
        console.error("Error:", error);
    }
}