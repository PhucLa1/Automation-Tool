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

async function addBonus() {
    try {
        const result = await eel.add_bonus_main(); // Gọi hàm login từ Python
    } catch (error) {
        console.error("Error:", error);
    }
}

async function addDeduction() {
    try {
        const result = await eel.add_deduction_main(); // Gọi hàm login từ Python
    } catch (error) {
        console.error("Error:", error);
    }
}

async function addTaxRate() {
    try {
        const result = await eel.add_tax_rate_main(); // Gọi hàm login từ Python
    } catch (error) {
        console.error("Error:", error);
    }
}

async function addBonusError() {
    try {
        const result = await eel.add_bonus_error_main(); // Gọi hàm login từ Python
    } catch (error) {
        console.error("Error:", error);
    }
}