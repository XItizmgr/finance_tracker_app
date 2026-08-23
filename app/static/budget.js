const budgetModal = document.getElementById("budgetModal");
const newBudgetBtn = document.getElementById("new-budget-btn")
const emptynewbudgetBtn = document.getElementById("empty-new-budget-btn")
const closeBudgetModal = document.getElementById("close-budget-modal")
const cancelbudgetModal = document.getElementById("cancel-budget-modal")
function openBudgetModal(){
    budgetModal.showModal()
}
function closeBudgetModalFunction() {
    budgetModal.close();
  }
if(newBudgetBtn){
    newBudgetBtn.addEventListener("click",openBudgetModal)
}
if(emptynewbudgetBtn){
    emptynewbudgetBtn.addEventListener("click",openBudgetModal)
}
closeBudgetModal.addEventListener("click",closeBudgetModalFunction)
cancelbudgetModal.addEventListener("click",closeBudgetModalFunction)
budgetModal.addEventListener("click",(e)=>{
    if(e.target === budgetModal){
        closeBudgetModalFunction()
    }
})