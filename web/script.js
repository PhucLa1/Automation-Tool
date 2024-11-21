async function loginAdmin() {
    try {
        const result = await eel.login()(); // Gọi hàm login từ Python
    } catch (error) {
        console.error("Error:", error);
    }
}

async function addPosition() {
    try {
        const result = await eel.add_position_main(); // Gọi hàm login từ Python
    } catch (error) {
        console.error("Error:", error);
    }
}