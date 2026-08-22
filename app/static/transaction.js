const transactionModal = document.getElementById("transactionModal")
const NewTransactionBtn = document.getElementById("new-transaction-btn")
const emptyAddBtn = document.getElementById("empty-add-transaction-btn")
const CloseTransactionBtn = document.getElementById("close-transaction-modal")
const cancelTransactionBtn = document.getElementById("cancel-transaction-modal")
if (NewTransactionBtn) {
    NewTransactionBtn.addEventListener("click", () => {
        transactionModal.showModal()
    })
}
if (emptyAddBtn) {
    emptyAddBtn.addEventListener('click', () => {
        transactionModal.showModal()
    })
}
if (CloseTransactionBtn) {
    CloseTransactionBtn.addEventListener("click", () => {
        transactionModal.close();
    })
}
if (cancelTransactionBtn) {
    cancelTransactionBtn.addEventListener("click", () => {
        transactionModal.close();
    });
}
transactionModal.addEventListener("click", (event) => {
    if (event.target === transactionModal) {
        transactionModal.close();
    }
});