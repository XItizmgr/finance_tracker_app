const data = window.dashboardData;
const financialCanvas = document.getElementById("financialChart");

let financialChart = null;


function createFinancialChart(period = "12M") {

    if (!financialCanvas) {
        return;
    }

    const periodData = data.periods[period];

    if (!periodData) {
        return;
    }


    if (financialChart) {
        financialChart.destroy();
    }


    financialChart = new Chart(financialCanvas, {

        type: "bar",

        data: {

            labels: periodData.labels,

            datasets: [

                {
                    label: "Income",

                    data: periodData.income,

                    backgroundColor: "#c94f00",

                    borderRadius: 5,

                    borderSkipped: false,

                    barPercentage: 0.65,

                    categoryPercentage: 0.7
                },

                {
                    label: "Expenses",

                    data: periodData.expenses,

                    backgroundColor: "#eaded5",

                    borderRadius: 5,

                    borderSkipped: false,

                    barPercentage: 0.65,

                    categoryPercentage: 0.7
                }

            ]

        },


        options: {

            responsive: true,

            maintainAspectRatio: false,


            plugins: {

                legend: {

                    position: "bottom",

                    labels: {

                        boxWidth: 8,

                        boxHeight: 8,

                        usePointStyle: true,

                        pointStyle: "circle",

                        padding: 20,

                        color: "#6b625d",

                        font: {
                            size: 11
                        }

                    }

                },


                tooltip: {

                    backgroundColor: "#22201e",

                    padding: 10,

                    callbacks: {

                        label: function (context) {

                            return (
                                " " +
                                context.dataset.label +
                                ": Rs. " +
                                Number(context.raw).toLocaleString()
                            );

                        }

                    }

                }

            },


            scales: {

                x: {

                    grid: {
                        display: false
                    },

                    border: {
                        display: false
                    },

                    ticks: {

                        color: "#6b625d",

                        font: {
                            size: 11
                        }

                    }

                },


                y: {

                    beginAtZero: true,

                    grid: {
                        color: "#f0e5dd"
                    },

                    border: {
                        display: false
                    },

                    ticks: {

                        color: "#6b625d",

                        font: {
                            size: 11
                        },

                        callback: function (value) {

                            return "Rs. " +
                                Number(value).toLocaleString();

                        }

                    }

                }

            }

        }

    });

}
createFinancialChart("12M");

const periodButtons =
    document.querySelectorAll(".chart-period");


periodButtons.forEach((button) => {

    button.addEventListener("click", () => {

        const period = button.dataset.period;
        periodButtons.forEach((btn) => {

            btn.classList.remove(
                "bg-white",
                "font-semibold",
                "text-[#c94f00]",
                "shadow-sm"
            );

            btn.classList.add(
                "text-gray-500"
            );

        });

        button.classList.add(
            "bg-white",
            "font-semibold",
            "text-[#c94f00]",
            "shadow-sm"
        );

        button.classList.remove(
            "text-gray-500"
        );
        createFinancialChart(period);

    });

});

const expenseCanvas =
    document.getElementById("expenseChart");


if (expenseCanvas) {

    new Chart(expenseCanvas, {

        type: "doughnut",

        data: {

            labels: data.expenseLabels,

            datasets: [

                {

                    data: data.expenseValues,

                    backgroundColor: [

                        "#c94f00",
                        "#d56b2a",
                        "#df8450",
                        "#e89d78",
                        "#efb69a",
                        "#f4cdb9",
                        "#f7ded1"

                    ],

                    borderWidth: 0,

                    hoverOffset: 5

                }

            ]

        },


        options: {

            responsive: true,

            maintainAspectRatio: false,

            cutout: "68%",


            plugins: {

                legend: {
                    display: false
                },


                tooltip: {

                    backgroundColor: "#22201e",

                    padding: 10,

                    callbacks: {

                        label: function (context) {

                            return (
                                " " +
                                context.label +
                                ": Rs. " +
                                Number(context.raw).toLocaleString()
                            );

                        }

                    }

                }

            }

        }

    });

}