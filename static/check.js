// Save the checkbox state to localStorage
function saveCheckboxState(checkboxId) {
    const isChecked = document.getElementById(checkboxId).checked;
    localStorage.setItem(checkboxId, isChecked);
}

// Load and apply the saved checkbox states on page load
function loadCheckboxStates() {
    const checkboxes = document.querySelectorAll('.grocery-checkbox');
    checkboxes.forEach(checkbox => {
        const isChecked = localStorage.getItem(checkbox.id) === 'true'; // localStorage stores everything as strings
        checkbox.checked = isChecked;
    });
}

// Load checkbox states when the window loads
window.onload = loadCheckboxStates;