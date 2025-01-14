// JavaScript code to load and display the chart
const ctx = document.getElementById('lineChart').getContext('2d');

// Sample data (replace with your data)
const data = {
    labels: ["Week 1", "Week 2", "Week 3", "Week 4"],
    datasets: [
        {
            label: 'Keyword Occurrences',
            data: [10, 15, 8, 12],  // Replace with your actual data
            fill: false,
            borderColor: 'rgba(75, 192, 192, 1)',
            tension: 0.1
        }
    ]
};

const config = {
    type: 'line',
    data: data,
};

const myChart = new Chart(ctx, config);

// Provide feedback
const feedbackText = document.getElementById('feedback-text');
feedbackText.textContent = "This chart shows the trend of mental health topics over the past month.";
