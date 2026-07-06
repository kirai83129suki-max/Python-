let chartInstance = null;

function calc() {
    let money = Number(document.getElementById("money").value);
    let goal = Number(document.getElementById("goal").value);
    let income = Number(document.getElementById("income").value);
    let expense = Number(document.getElementById("expense").value);
    let bonus = Number(document.getElementById("bonus").value);

    let monthly = income - expense;

    let total = money;
    let months = 0;

    let history = [];
    let graph = [];

    if (monthly <= 0 && bonus <= 0) {
        document.getElementById("result").innerText =
            "この条件だと目標に到達できない";
        return;
    }

    while (total < goal && months < 1200) {
        total += monthly;
        months++;

        if (months % 12 === 0) {
            total += bonus;
        }

        history.push(`${months}ヶ月目：${total.toLocaleString()}円`);
        graph.push(total);
    }

    // ===== 結果 =====
    let progress = Math.min((total / goal) * 100, 100);

    document.getElementById("result").innerHTML =
        `目標まで約 ${months} ヶ月<br>
        達成率：${progress.toFixed(1)}%`;

    // ===== 履歴 =====
    document.getElementById("history").innerHTML =
        history.join("<br>");

    // ===== 進捗バー =====
    document.getElementById("bar").value = progress;

    // ===== グラフ =====
    let canvas = document.getElementById("chart");
    let ctx = canvas.getContext("2d");

    if (chartInstance) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {
        type: "line",
        data: {
            labels: graph.map((_, i) => i + 1),
            datasets: [{
                label: "貯金推移",
                data: graph,
                borderWidth: 2,
                fill: false
            }]
        }
    });
}