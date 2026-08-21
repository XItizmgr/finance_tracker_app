const accountModal = document.getElementById("accountModal");
const accountForm = document.getElementById("accountForm");
const modalTitle = document.getElementById("account-modal-title");
const modalDescription = document.getElementById(
    "account-modal-description"
);
const accountNameInput = document.getElementById("account_name");
const accountTypeInput = document.getElementById("account_type");
const balanceInput = document.getElementById("balance");
const editButtons = document.querySelectorAll(".edit-account-btn");
function openAccountModal() {
    modalTitle.textContent = "Add Account";
    modalDescription.textContent =
        "Add an account to your FinTrack.";
    accountForm.action = "/account";
    accountNameInput.value = "";
    accountTypeInput.value = "";
    balanceInput.value = "";
    accountModal.showModal();
}
function openEditModal(id, name, type, balance) {
    modalTitle.textContent = "Edit Account";
    modalDescription.textContent =
        "Update your account information.";
    accountForm.action = `/account/edit/${id}`;
    accountNameInput.value = name;
    accountTypeInput.value = type;
    balanceInput.value = balance;
    accountModal.showModal();
}
function closeAccountModal() {
    accountModal.close();
}
editButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const id = button.dataset.id;
        const name = button.dataset.name;
        const type = button.dataset.type;
        const balance = button.dataset.balance;
        openEditModal(
            id,
            name,
            type,
            balance
        );
    });

});
accountModal.addEventListener("click", (event) => {

    if (event.target === accountModal) {
        closeAccountModal();
    }

});