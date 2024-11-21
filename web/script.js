async function loginAdmin() {
    try {
        const result = await eel.login_admin_main(); // Gọi hàm login từ Python
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

async function addContract() {
    try {
        const result = await eel.add_contract_main(); // Gọi hàm login từ Python
    } catch (error) {
        console.error("Error:", error);
    }
}

async function approveDecline() {
    try {
        const result = await eel.approve_decline_main(); // Gọi hàm login từ Python
    } catch (error) {
        console.error("Error:", error);
    }
}